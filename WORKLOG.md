# WORKLOG.md

Append-only history. Each entry records what changed, why, and what evidence exists.

---

## 2026-06-14 — Import latest manuscript and integrate StateDD workflow

**Scope:** Update `the-last-light` to the latest author-ready manuscript from `ff-vault/` and overlay the StateDD v2 workflow.

**What changed:**
- Imported `The_Last_Light_Author_Ready_Final.md` from `/home/ff/Documents/ff-vault/` as:
  - `The-Last-Light.md` (canonical manuscript)
  - `e.Combined-Book/The-Last-Light_Author-Ready_Final.md` (dated copy)
- Archived previous 35-chapter split-file manuscript:
  - Moved `a.The-Last-Light-Book/`, `b.Philosophical-Lenses/`, `c.Appendices/` to `archive/legacy-manuscript/`.
- Updated Docsify site entry points:
  - `README.md` rewritten for new title and StateDD workflow.
  - `index.html` meta tags, repo URL, and search namespace updated.
  - `_coverpage.md` rewritten.
  - `nl/README.md` and `nl/_coverpage.md` updated with stale-translation warnings.
  - Generated new `_sidebar.md` from canonical headings via `f.Scripts/generate-sidebar.py`.
- Integrated StateDD v2 workflow:
  - Added `AGENTS.md`, `STATUS.md`, `PROJECT_STATE.yaml`, `PROJECT_DNA.yaml`, `PROJECT_ADAPTER.yaml`, `NEXT_ACTIONS.md`, `BACKLOG.md`.
  - Added `docs/EVIDENCE_LOG.md`, `docs/ACCEPTANCE_FREEZES.md`, and ADR template.
  - Added `scripts/check_state_docs.py`, `scripts/statedd_handoff.py`, `scripts/statedd_doctor.py`, `scripts/statedd_audit.py`.
  - Added `prompts/` with all StateDD prompt templates.
  - Added `.github/ISSUE_TEMPLATE/`, `.github/pull_request_template.md`, `.github/workflows/statedd-validate.yml`.

**Evidence:**
- Source file: `/home/ff/Documents/ff-vault/The_Last_Light_Author_Ready_Final.md`
- Canonical manuscript: `The-Last-Light.md` (7,514 lines)
- Archive: `archive/legacy-manuscript/`
- Sidebar generator: `f.Scripts/generate-sidebar.py`

**Verification performed:**
- Confirmed canonical manuscript copied successfully.
- Confirmed old directories moved to archive (not deleted).
- Confirmed `_sidebar.md` includes all 22 chapters, interludes, epilogue, and 7 appendices.

**Remaining risks:**
- Legacy `f.Scripts/combine-book.sh` references archived paths.
- Dutch translation is stale.
- Docsify rendering not yet runtime-verified.

**Next action:** NA-1 — user review of StateDD baseline.

---

## 2026-06-14 — Merge Flemish-market adaptation workspace from the-last-light-v2

**Scope:** Extract the unique Dutch/Flemish-market adaptation materials and evidence from `/home/ff/Documents/Projects/the-last-light-v2/` and merge them into the canonical project. Do not treat the v2 manuscript or DOCX as canonical.

**What changed:**
- Copied `the_last_light_flemish_market/` from v2 into current project as `flemish-market/`.
- Copied v2 evidence artifacts into `docs/evidence/2026-06-04-bootstrap-docx-audit/` and `docs/evidence/2026-06-04-dutch-sample-gate/`.
- Appended v2 evidence entries to `docs/EVIDENCE_LOG.md`.
- Appended v2 worklog history to this file.
- Updated `PROJECT_STATE.yaml`, `STATUS.md`, `BACKLOG.md`, and `NEXT_ACTIONS.md` to track the Flemish-market adaptation.

**What was NOT merged:**
- `The_Last_Light.md` from v2 (different manuscript version; canonical remains `The-Last-Light.md`).
- `the_last_light.docx` and `The_Last_Light_Manuscript.docx` (source DOCX files remain in v2 until deletion).
- v2 StateDD contract files (current project already has its own StateDD baseline).

**Evidence:**
- `flemish-market/README.md`
- `flemish-market/manuscript_status.md`
- `flemish-market/samples_for_publishers/sample_auteursnoot_inleiding_h1.md`
- `docs/evidence/2026-06-04-bootstrap-docx-audit/`
- `docs/evidence/2026-06-04-dutch-sample-gate/`

**Verification performed:**
- Confirmed `flemish-market/` copied with all subdirectories.
- Confirmed evidence artifacts copied.
- Re-ran `python3 scripts/check_state_docs.py` — PASSED.

**Next action:** NA-4 — review Flemish-market sample voice.

---

## 2026-06-04 - Dutch/Flemish Sample Gate Draft (from the-last-light-v2)

- Drafted `flemish-market/samples_for_publishers/sample_auteursnoot_inleiding_h1.md`.
- Covered the required first-gate scope: Auteursnoot, Inleiding, and Hoofdstuk 1.
- Used the recommended working title and subtitle.
- Marked the sample as awaiting human review and not publisher-ready.
- Checked the sample for raw TODO/VERIFY markers; none were found.
- Checked the sample for non-ASCII characters after cleanup; none were found.
- Recorded evidence in `docs/evidence/2026-06-04-dutch-sample-gate/sample_gate_verification.txt`.

## 2026-06-04 - Manuscript Project Bootstrap Baseline (from the-last-light-v2)

- Received user strategic intake for a Flemish-market adaptation of *The Last Light*.
- Refreshed system and repo investigation.
  - OS: Fedora Linux 44 (Workstation Edition)
  - Kernel: 7.0.10-201.fc44.x86_64
  - Python: 3.14.5
  - Node: 22.22.2
  - npm: 10.9.7
  - pnpm: 11.2.2
  - Pandoc: 3.7.0.2
  - LibreOffice: 26.2.3.2
- Identified `the_last_light.docx` as the active source because it is newer than `The_Last_Light_Manuscript.docx`.
- Preserved the active source DOCX and extracted it to Markdown under `flemish-market/source_preserved/`.
- Created initial editorial reports for formatting cleanup, factual claims, repetition, terminology, adaptation choices, style, and title options.
- Replaced template-oriented README/state/backlog content with manuscript-project baseline truth.
- Created active queue for the first operating slice: Dutch/Flemish sample gate and factual-claim ledger expansion.
- Ran `python3 scripts/check_state_docs.py --bootstrap-gate`; gate passed before mode flip.
- Updated `AGENTS.md` and state files from bootstrap to operating mode.

## 2026-06-03 - Bootstrap Initialization (from the-last-light-v2)

- Cloned StateDD Template from https://github.com/lennertvhoy/StateDD_Template
- Initialized new project "the-last-light-v2" via `scripts/init_template.py`
- Moved template files to project root
- Initialized git repository on branch `main`, HEAD `3e56b73`
- System investigation completed
  - OS: Fedora Linux 44 (Workstation Edition)
  - Kernel: 7.0.10-201.fc44.x86_64
  - Python: 3.14.5
  - Node: 22.22.2
  - npm: 10.9.7
  - pnpm: installed
  - Podman: 5.8.2
  - Docker: not installed
- Repo structure investigated; no contradictions found
- Updated `PROJECT_STATE.yaml`, `STATUS.md`
- Awaiting user strategic intake to continue bootstrap
