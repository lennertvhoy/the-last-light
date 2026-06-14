# Evidence: Dutch/Flemish Sample Gate 2026-06-04

**Slice:** Draft and mechanically verify the first Dutch/Flemish sample gate.
**Backlog ID:** BL-006
**Agent ID:** NA-4
**Date:** 2026-06-04

## Claims

### Claim 1: Dutch/Flemish sample file created
- **Evidence:** `flemish-market/samples_for_publishers/sample_auteursnoot_inleiding_h1.md`
- **Verification:** File exists and contains Auteursnoot, Inleiding, and Hoofdstuk 1.

### Claim 2: Sample is explicitly marked as awaiting human review
- **Evidence:** Header/note in sample file states it is not publisher-ready.
- **Verification:** Text search confirms the warning is present.

### Claim 3: Sample passes mechanical quality checks
- **Evidence:** `sample_gate_verification.txt`
- **Verification:**
  - Required three sections present
  - No raw TODO/VERIFY markers
  - No non-ASCII characters after cleanup

## Runtime Identity

- repo: /home/ff/Documents/Projects/the-last-light-v2 (at time of original creation)
- merged_into: /home/ff/Documents/Projects/the-last-light
- branch: main
- head: 221d7be

## Test / Build / Lint Commands Run

```bash
# shell checks documented in sample_gate_verification.txt
```

## Notes

- Original evidence created in the-last-light-v2 on 2026-06-04.
- Merged into the canonical project on 2026-06-14.
- The sample is awaiting human voice review; no acceptance freeze should be recorded yet.
