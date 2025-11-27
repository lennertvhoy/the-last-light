import os
import glob

def fix_b_headers():
    print("Fixing headers in b.Philosophical-Lenses...")
    files = glob.glob("b.Philosophical-Lenses/*.md")
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        chapter_index = -1
        for i, line in enumerate(lines):
            if line.strip().startswith("# Chapter"):
                chapter_index = i
                break
        
        if chapter_index > 0:
            print(f"  Fixing {os.path.basename(filepath)}")
            new_lines = lines[chapter_index:]
            with open(filepath, 'w', encoding='utf-8') as f:
                f.writelines(new_lines)
        else:
            print(f"  Skipping {os.path.basename(filepath)} (No split point found)")

def fix_c_headers():
    print("\nFixing headers in c.Appendices...")
    files = glob.glob("c.Appendices/*.md")
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        if not lines:
            continue

        # Find first non-empty line
        first_content_index = 0
        for i, line in enumerate(lines):
            if line.strip():
                first_content_index = i
                break
        
        first_line = lines[first_content_index].strip()
        
        # Check if it's already a header
        if not first_line.startswith("#"):
            print(f"  Fixing {os.path.basename(filepath)}")
            # Add header marker
            lines[first_content_index] = "# " + lines[first_content_index]
            with open(filepath, 'w', encoding='utf-8') as f:
                f.writelines(lines)
        else: 
             # Double check it is H1 and not H2
             if first_line.startswith("##"):
                  print(f"  Promoting H2 to H1 in {os.path.basename(filepath)}")
                  lines[first_content_index] = lines[first_content_index][1:] # Remove one #
                  with open(filepath, 'w', encoding='utf-8') as f:
                    f.writelines(lines)


if __name__ == "__main__":
    fix_b_headers()
    fix_c_headers()
