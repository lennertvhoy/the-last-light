# Evidence: DOCX Bootstrap Audit 2026-06-04

**Slice:** Extract and audit the active source DOCX for the Flemish-market adaptation.
**Backlog ID:** BL-007
**Agent ID:** NA-5
**Date:** 2026-06-04

## Claims

### Claim 1: Active source DOCX identified and preserved
- **Evidence:** `flemish-market/source_preserved/the_last_light_source_2026-06-04.docx`
- **Verification:** Filesystem mtime and DOCX core timestamp show `the_last_light.docx` is newer than the older manuscript candidate.

### Claim 2: Source extracted to clean Markdown
- **Evidence:** `flemish-market/source_preserved/the_last_light_source_2026-06-04.md`
- **Verification:** File exists and contains the extracted source.

### Claim 3: Source audited for formatting artifacts and TODO/VERIFY markers
- **Evidence:** `audit_counts.txt`, `todo_verify_locations.txt`, `top_level_headings.txt`
- **Verification:**
  - ~119k English words
  - 75 TODO/VERIFY markers
  - No soft-hyphen, replacement-character, U+FFFE, or unusual-control-character corruption

## Runtime Identity

- repo: /home/ff/Documents/Projects/the-last-light-v2 (at time of original creation)
- merged_into: /home/ff/Documents/Projects/the-last-light
- branch: main
- head: 221d7be

## Test / Build / Lint Commands Run

```bash
python3 scripts/check_state_docs.py --bootstrap-gate
```

## Notes

- Original evidence created in the-last-light-v2 on 2026-06-04.
- Merged into the canonical project on 2026-06-14.
- The v2 repo has since been emptied; this evidence is now the durable copy.
