import os
import re

def clean_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        original_content = f.read()

    content = original_content

    # 1. Remove Standard Contributors Block (**Contributors:** ... **Contributors List:** ...)
    pattern_standard = r'\*\*Contributors:\*\*.*?\*\*Contributors List:\*\*.*?(?:- Original Author.*?)?(?:\n\s*---)?'
    content = re.sub(pattern_standard, '', content, flags=re.DOTALL)

    # 2. Remove HTML Comments (<!-- Contributor Note: ... -->)
    pattern_html = r'<!--\s*Contributor Note:.*?-->'
    content = re.sub(pattern_html, '', content, flags=re.DOTALL)

    # 3. Remove Single Line Contributors (*Contributor: ...*)
    pattern_line = r'^\s*\*Contributor:.*?\*\s*'
    content = re.sub(pattern_line, '', content, flags=re.MULTILINE)

    # 4. Remove Blockquote Contributors (> **Contributor Note:** ...)
    pattern_blockquote = r'^>\s*\*\* Contributor Note:\*\*.*?(?=\n\s*\n|\n#|$)'
    content = re.sub(pattern_blockquote, '', content, flags=re.DOTALL | re.MULTILINE)

    # 5. Remove "Contributors" footer prompts
    pattern_footer = r'\*Contributors: Please add any new appendix references here.*?\*'
    content = re.sub(pattern_footer, '', content, flags=re.DOTALL)
    
    # 6. Clean up potential leftover multiple newlines (max 2 newlines)
    content = re.sub(r'\n{3,}', '\n\n', content)

    if content != original_content:
        print(f"Cleaning {filepath}")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

def main():
    dirs = ['a.The-Last-Light-Book', 'b.Philosophical-Lenses', 'c.Appendices']
    for d in dirs:
        if os.path.exists(d):
            for root, _, files in os.walk(d):
                for file in files:
                    if file.endswith('.md'):
                        clean_file(os.path.join(root, file))

if __name__ == '__main__':
    main()