import os
import re

# Logic:
# 1. Read _sidebar.md to find the ordered list of chapter files.
# 2. Assign a sequential Chapter Number (1-35) to each file found in the "Chapter N" links.
# 3. Open each file.
# 4. Iterate through lines.
# 5. Maintain counters for H2 (subsection) and H3 (subsubsection).
# 6. Replace `## Title` with `## X.Y Title` and `### Title` with `### X.Y.Z Title`.
#    X = Chapter Number
#    Y = Subsection Counter
#    Z = Subsubsection Counter
# 7. Reset counters appropriately.
# 8. Skip lines that already have the correct numbering pattern to allow idempotency.
# 9. Skip "References" or "Further Reading" sections if desired (optional, but good practice).

SIDEBAR_PATH = "/home/ff/.openclaw/workspace/repos/the-last-light/_sidebar.md"
REPO_ROOT = "/home/ff/.openclaw/workspace/repos/the-last-light"

def get_chapter_files():
    """Parses _sidebar.md to get a list of (chapter_num, file_rel_path)"""
    chapters = []
    current_chapter = 0
    
    with open(SIDEBAR_PATH, 'r') as f:
        for line in f:
            # Look for links like: - [Chapter 1: Title](path/to/file.md)
            match = re.search(r'\[Chapter (\d+):.*?\]\((.*?)\)', line)
            if match:
                chap_num = int(match.group(1))
                rel_path = match.group(2)
                chapters.append((chap_num, rel_path))
    
    # Sort just in case, though sidebar order is the truth
    return chapters

def process_file(chapter_num, rel_path):
    abs_path = os.path.join(REPO_ROOT, rel_path)
    if not os.path.exists(abs_path):
        print(f"File not found: {abs_path}")
        return

    with open(abs_path, 'r') as f:
        lines = f.readlines()

    new_lines = []
    h2_count = 0
    h3_count = 0
    
    # Regex to detect existing numbers at start of header title
    # e.g. "## 1.1 Title" or "## 1.2.1 Title"
    # We want to strip them and replace with calculated numbers
    header_regex = re.compile(r'^(#+)\s+(\d+(\.\d+)*\s+)?(.*)')

    # Skip counting for Acknowledgements/References?
    # For now, we number everything as requested, unless it's obviously "References" at the end
    
    for line in lines:
        stripped = line.strip()
        
        # Check if line is a header
        if stripped.startswith('##'):
            match = header_regex.match(line)
            if match:
                level_hashes = match.group(1)
                existing_num = match.group(2) # might be None or "1.1 "
                title_text = match.group(4)
                
                # Check for "References" or "Appendices" or "Further Reading" to skip numbering?
                # User asked for "subchapter numbering", likely implying content structure.
                # Usually References are not numbered subchapters.
                if title_text.lower().startswith("references") or title_text.lower().startswith("further reading"):
                     new_lines.append(line)
                     continue

                if level_hashes == '##':
                    h2_count += 1
                    h3_count = 0
                    new_num = f"{chapter_num}.{h2_count}"
                    new_line = f"## {new_num} {title_text}\n"
                    new_lines.append(new_line)
                    print(f"  Updated: {new_num} {title_text}")
                    
                elif level_hashes == '###':
                    h3_count += 1
                    new_num = f"{chapter_num}.{h2_count}.{h3_count}"
                    new_line = f"### {new_num} {title_text}\n"
                    new_lines.append(new_line)
                    print(f"  Updated: {new_num} {title_text}")
                else:
                    # H4 and deeper - usually not numbered in this style, or just leave as is
                    new_lines.append(line)
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)

    with open(abs_path, 'w') as f:
        f.writelines(new_lines)

def main():
    print("Reading sidebar...")
    chapters = get_chapter_files()
    print(f"Found {len(chapters)} chapters.")
    
    for chap_num, rel_path in chapters:
        print(f"Processing Chapter {chap_num}: {rel_path}")
        process_file(chap_num, rel_path)

if __name__ == "__main__":
    main()
