#!/bin/bash

# Bash script to combine all book chapters into a single file.
# It automatically finds all .md files in the numbered directories and orders them.

# --- Configuration ---
OUTPUT_DIR="./build"
TIMESTAMP=$(date +%Y%m%d%H%M%S)
OUTPUT_FILE="$OUTPUT_DIR/The-Last-Light_Combined_$TIMESTAMP.md"
PROJECT_ROOT="."
EXCLUDE_APPENDICES=false

# --- Argument Parsing ---
if [[ "$1" == "--without-appendices" ]]; then
    EXCLUDE_APPENDICES=true
    echo "Excluding appendices from the combined book."
fi

# Ensure the output directory exists
mkdir -p "$OUTPUT_DIR"

# --- Header ---
HEADER="# THE LAST LIGHT\n## A Field Guide to Our Digital Crossroads\n\n---"

# --- Main Logic ---
# Initialize with header
echo -e "$HEADER" > "$OUTPUT_FILE"

# Find all numbered directories, sort them, and process them
find "$PROJECT_ROOT" -maxdepth 1 -type d -name "Part-*" | sort | while read -r dir; do
    # Skip appendices if the flag is set
    if [[ "$EXCLUDE_APPENDICES" == true && "$dir" == *"Part-11-Appendices"* ]]; then
        echo "Skipping directory: $dir"
        continue
    fi

    echo "Processing directory: $dir"
    
    # Find all .md files in the directory, sort them, and process them
    find "$dir" -maxdepth 1 -type f -name "*.md" | sort | while read -r file; do
        echo "  Appending file: $file"
        
        # Add a clean separator and the file content
        echo \n\n---\n' >> "$OUTPUT_FILE"
        cat "$file" >> "$OUTPUT_FILE"
    done
done

# --- Completion Message ---
echo -e "\nBook combined successfully!"
echo "Output file: $OUTPUT_FILE"
