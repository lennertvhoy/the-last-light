# PowerShell script to combine all book chapters into a single file.
# It automatically finds all .md files in the numbered directories and orders them alphabetically.

# Define the output directory and filename
$outputDir = ".\_build"
$projectRoot = "."
$outputFile = "$outputDir\The-Last-Light_Combined.md"

# Ensure the output directory exists
if (-not (Test-Path -Path $outputDir)) {
    New-Item -ItemType Directory -Path $outputDir | Out-Null
}

# --- Book Structure ---
# Find all numbered directories and sort them numerically.
$chapterDirs = Get-ChildItem -Path $projectRoot -Directory | Where-Object { $_.Name -match "^\d{2}-" -and $_.Name -notin "11-scripts", "12-scripts", "13-summary", "10-appendices" } | Sort-Object Name

# --- Header ---
$header = @"
# THE LAST LIGHT
## A Field Guide to Our Digital Crossroads

---
"@

# --- Main Logic ---
# Initialize with header
Set-Content -Path $outputFile -Value $header -Encoding UTF8

# Process each directory and its markdown files
foreach ($dir in $chapterDirs) {
    Write-Host "Processing directory: $($dir.Name)" -ForegroundColor Cyan
    
    # Find all .md files in the directory and sort them
    $mdFiles = Get-ChildItem -Path $dir.FullName -Filter "*.md" | Sort-Object Name
    
    foreach ($file in $mdFiles) {
        Write-Host "  Appending file: $($file.Name)"
        
        # Add a clean separator
        $separator = "`r`n`r`n---\r`n`r`n"
        Add-Content -Path $outputFile -Value $separator -Encoding UTF8
        
        # Get content and append
        $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8
        Add-Content -Path $outputFile -Value $content -Encoding UTF8
    }
}

# --- Completion Message ---
Write-Host "`nBook combined successfully!" -ForegroundColor Green
Write-Host "Output file: $outputFile"