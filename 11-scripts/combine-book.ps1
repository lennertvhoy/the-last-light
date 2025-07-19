# PowerShell script to combine all book chapters into a single file
# Generates a unique ID and preserves separate chapters

# Get current timestamp for unique ID
$timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
$uniqueId = "last-light-$timestamp"

# Define the output file
$outputFile = ".\$uniqueId.md"

# Define chapter order (following the book structure)
$chapters = @(
    ".\README.md",
    ".\00-foreword\README.md",
    ".\01-introduction\README.md",
    ".\02-part-one-the-chinese-room\README.md",
    ".\02-part-one-the-chinese-room\01-the-broken-man.md",
    ".\02-part-one-the-chinese-room\02-we-all-live-in-the-chinese-room.md",
    ".\02-part-one-the-chinese-room\03-the-leveling-effect.md",
    ".\02-part-one-the-chinese-room\04-cognitive-atrophy.md",
    ".\03-part-two-layer-8-singularity\README.md",
    ".\08-part-seven-echopraxia\README.md"
)

# Create header for combined file
$header = @"
# THE LAST LIGHT: When Gods Learn to Hate
## A Field Guide to Our Digital Crossroads

**Combined Edition**  
**Generated:** $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")  
**Version ID:** $uniqueId

---

"@

# Initialize output with header
$combinedContent = $header

# Process each chapter
foreach ($chapter in $chapters) {
    if (Test-Path $chapter) {
        Write-Host "Processing: $chapter"
        
        # Read chapter content
        $content = Get-Content $chapter -Raw -Encoding UTF8
        
        # Add chapter separator
        $combinedContent += "`n`n" + "="*80 + "`n"
        $combinedContent += "FILE: $chapter`n"
        $combinedContent += "="*80 + "`n`n"
        
        # Add chapter content
        $combinedContent += $content
        
        # Add page break
        $combinedContent += "`n`n" + "-"*80 + "`n"
        $combinedContent += "END OF: $chapter"
        $combinedContent += "`n" + "-"*80 + "`n`n"
    }
    else {
        Write-Warning "Chapter not found: $chapter"
    }
}

# Add footer
$footer = @"

---

**THE LAST LIGHT: When Gods Learn to Hate**  
**Combined Edition - Version ID: $uniqueId**  
**Generated on:** $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")

This combined version contains all available chapters as of generation time.
Individual chapter files remain unchanged.

---
"@

$combinedContent += $footer

# Write to output file
$combinedContent | Out-File -FilePath $outputFile -Encoding UTF8

Write-Host "`nBook combined successfully!" -ForegroundColor Green
Write-Host "Output file: $outputFile" -ForegroundColor Cyan
Write-Host "Version ID: $uniqueId" -ForegroundColor Yellow
Write-Host "Total chapters processed: $($chapters.Count)" -ForegroundColor Magenta

# Display file info
$fileInfo = Get-Item $outputFile
Write-Host "File size: $([math]::Round($fileInfo.Length / 1KB, 2)) KB" -ForegroundColor Gray

# Optional: Open file in default editor
$openFile = Read-Host "`nOpen combined file in default editor? (y/n)"
if ($openFile -eq 'y' -or $openFile -eq 'Y') {
    Start-Process $outputFile
}