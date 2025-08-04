import os
import re

def verify_sidebar_paths():
    sidebar_path = "/home/ff/Documents/the-last-light/_sidebar.md"
    
    with open(sidebar_path, 'r') as f:
        content = f.read()
    
    # Find all links in the sidebar
    links = re.findall(r'\[.*?\]\((.*?)\)', content)
    
    # Check if each link points to an existing file and verify the path
    incorrect_paths = []
    for link in links:
        # Skip external links
        if link.startswith('http'):
            continue
        
        # Construct the full path
        full_path = os.path.join("/home/ff/Documents/the-last-light", link)
        
        # Check if the file exists
        if not os.path.exists(full_path):
            incorrect_paths.append(link)
    
    return incorrect_paths

# Verify the sidebar paths
incorrect_paths = verify_sidebar_paths()

if incorrect_paths:
    print("The following file paths in the sidebar are incorrect:")
    for path in incorrect_paths:
        print(f"  - {path}")
else:
    print("All file paths in the sidebar are correct.")