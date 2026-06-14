# WORKLOG.md

Append-only history. Each entry records what changed, why, and what evidence exists.

---

## 2026-06-14 — Scrub visible editorial markup from canonical manuscript (NA-8 / BL-012)

**Scope:** Remove reader-visible editorial scaffolding from `The-Last-Light.md` and verify the rendered Docsify site no longer exposes internal editing notes.

**What changed:**
- Searched `The-Last-Light.md` for visible editorial markup and found 8 internal notes in the Author's Note:
  - 7 `* edit:` comments questioning voice, factual claims, and examples.
  - 1 inline `*** most of this book was written with ai agent assistance...` disclosure note.
- Removed all 8 notes from the public canonical manuscript using a targeted regex that preserved surrounding prose and spacing.
- Preserved the removed text and flagged substantive concerns in `Evidence/02-editorial-markup-scrub-2026-06-14/03-removed-editorial-notes.md`.
- Started the local Docsify server on port 3456 and verified the rendered Author's Note and Chapter 1 are clean.
- Confirmed via DOM evaluation that no `* edit:`, `TODO:`, or `FIXME:` strings remain in the rendered page body.
- Created evidence folder `Evidence/02-editorial-markup-scrub-2026-06-14/` with before/after screenshots, grep results, removed-notes ledger, and README.
- Dispositioned untracked directories found during this slice:
  - Moved `docs/evidence/2026-06-14-presentation-smb-access/` into the new evidence folder as historical evidence.
  - Left `g.Presentations/` in place as project-relevant assets to be committed.
  - Quarantined incomplete prompt-copy website work (`Evidence/03-prompt-copy-site/` and `docs/ai-driven-dev/`) inside the evidence folder because it belongs to BL-021/NA-18 and its completion status was unknown.
  - Reverted unrelated changes to `AGENTS.md` and `_sidebar.md` so this slice stays focused on BL-012.
- Updated StateDD files:
  - `STATUS.md` latest change and next step updated.
  - `PROJECT_STATE.yaml` manuscript status, site verification, and risk R7 updated.
  - `NEXT_ACTIONS.md` completed BL-012 removed; BL-015 set as next P0 slice, BL-013 as P1.
  - `BACKLOG.md` BL-012 marked completed with evidence reference.
  - `docs/EVIDENCE_LOG.md` entry EV-2026-06-14-009 added.

**Evidence:**
- `Evidence/02-editorial-markup-scrub-2026-06-14/01-grep-before-cleanup.txt`
- `Evidence/02-editorial-markup-scrub-2026-06-14/02-authors-note-before-cleanup.png`
- `Evidence/02-editorial-markup-scrub-2026-06-14/03-removed-editorial-notes.md`
- `Evidence/02-editorial-markup-scrub-2026-06-14/04-authors-note-after-cleanup.png`
- `Evidence/02-editorial-markup-scrub-2026-06-14/05-chapter1-after-cleanup.png`
- `Evidence/02-editorial-markup-scrub-2026-06-14/06-homepage-after-cleanup.png`
- `Evidence/02-editorial-markup-scrub-2026-06-14/07-grep-after-cleanup.txt`
- `Evidence/02-editorial-markup-scrub-2026-06-14/README.md`
- `docs/EVIDENCE_LOG.md` entry EV-2026-06-14-009

**Verification performed:**
- Local Docsify server returned HTTP 200 on `http://127.0.0.1:3456/`.
- Kimi WebBridge screenshots captured before and after cleanup.
- DOM evaluation confirmed no visible `* edit:`, `TODO:`, or `FIXME:` strings in rendered page body.
- `grep` confirmed no `* edit:`, `TODO`, `FIXME`, or `citation needed` strings remain in `The-Last-Light.md`.
- Intentional `VERIFY` text in Appendix A decision-tree framework card was preserved as final content.

**Remaining risks / open questions:**
- Removed notes flagged factual contradictions (who the author teaches, the fourteen-year-old example, AI-assistance disclosure scope, people's AI adoption posture). Author should review `03-removed-editorial-notes.md` and decide whether to revise prose.
- Public site will only reflect the cleanup after the next GitHub Pages deployment.

**Next action:** NA-11 / BL-015 — fix or retire the Dutch (`/nl/`) route.

---

## 2026-06-14 — Integrate trial-lesson feedback into AI-Driven Development using agent swarm

**Scope:** Use an agent swarm to rework the AI-Driven Development course based on the trial lesson: prompt confusion, missing copy-paste source, CLI-only framing, PersonaLab context gap, and tool-heavy MCP section.

**What changed:**
- Read AI-Driven Development extracted texts and analyses, plus the existing COURSE_MAP.md and SLIDE_MAP.md.
- Launched 4 parallel coder subagents:
  - `course-rework` — revised 3.5-hour workshop outline, learning objectives, screenshot insertion plan, PersonaLab context sandwich.
  - `prompt-screenshots` — 10 screenshot specifications tied to canonical prompts.
  - `prompt-website` — Docsify sub-page design with stable short-link slugs and one-click copy.
  - `cli-gui-recommendation` — hybrid CLI/GUI track recommendation for mixed audience.
- Launched 1 synthesis subagent to merge the four deliverables into:
  - `g.Presentations/workspaces/ai-driven-dev-rework/INTEGRATED_ACTION_PLAN.md`
  - `g.Presentations/workspaces/ai-driven-dev-rework/DESIGN_DECISIONS.md`
- User indicated they already have a good site; wrote handoff prompt for another coding agent:
  - `g.Presentations/workspaces/ai-driven-dev-rework/HANDOFF_BUILD_PROMPT_SITE.md`
- Updated StateDD files:
  - `PROJECT_STATE.yaml` new `ai_driven_dev_rework` section.
  - `NEXT_ACTIONS.md` new P0 NA-18 for building the prompt site and slide rework.
  - `BACKLOG.md` new BL-021.
  - `docs/EVIDENCE_LOG.md` entries EV-2026-06-14-007 and EV-2026-06-14-008.
  - `STATUS.md` latest change updated.

**Evidence:**
- `g.Presentations/workspaces/ai-driven-dev-rework/course-rework.md`
- `g.Presentations/workspaces/ai-driven-dev-rework/prompt-screenshots.md`
- `g.Presentations/workspaces/ai-driven-dev-rework/prompt-website.md`
- `g.Presentations/workspaces/ai-driven-dev-rework/cli-gui-recommendation.md`
- `g.Presentations/workspaces/ai-driven-dev-rework/INTEGRATED_ACTION_PLAN.md`
- `g.Presentations/workspaces/ai-driven-dev-rework/DESIGN_DECISIONS.md`
- `g.Presentations/workspaces/ai-driven-dev-rework/HANDOFF_BUILD_PROMPT_SITE.md`
- `docs/EVIDENCE_LOG.md` entries EV-2026-06-14-007 and EV-2026-06-14-008

**Verification performed:**
- Confirmed all 5 subagent deliverables, 2 synthesis files, and the handoff prompt exist and are non-empty.
- Re-ran `python3 scripts/check_state_docs.py --bootstrap-gate` — PASSED.

**Remaining risks / open questions:**
- Delivery language: Dutch source deck vs English delivery.
- Live vs staged PersonaLab BL-002 demo.
- Exact URL/path on user's existing site.
- GUI tool versions must be tested for feature parity with CLI.

**Next action:** NA-18 — user confirms language and demo approach, then hands off `HANDOFF_BUILD_PROMPT_SITE.md` to another coding agent to build the prompt-copy website on the user's existing site.

---

## 2026-06-14 — UI/UX audit of The Last Light Docsify site

**Scope:** Perform a browser-based UI/UX review of the local and public Docsify site, capture evidence, and update StateDD docs with findings and recommended next slice.

**What changed:**
- Started local Docsify server on port 3456.
- Inspected desktop and mobile viewports using Kimi WebBridge and Playwright viewport emulation.
- Captured 11 evidence screenshots in `Evidence/01-ui-ux-audit-2026-06-14/`.
- Wrote full audit report at `docs/ui-ux/last-light-site-audit-2026-06-14.md`.
- Updated `STATUS.md`, `PROJECT_STATE.yaml`, `BACKLOG.md`, `NEXT_ACTIONS.md`, `docs/EVIDENCE_LOG.md`.
- Added backlog items BL-012 through BL-020 derived from audit findings.
- Proposed NA-8 (BL-012) as the next implementation slice: scrub visible editorial markup from the canonical manuscript.

**Evidence:**
- `Evidence/01-ui-ux-audit-2026-06-14/README.md`
- `docs/ui-ux/last-light-site-audit-2026-06-14.md`
- `docs/EVIDENCE_LOG.md` EV-2026-06-14-005

**Verification performed:**
- Confirmed local server returns HTTP 200.
- Confirmed public GitHub Pages site matches local build.
- Confirmed search returns relevant results for "conscious delegation".
- Confirmed mobile menu opens and content reflows at 390 px width.
- Documented visible editorial markup, broken Dutch route, bare 404 page, and sidebar typography issues.

**Remaining risks:**
- Manuscript cleanup (BL-012) must be completed before the site can be promoted as a serious book landing page.
- Dutch route (BL-015) and publisher path (BL-014) need user decisions.

**Next action:** NA-8 — scrub visible editorial markup from `The-Last-Light.md`.

---

## 2026-06-14 — Complete presentation retrieval, agent-swarm analysis, and course/slide maps

**Scope:** Finish the full pipeline from SMB retrieval through agent-swarm analysis to course/slide master maps for The Last Light presentation assets.

**What changed:**
- Mounted `//192.168.122.204/Presentations` using `presentationshare` credentials after Windows agent unlocked access.
- Copied 11 files into `g.Presentations/originals/` preserving source tree.
- Created `g.Presentations/curated/` with 8 deduplicated files:
  - kept one `AI-Driven Development.pdf` (Documents copy)
  - kept newer/larger `Digitale dubbelgangers_...` from Documents
  - kept both related-format remix files
  - kept both StateDD versions pending content review
- Generated `g.Presentations/CATALOG.md`, `g.Presentations/CHECKSUMS.sha256`, and `g.Presentations/scripts/extract.py`.
- Extracted Markdown text for all 8 curated assets into `g.Presentations/extracted/`.
- Launched an AgentSwarm of 8 coder subagents, one per extracted file, producing `g.Presentations/workspaces/analysis/*.analysis.md`.
- Delegated a synthesis subagent to merge analyses into:
  - `g.Presentations/workspaces/courses/COURSE_MAP.md` (10 proposed courses)
  - `g.Presentations/workspaces/slides/SLIDE_MAP.md` (14 proposed decks)
- Updated StateDD files:
  - `STATUS.md` combined with concurrent UI/UX audit latest changes.
  - `PROJECT_STATE.yaml` presentations section marked `copied_and_deduplicated` with swarm outputs and next action NA-17.
  - `NEXT_ACTIONS.md` P0 [BL-011] agent ID corrected to NA-17 to avoid collision with UI/UX audit IDs.
  - `BACKLOG.md` BL-011 status updated to analysis complete.
  - `docs/EVIDENCE_LOG.md` entries EV-2026-06-14-005 and EV-2026-06-14-006 added.

**Evidence:**
- `g.Presentations/originals/`
- `g.Presentations/curated/`
- `g.Presentations/CATALOG.md`
- `g.Presentations/CHECKSUMS.sha256`
- `g.Presentations/extracted/`
- `g.Presentations/workspaces/analysis/`
- `g.Presentations/workspaces/courses/COURSE_MAP.md`
- `g.Presentations/workspaces/slides/SLIDE_MAP.md`
- `docs/EVIDENCE_LOG.md` entries EV-2026-06-14-005 and EV-2026-06-14-006

**Verification performed:**
- Confirmed SMB mount succeeded with new credentials.
- Confirmed `rsync` copied 159,857,934 bytes without errors.
- Verified curated file checksums match originals.
- Confirmed extraction script produced Markdown for all 8 curated assets.
- Confirmed 8 analysis files and 2 synthesis map files exist and are non-empty.
- Re-ran `python3 scripts/check_state_docs.py --bootstrap-gate` — PASSED.

**Remaining risks:**
- Agent-swarm analysis based on extracted text only; visuals/diagrams may be missed.
- StateDD versioned pair and related-format pairs need human content review.
- Course/slide maps need user approval before building any deck.

**Next action:** NA-17 — user reviews COURSE_MAP.md and SLIDE_MAP.md and chooses the first build target.

---

## 2026-06-14 — Retrieve, deduplicate, and prepare presentation assets for agent-swarm development

**Scope:** Mount the corrected SMB share, copy 11 presentations into the project, apply deduplication rules, extract text, and prepare the StateDD workflow for course/slide development.

**What changed:**
- Mounted `//192.168.122.204/Presentations` using credentials for `presentationshare`.
- Created `g.Presentations/` directory structure:
  - `originals/` — exact mirror of the SMB share tree (11 files)
  - `curated/` — deduplicated canonical set (8 files)
  - `archive/older-versions/` — reserved for removed older copies
  - `meta/` — Windows agent HANDOFF and MANIFEST
  - `scripts/extract.py` — PPTX/PDF to Markdown extractor
  - `extracted/` — Markdown text for all curated assets
  - `workspaces/courses/` and `workspaces/slides/` — empty outputs directories
  - `CATALOG.md` — inventory and deduplication decisions
  - `CHECKSUMS.sha256` — integrity checksums
- Applied deduplication rules:
  - Kept one `AI-Driven Development.pdf` (Documents copy as canonical).
  - Kept newer/larger `Documents/Digitale dubbelgangers_...`, excluded older Desktop/Presentaties copy from curated.
  - Kept both `AI-20251103_lenny_remix.pptx` and `.pdf` as related formats.
  - Kept both StateDD versions for content review; v2 flagged as likely newer.
- Updated StateDD files:
  - `STATUS.md` with retrieval completion.
  - `PROJECT_STATE.yaml` presentations section now `copied_and_deduplicated`; blocker removed; risks R4-R6 updated/added.
  - `NEXT_ACTIONS.md` P0 now NA-7 (agent-swarm analysis).
  - `BACKLOG.md` BL-011 acceptance criteria expanded.
  - `docs/EVIDENCE_LOG.md` entry EV-2026-06-14-005 added.

**Evidence:**
- `g.Presentations/originals/`
- `g.Presentations/curated/`
- `g.Presentations/CATALOG.md`
- `g.Presentations/CHECKSUMS.sha256`
- `g.Presentations/extracted/`
- `docs/EVIDENCE_LOG.md` entry EV-2026-06-14-005

**Verification performed:**
- Confirmed SMB mount succeeded and all 11 files listed.
- Confirmed `rsync` copied 159,857,934 bytes without errors.
- Verified `curated/` file checksums match corresponding `originals/` checksums.
- Confirmed `extract.py` produced Markdown for all 8 curated assets.
- Re-ran `python3 scripts/check_state_docs.py --bootstrap-gate` — PASSED.

**Remaining risks:**
- Agent-swarm analysis depends on extracted text and may miss visuals.
- StateDD versioned pair may duplicate content; needs review.
- Related-format PDF/PPTX pairs may need consolidation.

**Next action:** NA-7 — agent-swarm analysis of extracted presentations to produce course and slide maps.

---

## 2026-06-14 — Attempt to retrieve presentation assets from Windows SMB share

**Scope:** Mount `\\192.168.122.204\Presentations`, copy the 11 presentations into the project, apply the Windows agent's deduplication rules, and prepare the StateDD workflow for course/slide development.

**What changed:**
- Created evidence directory `docs/evidence/2026-06-14-presentation-smb-access/`.
- Wrote handoff request for the Windows agent: `HANDOFF_to_Windows_Agent.md`.
- Recorded sanitized mount attempt log: `mount_attempt.log`.
- Updated `STATUS.md` with the current blocker.
- Updated `PROJECT_STATE.yaml` with a `presentations` section and risk R4.
- Added backlog item `[BL-011] Retrieve and integrate presentation assets`.
- Added active item `P0 [BL-011] Restore SMB access to Windows presentation share`.
- Appended evidence entry `EV-2026-06-14-004` to `docs/EVIDENCE_LOG.md`.

**What was NOT done:**
- Files were not copied because SMB authentication failed and the attempted account was locked out.
- Deduplication was not applied.
- Agent-swarm slide/course analysis was not started.

**Evidence:**
- `docs/evidence/2026-06-14-presentation-smb-access/HANDOFF_to_Windows_Agent.md`
- `docs/evidence/2026-06-14-presentation-smb-access/mount_attempt.log`
- `docs/EVIDENCE_LOG.md` entry EV-2026-06-14-004

**Verification performed:**
- Confirmed share host reachable via ICMP.
- Confirmed SMB port 445 responds.
- Confirmed guest/anonymous access denied.
- Confirmed supplied credentials fail with `NT_STATUS_LOGON_FAILURE`.
- Confirmed repeated attempts resulted in `NT_STATUS_ACCOUNT_LOCKED_OUT`.
- Re-ran `python3 scripts/check_state_docs.py --bootstrap-gate` — PASSED.

**Remaining risks:**
- SMB access blocked until Windows agent unlocks account and provides corrected credentials.
- The 11 presentations remain on the Windows host only.

**Next action:** NA-6 — Windows agent provides corrected credentials or mount options.

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
