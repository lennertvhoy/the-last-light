# EVIDENCE_LOG.md

**Purpose:** Structured ledger of proof artifacts for user-facing claims.

## Entry Format

```yaml
- ID: EV-YYYY-MM-DD-001
  File: /absolute/path/to/artifact.png
  Title: short description
  Source/System: browser | api | test | log | screenshot
  Route/Page: optional route or URL
  Action: what was done
  Shows:
    - visible fact 1
    - visible fact 2
  Proves:
    - why the artifact matters
  Type: source-data | chatbot | gap | integration | docs-render-verification
  as_of: 2026-03-18T18:00:00+01:00
  Notes: optional context
```

## Guidance

- Link evidence to the specific claim it supports.
- Prefer durable artifact paths.
- Place saved artifacts under `docs/evidence/YYYY-MM-DD-<slug>/` when possible.
- Add timestamps for anything that may become stale.

## EV-2026-06-14-001: Latest manuscript imported and old manuscript archived

- File: /home/ff/Documents/Projects/the-last-light/The-Last-Light.md
- File: /home/ff/Documents/Projects/the-last-light/e.Combined-Book/The-Last-Light_Author-Ready_Final.md
- File: /home/ff/Documents/Projects/the-last-light/archive/legacy-manuscript/
- Title: Canonical manuscript updated and legacy content archived
- Source/System: file-system
- Action: Copied `The_Last_Light_Author_Ready_Final.md` from `ff-vault/` and moved old split-file directories to `archive/legacy-manuscript/`
- Shows:
  - canonical manuscript is 7,514 lines and 800 KB
  - old `a.The-Last-Light-Book/`, `b.Philosophical-Lenses/`, `c.Appendices/` now live under `archive/legacy-manuscript/`
- Proves:
  - the live project points to the latest author-ready version
  - previous content is preserved, not deleted
- Type: source-data
- as_of: 2026-06-14T18:47:00+02:00

## EV-2026-06-14-002: Docsify sidebar generated from canonical headings

- File: /home/ff/Documents/Projects/the-last-light/_sidebar.md
- File: /home/ff/Documents/Projects/the-last-light/f.Scripts/generate-sidebar.py
- Title: Sidebar reflects new manuscript structure
- Source/System: script
- Action: Ran `python3 f.Scripts/generate-sidebar.py` against `The-Last-Light.md`
- Shows:
  - sidebar lists Front Matter, 22 chapters + interludes + epilogue, and 7 appendices
  - anchor slugs match Docsify default slugify
- Proves:
  - site navigation is aligned with the canonical manuscript
- Type: docs-render-verification
- as_of: 2026-06-14T18:50:00+02:00

## EV-2026-06-14-003: StateDD workflow integrated

- File: /home/ff/Documents/Projects/the-last-light/AGENTS.md
- File: /home/ff/Documents/Projects/the-last-light/PROJECT_STATE.yaml
- File: /home/ff/Documents/Projects/the-last-light/PROJECT_DNA.yaml
- File: /home/ff/Documents/Projects/the-last-light/scripts/check_state_docs.py
- Title: State Driven Development v2 workflow adopted for book project
- Source/System: test
- Action: Copied StateDD v2 template files from `lennertvhoy/StateDD_Template` and adapted content for The Last Light
- Shows:
  - contract files present and rewritten for a Docsify book project
  - hygiene/audit scripts present and executable
- Proves:
  - project now operates under explicit state, backlog, and evidence discipline
- Type: docs-render-verification
- as_of: 2026-06-14T18:51:00+02:00

## EV-2026-06-04-001: Current source DOCX extraction and bootstrap audit (from the-last-light-v2)

```yaml
ID: EV-2026-06-04-001
Files:
  - docs/evidence/2026-06-04-bootstrap-docx-audit/source_plain.txt
  - docs/evidence/2026-06-04-bootstrap-docx-audit/source_markdown.md
  - docs/evidence/2026-06-04-bootstrap-docx-audit/audit_counts.txt
  - docs/evidence/2026-06-04-bootstrap-docx-audit/todo_verify_locations.txt
  - docs/evidence/2026-06-04-bootstrap-docx-audit/top_level_headings.txt
  - docs/evidence/2026-06-04-bootstrap-docx-audit/bootstrap_gate_pre_flip.txt
Title: Current source DOCX extraction and audit
Source/System: pandoc | shell | python audit
Action: Extracted the current DOCX source and audited word count, headings, TODO/VERIFY markers, and formatting artifacts.
Shows:
  - the_last_light.docx is the current source observed on 2026-06-04
  - extracted source has about 119k English words
  - source contains 75 TODO/VERIFY markers
  - no soft-hyphen, replacement-character, U+FFFE, or unusual-control-character corruption was found in extracted Markdown
  - bootstrap gate passed before the repo mode was flipped to operating
Proves:
  - bootstrap source identity and extraction were directly verified
  - the next adaptation slice must handle factual verification before publisher-facing output
  - the repo met its bootstrap completion gate before operating mode
Type: source-data
as_of: 2026-06-04T09:35:00+02:00
Notes: The older The_Last_Light_Manuscript.docx remains in the v2 repo but is not treated as the active source. This evidence was merged from /home/ff/Documents/Projects/the-last-light-v2 on 2026-06-14.
```

## EV-2026-06-04-002: Dutch/Flemish sample gate draft verification (from the-last-light-v2)

```yaml
ID: EV-2026-06-04-002
Files:
  - flemish-market/samples_for_publishers/sample_auteursnoot_inleiding_h1.md
  - docs/evidence/2026-06-04-dutch-sample-gate/sample_gate_verification.txt
Title: Dutch/Flemish sample gate draft verification
Source/System: shell checks | manuscript artifact
Action: Created and mechanically checked the Dutch/Flemish sample gate for Auteursnoot, Inleiding, and Hoofdstuk 1.
Shows:
  - the sample file exists under the publisher samples folder
  - the recommended title and subtitle are present
  - the sample is explicitly marked as awaiting human review and not publisher-ready
  - the sample contains the required three sections
  - raw TODO/VERIFY markers were not found in the sample
  - no non-ASCII characters were found after cleanup
Proves:
  - BL-001 drafting exit criteria were mechanically satisfied
  - the sample is ready for human/CTO voice review
  - no acceptance freeze should be recorded yet because the sample voice is not accepted
Type: source-data
as_of: 2026-06-04T09:50:00+02:00
Notes: This evidence was merged from /home/ff/Documents/Projects/the-last-light-v2 on 2026-06-14.
```
