# The Last Light — Status

**Updated At:** 2026-06-14
**Mode:** bootstrap
**Repo:** `/home/ff/Documents/Projects/the-last-light` on branch `main`
**Git HEAD:** `4056519`

## Current Truth

- The canonical manuscript is now `The-Last-Light.md`: "The Last Light: How to Stay Human When Everything Can Be Outsourced" (7,514 lines, 22 chapters + 7 appendices).
- The previous 35-chapter split-file manuscript has been archived under `archive/legacy-manuscript/`.
- The Docsify site (`index.html`, `_coverpage.md`, `_sidebar.md`) has been updated to serve the new manuscript.
- The Dutch translation (`nl/`) remains available but is stale; warnings have been added to `nl/README.md` and `nl/_coverpage.md`.
- State Driven Development (StateDD) workflow has been integrated: `AGENTS.md`, state files, `docs/`, `scripts/`, `prompts/`, `.github/ISSUE_TEMPLATE/`, and `statedd-validate.yml`.
- Dutch/Flemish-market adaptation workspace merged from `the-last-light-v2` into `flemish-market/` (not canonical).
- UI/UX audit completed; site is functional but not yet launch-ready as a book landing page.

## Latest Change

- Completed a UI/UX audit of the Docsify site using Kimi WebBridge (desktop) and Playwright viewport emulation (mobile).
- Evidence saved to `/home/ff/Documents/Projects/the-last-light/Evidence/01-ui-ux-audit-2026-06-14/`.
- Full report written to `docs/ui-ux/last-light-site-audit-2026-06-14.md`.
- Key blockers identified: visible editorial markup in the rendered manuscript, broken Dutch route, bare 404 page, weak publisher/media path.
- Added backlog items BL-012 through BL-020 derived from audit findings.
- Also completed end-to-end retrieval and integration of 11 Windows-hosted presentations via SMB.
- Built `g.Presentations/` with originals, curated deduplicated set, extracted Markdown, catalog, checksums, and extraction script.
- Ran an agent swarm (8 parallel subagents + 1 synthesis subagent) over the extracted presentations.
- Produced `g.Presentations/workspaces/courses/COURSE_MAP.md` (10 courses) and `g.Presentations/workspaces/slides/SLIDE_MAP.md` (14 decks).
- Updated StateDD contract files and evidence log (EV-2026-06-14-005 and EV-2026-06-14-006).

## Bootstrap Goal

Establish a truthful operating baseline for The Last Light project and transition to `operating` mode once the user accepts the new manuscript + StateDD setup.

## Next Step

- Run `python3 scripts/check_state_docs.py --bootstrap-gate` and fix any failures.
- User reviews and accepts the baseline; flip `AGENTS.md` `repo_mode` to `operating`.
