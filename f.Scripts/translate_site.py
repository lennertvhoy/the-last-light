import os
import re
import json
import hashlib
import argparse
from pathlib import Path
from openai import OpenAI
from concurrent.futures import ThreadPoolExecutor, as_completed

# Configuration
REPO_ROOT = Path(__file__).resolve().parent.parent
SIDEBAR_PATH = REPO_ROOT / "_sidebar.md"
TARGET_LANG = "nl"
TARGET_DIR = REPO_ROOT / TARGET_LANG
CACHE_FILE = REPO_ROOT / f".translation_cache_{TARGET_LANG}.json"

# Initialize OpenAI client (expects OPENAI_API_KEY in env)
try:
    client = OpenAI()
except Exception as e:
    print(f"Warning: OpenAI client could not be initialized. {e}")
    client = None

def get_file_hash(content):
    """Returns SHA256 hash of content."""
    return hashlib.sha256(content.encode('utf-8')).hexdigest()

def load_cache():
    """Loads translation cache from JSON file."""
    if CACHE_FILE.exists():
        with open(CACHE_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_cache(cache):
    """Saves translation cache to JSON file."""
    with open(CACHE_FILE, 'w') as f:
        json.dump(cache, f, indent=2)

def get_files_from_sidebar():
    """Parses _sidebar.md to find all linked markdown files."""
    files = []
    with open(SIDEBAR_PATH, 'r') as f:
        content = f.read()
    
    # Match links like [Title](path/to/file.md)
    # We only want local markdown files
    matches = re.findall(r'\[.*?\]\((.*?\.md)\)', content)
    
    for match in matches:
        # Resolve relative paths
        full_path = (REPO_ROOT / match).resolve()
        try:
            rel_path = full_path.relative_to(REPO_ROOT)
            if full_path.exists():
                files.append(rel_path)
            else:
                print(f"Warning: Referenced file not found: {rel_path}")
        except ValueError:
            # Path is not relative to repo root (e.g. external link), skip
            pass
            
    return list(set(files)) # unique files



def translate_sidebar():
    """Translates the _sidebar.md file and adjusts links to be absolute /nl/ paths."""
    print("Translating Sidebar...")
    with open(SIDEBAR_PATH, 'r') as f:
        content = f.read()

    # Rewrite links to point to /nl/ directory
    # Regex to find standard markdown links: [Title](path/to/file)
    # We use negative lookbehind (?<!!) to ensure we don't match images ![Alt](url)
    
    def replace_link(match):
        title = match.group(1)
        url = match.group(2)
        
        if url.startswith('http') or url.startswith('/'):
            return f"[{title}]({url})"
        
        # Check if it's a known file or directory structure
        # We blindly prefix /nl/ because we are mirroring the structure
        return f"[{title}](/nl/{url})"

    rewritten_content = re.sub(r'(?<!\!)\[(.*?)\]\((.*?)\)', replace_link, content)
    
    target_sidebar = TARGET_DIR / "_sidebar.md"
    target_sidebar.parent.mkdir(parents=True, exist_ok=True)
    
    with open(target_sidebar, 'w') as f:
        f.write(rewritten_content)

def fix_relative_paths(text):
    """
    Adjusts relative paths in the translated content.
    Since content is moved to nl/subdir, relative links to assets (images) need an extra ../
    Links to other markdown files should remain as is (pointing to the translated sibling).
    """
    def replace_path(match):
        alt = match.group(1)
        url = match.group(2)
        
        # specific check for markdown files - keep them relative (sibling)
        if url.endswith('.md') or '#' in url:
             if url.startswith('http') or url.startswith('/'):
                 return f"[{alt}]({url})"
             return f"[{alt}]({url})"

        # If it is an image or other asset
        if not url.startswith('http') and not url.startswith('/'):
            # Prepend ../ to escape the nl/ directory
            return f"![{alt}](../{url})"
        
        return f"![{alt}]({url})"

    # Fix images: ![Alt](url)
    text = re.sub(r'!\[(.*?)\]\((.*?)\)', replace_path, text)
    return text
    
def translate_content(text, filename="content"):
    """Translates text to Dutch using OpenAI API."""
    if not client:
        print("Error: OpenAI client not initialized. Set OPENAI_API_KEY.")
        return text # Return original if no client

    print(f"Translating {filename}...")
    
    system_prompt = (
        "You are a professional translator for a philosophical sci-fi book called 'The Last Light'. "
        "Translate the following Markdown content from English to Dutch. "
        "Guidelines:\n"
        "1. Preserve all Markdown formatting, links, images, and code blocks exactly.\n"
        "2. Do NOT translate code blocks (content inside ```...```).\n"
        "3. Preserve the specific tone: philosophical, slightly melancholic, intellectual, yet accessible.\n"
        "4. Output ONLY the translated markdown, no preamble.\n"
        "5. Translate headers and link text, but NOT link targets (URLs).\n"
        "6. Leave HTML tags as is unless they contain translatable text.\n"
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text}
            ],
            temperature=0.3
        )
        translated_text = response.choices[0].message.content
        
        # Post-process paths
        translated_text = fix_relative_paths(translated_text)
        
        return translated_text
        
    except Exception as e:
        print(f"Error translating {filename}: {e}")
        return text



def process_file(rel_path, cache, args):
    """Worker function to process a single file."""
    src_path = REPO_ROOT / rel_path
    dst_path = TARGET_DIR / rel_path
    
    try:
        with open(src_path, 'r') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {rel_path}: {e}")
        return

    current_hash = get_file_hash(content)
    # Note: cache access needs to be thread-safe if we were writing to it concurrently, 
    # but here we just read. We will return the result to main thread to update cache.
    cached_hash = cache.get(str(rel_path))
    
    if not args.force and current_hash == cached_hash and dst_path.exists():
        return None # Skipped

    # Translate
    translated_text = translate_content(content, filename=str(rel_path))
    
    # Add footer disclaimer
    disclaimer = "\n\n---\n*Vertaald door AI. Controleer de originele Engelse versie bij twijfel.*"
    if disclaimer not in translated_text:
            translated_text += disclaimer

    # Write file
    dst_path.parent.mkdir(parents=True, exist_ok=True)
    with open(dst_path, 'w') as f:
        f.write(translated_text)
        
    return (str(rel_path), current_hash)

def main():
    parser = argparse.ArgumentParser(description="Translate site to Dutch")
    parser.add_argument("--force", action="store_true", help="Force re-translation of all files")
    parser.add_argument("--workers", type=int, default=5, help="Number of parallel workers")
    args = parser.parse_args()

    # Create target directory
    TARGET_DIR.mkdir(parents=True, exist_ok=True)

    cache = load_cache()
    files = get_files_from_sidebar()
    
    print(f"Found {len(files)} files to process.")

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        future_to_file = {executor.submit(process_file, f, cache, args): f for f in files}
        
        for future in as_completed(future_to_file):
            rel_path = future_to_file[future]
            try:
                result = future.result()
                if result:
                    path, new_hash = result
                    cache[path] = new_hash
                    # Save cache incrementally (not perfectly thread-safe but low risk for this use case)
                    save_cache(cache)
                    print(f"Completed: {path}")
                else:
                    print(f"Skipped (up to date): {rel_path}")
            except Exception as e:
                print(f"File {rel_path} generated an exception: {e}")

    # Translate sidebar last
    translate_sidebar()
    
    # Create a _navbar.md for switching languages if needed, or just let index.html handle it.
    # For now, we are done.

if __name__ == "__main__":
    main()
