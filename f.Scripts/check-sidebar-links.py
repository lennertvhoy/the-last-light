import os
import re

def check_sidebar_links():
    sidebar_path = "/home/ff/Documents/the-last-light/_sidebar.md"
    
    with open(sidebar_path, 'r') as f:
        content = f.read()
    
    # Find all links in the sidebar
    links = re.findall(r'\[.*?\]\((.*?)\)', content)
    
    # Check if each link points to an existing file
    missing_files = []
    for link in links:
        # Skip external links
        if link.startswith('http'):
            continue
        
        # Construct the full path
        full_path = os.path.join("/home/ff/Documents/the-last-light", link)
        
        # Check if the file exists
        if not os.path.exists(full_path):
            missing_files.append(link)
    
    return missing_files

# Check the sidebar links
missing_files = check_sidebar_links()

if missing_files:
    print("The following files are referenced in the sidebar but don't exist:")
    for file in missing_files:
        print(f"  - {file}")
else:
    print("All files referenced in the sidebar exist.")