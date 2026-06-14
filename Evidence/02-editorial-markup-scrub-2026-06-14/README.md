# Evidence: NA-8 / BL-012 Editorial Markup Scrub

**Date:** 2026-06-14
**Agent ID:** NA-8
**Backlog ID:** BL-012
**Canonical manuscript:** `/home/ff/Documents/Projects/the-last-light/The-Last-Light.md`

## What this folder proves

This evidence shows that visible editorial scaffolding (`* edit:` comments and an inline AI-assistance disclosure note) was removed from the public-facing Author's Note of *The Last Light*, and that the rendered Docsify site no longer exposes internal editing notes to readers.

## Files

| # | File | Description |
|---|------|-------------|
| 01 | `01-grep-before-cleanup.txt` | Grep output locating 8 visible editorial notes in `The-Last-Light.md` before cleanup. |
| 02 | `02-authors-note-before-cleanup.png` | Browser screenshot of the rendered Author's Note showing visible `* edit:` markup (Kimi WebBridge). |
| 03 | `03-removed-editorial-notes.md` | The exact text of the 8 removed notes, with flagged factual/authorial concerns for review. |
| 04 | `04-authors-note-after-cleanup.png` | Browser screenshot of the rendered Author's Note after cleanup — no visible editorial markup. |
| 05 | `05-chapter1-after-cleanup.png` | Browser screenshot of Chapter 1 after cleanup. |
| 06 | `06-homepage-after-cleanup.png` | Browser screenshot of the homepage after cleanup. |
| 07 | `07-grep-after-cleanup.txt` | Grep output confirming no `* edit:`, `TODO`, `FIXME`, or `citation needed` strings remain in the manuscript. |
| 08 | `08-public-authors-note-after-push.png` | Public GitHub Pages site immediately after push — still showed cached/stale editorial markup (before storage clear). |
| 11 | `11-public-authors-note-after-cache-clear.png` | Public GitHub Pages site after clearing `localStorage`/`sessionStorage` and reloading with cache-busting query — no visible editorial markup. |
| — | `README.md` | This file. |
| — | `2026-06-14-presentation-smb-access/` | Historical evidence of the SMB access attempt, moved here from `docs/evidence/` as part of untracked-directory disposition. |
| — | `quarantine-prompt-copy-site-work/` | Incomplete prompt-copy website files (`Evidence/03-prompt-copy-site/` and `docs/ai-driven-dev/`) discovered during this slice; quarantined because they belong to BL-021/NA-18 and their completion status is unknown. |

## Verification summary

- Local Docsify server: `http://127.0.0.1:3456/`
- Public site: `https://lennertvhoy.github.io/the-last-light/`
- Browser verification: Kimi WebBridge
- DOM evaluation after cleanup: no `* edit:`, `TODO:`, or `FIXME:` strings found in the rendered page body.
- Public site initially served cached/stale content containing the old `* edit:` notes; after clearing browser `localStorage`/`sessionStorage` and reloading with a cache-busting query, the public render matched the local clean render.

## Disposition of untracked directories found during this slice

- `docs/evidence/2026-06-14-presentation-smb-access/` → moved into this evidence folder as historical evidence.
- `g.Presentations/` → project-relevant presentation assets; left in place and committed.
- `Evidence/03-prompt-copy-site/` and `docs/ai-driven-dev/` → incomplete prompt-copy website work (BL-021/NA-18) discovered mid-slice; quarantined here because its completion status and ownership are unknown. Reverted unrelated `AGENTS.md` and `_sidebar.md` changes to keep this slice focused.
