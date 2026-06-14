# The Last Light — Status

**Updated At:** 2026-06-14
**Mode:** bootstrap
**Repo:** `/home/ff/Documents/Projects/the-last-light` on branch `main`
**Git HEAD:** `404035a`

## Current Truth

- The canonical manuscript is now `The-Last-Light.md`: "The Last Light: How to Stay Human When Everything Can Be Outsourced" (7,514 lines, 22 chapters + 7 appendices).
- The previous 35-chapter split-file manuscript has been archived under `archive/legacy-manuscript/`.
- The Docsify site (`index.html`, `_coverpage.md`, `_sidebar.md`) has been updated to serve the new manuscript.
- The Dutch translation (`nl/`) remains available but is stale; warnings have been added to `nl/README.md` and `nl/_coverpage.md`.
- State Driven Development (StateDD) workflow has been integrated: `AGENTS.md`, state files, `docs/`, `scripts/`, `prompts/`, `.github/ISSUE_TEMPLATE/`, and `statedd-validate.yml`.
- Dutch/Flemish-market adaptation workspace merged from `the-last-light-v2` into `flemish-market/` (not canonical).

## Latest Change

- Imported latest manuscript from `/home/ff/Documents/ff-vault/The_Last_Light_Author_Ready_Final.md`.
- Archived old manuscript directories.
- Generated new `_sidebar.md` from canonical headings.
- Updated `README.md`, `index.html`, and cover pages.
- Integrated StateDD v2 template files, adapted for a book project.
- Merged `the-last-light-v2` Flemish-market adaptation materials into `flemish-market/`; v2 manuscript/DOCX not treated as canonical.

## Bootstrap Goal

Establish a truthful operating baseline for The Last Light project and transition to `operating` mode once the user accepts the new manuscript + StateDD setup.

## Next Step

- Run `python3 scripts/check_state_docs.py --bootstrap-gate` and fix any failures.
- User reviews and accepts the baseline; flip `AGENTS.md` `repo_mode` to `operating`.
