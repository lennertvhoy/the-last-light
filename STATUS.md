# The Last Light — Status

**Updated At:** 2026-06-14
**Mode:** bootstrap
**Repo:** `/home/ff/Documents/Projects/the-last-light` on branch `main`
**Git HEAD:** `73b775d`

## Current Truth

- The canonical manuscript is now `The-Last-Light.md`: "The Last Light: How to Stay Human When Everything Can Be Outsourced" (7,514 lines, 22 chapters + 7 appendices).
- The previous 35-chapter split-file manuscript has been archived under `archive/legacy-manuscript/`.
- The Docsify site (`index.html`, `_coverpage.md`, `_sidebar.md`) has been updated to serve the new manuscript.
- The Dutch translation (`nl/`) remains available but is stale; warnings have been added to `nl/README.md` and `nl/_coverpage.md`.
- State Driven Development (StateDD) workflow has been integrated: `AGENTS.md`, state files, `docs/`, `scripts/`, `prompts/`, `.github/ISSUE_TEMPLATE/`, and `statedd-validate.yml`.
- Dutch/Flemish-market adaptation workspace merged from `the-last-light-v2` into `flemish-market/` (not canonical).
- UI/UX audit completed; site is functional but not yet launch-ready as a book landing page.

## Latest Change

- Completed NA-8 / BL-012: scrubbed visible editorial markup from `The-Last-Light.md`.
- Removed 8 internal author notes (`* edit:` comments and one inline AI-assistance disclosure) from the public Author's Note.
- Preserved removed text and substantive concerns in `Evidence/02-editorial-markup-scrub-2026-06-14/03-removed-editorial-notes.md`.
- Verified local Docsify render on `http://127.0.0.1:3456/` and confirmed no `* edit:`, `TODO:`, or `FIXME:` strings remain in the rendered page body.
- Captured before/after browser screenshots with Kimi WebBridge.
- Dispositioned untracked directories: moved `docs/evidence/2026-06-14-presentation-smb-access/` into the new evidence folder; committed `g.Presentations/` in place; quarantined incomplete prompt-copy site work (`Evidence/03-prompt-copy-site/` and `docs/ai-driven-dev/`) because it belongs to BL-021/NA-18 and its status is unknown.
- Updated StateDD files and evidence log (EV-2026-06-14-009).

## Bootstrap Goal

Establish a truthful operating baseline for The Last Light project and transition to `operating` mode once the user accepts the new manuscript + StateDD setup.

## Next Step

- NA-9 / BL-015: fix or retire the Dutch (`/nl/`) route so it no longer shows English content and unstyled CTAs.
- Then NA-10 / BL-013: redesign the coverpage as a serious book landing page, or NA-11 / BL-016: improve the 404 page.
