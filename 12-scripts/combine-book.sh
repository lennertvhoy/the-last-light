#!/bin/bash

# Bash script to combine all book chapters into a single file.
# It automatically finds all .md files in the numbered directories and orders them.

# Define the output directory and filename
OUTPUT_DIR="./_build"
OUTPUT_FILE="$OUTPUT_DIR/The-Last-Light_Combined.md"
PROJECT_ROOT="."

# Ensure the output directory exists
mkdir -p "$OUTPUT_DIR"

# --- Header ---
HEADER="# THE LAST LIGHT\n## A Field Guide to Our Digital Crossroads\n\n---"

# --- Main Logic ---
# Initialize with header
echo -e "$HEADER" > "$OUTPUT_FILE"

# Find all numbered directories, sort them, and process them
find "$PROJECT_ROOT" -maxdepth 1 -type d -name "[0-9][0-9]-*" | sort | grep -vE '11-scripts|12-summary|12-appendices' | while read -r dir; do
    echo "Processing directory: $dir"
    
    # Find all .md files in the directory, sort them, and process them
    find "$dir" -maxdepth 1 -type f -name "*.md" | sort | while read -r file; do
        echo "  Appending file: $file"
        
        # Add a clean separator and the file content
        echo $'\n\n---\n' >> "$OUTPUT_FILE"
        sed 's/\\n/\n/g; s/\\r/\r/g' "$file" >> "$OUTPUT_FILE"
    done
done

# --- Completion Message ---
echo -e "\nBook combined successfully!"
echo "Output file: $OUTPUT_FILE"