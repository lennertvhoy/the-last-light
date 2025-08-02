# Get the current date and time in YYYYMMDDHHMMSS format
$TIMESTAMP = Get-Date -Format "yyyyMMddHHmmss"

# Define the output directory and file names with the timestamp
$OUTPUT_DIR = "e.Combined-Book"
$OUTPUT_FILE = "${OUTPUT_DIR}/The-Last-Light_Combined_${TIMESTAMP}.md"
$OUTPUT_FILE_NO_EXTRAS = "${OUTPUT_DIR}/The-Last-Light_Combined_NoExtras_${TIMESTAMP}.md"

# Define the base directory for the book parts
$BOOK_DIR = "a.The-Last-Light-Book"

# Define the order of the parts to be combined
$PARTS = @(
    "Part-00-Introduction",
    "Part-01-The-Chinese-Room",
    "Part-02-The-Layer-8-Singularity",
    "Part-03-The-Successors",
    "Part-04-Weaponized-Consciousness",
    "Part-05-The-Oppenheimer-Moment",
    "Part-06-The-Dead-End",
    "Part-07-The-Digital-Pathogen",
    "Part-08-A-New-Beginning",
    "Part-09-Conclusion"
)

# Create or clear the output files
if (-not (Test-Path -Path $OUTPUT_DIR)) {
    New-Item -ItemType Directory -Path $OUTPUT_DIR
}
Clear-Content -Path $OUTPUT_FILE -ErrorAction SilentlyContinue
Clear-Content -Path $OUTPUT_FILE_NO_EXTRAS -ErrorAction SilentlyContinue

# Function to process and combine files
function Combine-Files($destFile, $includeExtras) {
    # Loop through the defined parts in order
    foreach ($part in $PARTS) {
        # Find all markdown files in the current part directory, sorted numerically
        Get-ChildItem -Path "${BOOK_DIR}/${part}" -Filter "*.md" | Sort-Object -Property { [int]($_.Name -replace '.*?(\d+).*?', '$1') } | ForEach-Object {
            # Add a separator and the file name before each file's content
            Add-Content -Path $destFile -Value "`n`n"
            # Append the content of the file to the destination file
            Get-Content -Path $_.FullName | Add-Content -Path $destFile
        }
    }

    # Conditionally include extra files
    if ($includeExtras) {
        # Append Philosophical Lenses
        Get-ChildItem -Path "b.Philosophical-Lenses" -Filter "*.md" | Sort-Object -Property { [int]($_.Name -replace '.*?(\d+).*?', '$1') } | ForEach-Object {
            Add-Content -Path $destFile -Value "`n`n"
            Get-Content -Path $_.FullName | Add-Content -Path $destFile
        }

        # Append Appendices
        Get-ChildItem -Path "c.Appendices" -Filter "*.md" | Sort-Object -Property { [int]($_.Name -replace '.*?(\d+).*?', '$1') } | ForEach-Object {
            Add-Content -Path $destFile -Value "`n`n"
            Get-Content -Path $_.FullName | Add-Content -Path $destFile
        }

        # Append References
        Get-ChildItem -Path "d.References" -Filter "*.md" | Sort-Object | ForEach-Object {
            Add-Content -Path $destFile -Value "`n`n"
            Get-Content -Path $_.FullName | Add-Content -Path $destFile
        }

        # Append other root-level markdown files
        Get-ChildItem -Path . -Filter "*.md" -Depth 0 | ForEach-Object {
            Add-Content -Path $destFile -Value "`n`n"
            Get-Content -Path $_.FullName | Add-Content -Path $destFile
        }
    }
}

# Combine all files including extras
Combine-Files $OUTPUT_FILE $true

# Combine files excluding extras
Combine-Files $OUTPUT_FILE_NO_EXTRAS $false

Write-Host "Book combined into ${OUTPUT_FILE}"
Write-Host "Book (no extras) combined into ${OUTPUT_FILE_NO_EXTRAS}"