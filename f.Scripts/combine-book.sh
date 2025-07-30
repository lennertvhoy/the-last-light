#!/bin/bash

# Get the current date and time in YYYYMMDDHHMMSS format
TIMESTAMP=$(date +"%Y%m%d%H%M%S")

OUTPUT_DIR="e.Combined-Book"

# Define the output file name with the timestamp
OUTPUT_FILE="${OUTPUT_DIR}/The-Last-Light_Combined_${TIMESTAMP}.md"
OUTPUT_FILE_NO_EXTRAS="${OUTPUT_DIR}/The-Last-Light_Combined_NoExtras_${TIMESTAMP}.md"

# Define the base directory for the book parts
BOOK_DIR="The-Last-Light-Book"

# Define the order of the parts to be combined
PARTS=(
    "Part-00-Introduction"
    "Part-01-The-Chinese-Room"
    "Part-02-The-Layer-8-Singularity"
    "Part-03-The-Successors"
    "Part-04-Weaponized-Consciousness"
    "Part-05-The-Oppenheimer-Moment"
    "Part-06-The-Dead-End"
    "Part-07-The-Digital-Pathogen"
    "Part-08-A-New-Beginning"
    "Part-09-Conclusion"
)

# Create or clear the output files
> "$OUTPUT_FILE"
> "$OUTPUT_FILE_NO_EXTRAS"

# Function to process and combine files
combine_files() {
    local dest_file="$1"
    local include_extras="$2"

    # Loop through the defined parts in order
    for part in "${PARTS[@]}"; do
        # Find all markdown files in the current part directory, sorted numerically
        find "${BOOK_DIR}/${part}" -name "*.md" | sort -V | while read -r file; do
            # Add a separator and the file name before each file's content
            echo -e "\n\n--- ${file} ---\n\n" >> "$dest_file"
            # Append the content of the file to the destination file
            cat "$file" >> "$dest_file"
        done
    done

    # Conditionally include extra files
    if [ "$include_extras" = "true" ]; then
        # Append Philosophical Lenses
        find "Philosophical-Lenses" -name "*.md" | sort -V | while read -r file; do
            echo -e "\n\n--- ${file} ---\n\n" >> "$dest_file"
            cat "$file" >> "$dest_file"
        done

        # Append Appendices
        find "Appendices" -name "*.md" | sort -V | while read -r file; do
            echo -e "\n\n--- ${file} ---\n\n" >> "$dest_file"
            cat "$file" >> "$dest_file"
        done

        # Append References
        find "References" -name "*.md" | sort -V | while read -r file; do
            echo -e "\n\n--- ${file} ---\n\n" >> "$dest_file"
            cat "$file" >> "$dest_file"
        done

        # Append other root-level markdown files
        find . -maxdepth 1 -name "*.md" -print0 | while IFS= read -r -d $'\0' file; do
            echo -e "\n\n--- ${file} ---\n\n" >> "$dest_file"
            cat "$file" >> "$dest_file"
        done
    fi
}

# Combine all files including extras
combine_files "$OUTPUT_FILE" "true"

# Combine files excluding extras
combine_files "$OUTPUT_FILE_NO_EXTRAS" "false"

echo "Book combined into ${OUTPUT_FILE}"
echo "Book (no extras) combined into ${OUTPUT_FILE_NO_EXTRAS}"