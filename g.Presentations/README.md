# g.Presentations — Course & Slide Asset Workspace

This directory holds presentation assets retrieved from the Windows SMB share `//192.168.122.204/Presentations` and the downstream analysis used to develop courses and slide decks for *The Last Light*.

## Quick navigation

| Path | Purpose |
|---|---|
| `originals/` | Exact mirror of the SMB share tree (11 files). |
| `curated/` | Deduplicated canonical set (8 files). |
| `extracted/` | Markdown text extracted from every curated asset. |
| `scripts/extract.py` | Python extractor for PPTX (via `python-pptx`) and PDF (via `pdftotext`). |
| `CATALOG.md` | Deduplication decisions and inventory. |
| `CHECKSUMS.sha256` | Integrity checksums for originals and curated files. |
| `workspaces/analysis/` | Per-presentation analysis reports from the agent swarm. |
| `workspaces/courses/COURSE_MAP.md` | Master map of 10 proposed courses. |
| `workspaces/slides/SLIDE_MAP.md` | Master map of 14 proposed slide decks. |
| `workspaces/courses/` / `workspaces/slides/` | Empty output directories for future built artifacts. |
| `meta/` | Windows agent handoff and manifest. |

## Agent-swarm results

- 8 parallel coder subagents analyzed the extracted Markdown files.
- 1 synthesis subagent merged the analyses into `COURSE_MAP.md` and `SLIDE_MAP.md`.
- Maps are based on extracted text only; diagrams, screenshots, and speaker notes were not available to the swarm.

## Next step

Review `workspaces/courses/COURSE_MAP.md` and `workspaces/slides/SLIDE_MAP.md`, then choose the first course or deck to build.
