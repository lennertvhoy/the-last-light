#!/bin/bash

# combine-book.sh — The Last Light
#
# The canonical manuscript is now a single file (The-Last-Light.md).
# This script creates a dated copy under e.Combined-Book/ for distribution
# or archival purposes. The previous split-file combination logic has been
# retired; the old manuscript lives in archive/legacy-manuscript/.

set -euo pipefail

TIMESTAMP=$(date +"%Y%m%d%H%M%S")
OUTPUT_DIR="e.Combined-Book"
CANONICAL="The-Last-Light.md"

mkdir -p "$OUTPUT_DIR"

OUTPUT_FILE="${OUTPUT_DIR}/The-Last-Light_Combined_${TIMESTAMP}.md"
OUTPUT_FILE_NO_EXTRAS="${OUTPUT_DIR}/The-Last-Light_Combined_NoExtras_${TIMESTAMP}.md"

if [ ! -f "$CANONICAL" ]; then
    echo "Error: canonical manuscript not found: $CANONICAL" >&2
    exit 1
fi

# Full copy (with extras placeholder for compatibility)
cp "$CANONICAL" "$OUTPUT_FILE"

# No-extras copy (same content; kept for compatibility with old consumers)
cp "$CANONICAL" "$OUTPUT_FILE_NO_EXTRAS"

echo "Book combined into ${OUTPUT_FILE}"
echo "Book (no extras) combined into ${OUTPUT_FILE_NO_EXTRAS}"
