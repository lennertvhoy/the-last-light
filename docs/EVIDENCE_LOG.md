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

## EV-2026-06-14-006: Agent-swarm analysis produced course and slide maps

```yaml
ID: EV-2026-06-14-006
Files:
  - g.Presentations/workspaces/analysis/
  - g.Presentations/workspaces/courses/COURSE_MAP.md
  - g.Presentations/workspaces/slides/SLIDE_MAP.md
Title: Agent swarm analyzed extracted presentations and proposed course/slide architecture
Source/System: AgentSwarm | coder subagent
Action: Launched 8 parallel coder subagents, one per extracted Markdown file, to produce structured analyses; then a lead synthesis subagent merged them into COURSE_MAP.md and SLIDE_MAP.md.
Shows:
  - 8 per-presentation analysis files exist
  - COURSE_MAP.md lists 10 proposed courses with priorities, audiences, and dependencies
  - SLIDE_MAP.md lists 14 proposed decks with quick-win and needs-visual-review flags
  - cross-cutting themes mapped to The Last Light book themes
  - merge/consolidation recommendations documented
Proves:
  - extracted assets are ready for downstream course/slide development
  - a human-reviewable plan exists before building any new deck
Type: docs-render-verification
as_of: 2026-06-14T19:50:00+02:00
Notes: Maps are based on extracted text only; visuals, diagrams, and speaker notes were not available to the swarm.
```

## EV-2026-06-14-005: Presentations retrieved, deduplicated, and catalogued

```yaml
ID: EV-2026-06-14-005
Files:
  - g.Presentations/originals/
  - g.Presentations/curated/
  - g.Presentations/CATALOG.md
  - g.Presentations/CHECKSUMS.sha256
  - g.Presentations/scripts/extract.py
  - g.Presentations/extracted/
Title: Windows presentation assets copied into project and prepared for agent analysis
Source/System: cifs-utils | rsync | sha256sum | python-pptx | pdftotext
Action: Mounted //192.168.122.204/Presentations with presentationshare credentials, copied 11 files preserving original tree, created deduplicated curated set of 8 files, generated catalog and checksums, extracted Markdown text from all curated assets.
Shows:
  - 11 presentation files copied to g.Presentations/originals/
  - 8 curated files after deduplication
  - sha256 checksums verify curated copies match originals
  - extracted Markdown files exist for each curated asset
  - deduplication decisions documented in CATALOG.md
Proves:
  - presentation assets are now durably stored in the project
  - duplicates were resolved according to the Windows agent handoff rules
  - assets are ready for agent-swarm course/slide development
Type: source-data
as_of: 2026-06-14T19:45:00+02:00
Notes: Original folder structure preserved; related-format pairs and versioned pair kept in curated set pending content review.
```

## EV-2026-06-14-004: SMB share access attempt blocked by authentication failure

```yaml
ID: EV-2026-06-14-004
Files:
  - docs/evidence/2026-06-14-presentation-smb-access/HANDOFF_to_Windows_Agent.md
  - docs/evidence/2026-06-14-presentation-smb-access/mount_attempt.log
Title: Presentation SMB share reachable but not accessible
Source/System: shell | cifs-utils | smbclient
Action: Attempted to mount //192.168.122.204/Presentations from Fedora 44 using the credentials supplied by the user.
Shows:
  - share host is reachable via ICMP (TTL 128, ~0.34 ms RTT)
  - SMB port 445 responds
  - guest/anonymous access denied (NT_STATUS_ACCESS_DENIED)
  - provided credentials failed SMB session setup (NT_STATUS_LOGON_FAILURE)
  - repeated attempts resulted in NT_STATUS_ACCOUNT_LOCKED_OUT
Proves:
  - presentation retrieval is currently blocked on the Windows side, not the network path
  - Windows agent intervention is required to unlock account and provide correct credentials or mount options
Type: integration
as_of: 2026-06-14T19:30:00+02:00
Notes: Password/PIN value is intentionally omitted from this log for security. The Windows agent handoff document contains the request for corrected access details.
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

## EV-2026-06-14-005: UI/UX audit of The Last Light Docsify site

```yaml
ID: EV-2026-06-14-005
Files:
  - Evidence/01-ui-ux-audit-2026-06-14/01-coverpage-desktop.png
  - Evidence/01-ui-ux-audit-2026-06-14/02-bookpage-desktop.png
  - Evidence/01-ui-ux-audit-2026-06-14/03-chapter1-desktop.png
  - Evidence/01-ui-ux-audit-2026-06-14/04-chapter1-scrolled-desktop.png
  - Evidence/01-ui-ux-audit-2026-06-14/05-nl-coverpage-desktop.png
  - Evidence/01-ui-ux-audit-2026-06-14/06-coverpage-mobile.png
  - Evidence/01-ui-ux-audit-2026-06-14/07-bookpage-mobile.png
  - Evidence/01-ui-ux-audit-2026-06-14/08-menu-mobile.png
  - Evidence/01-ui-ux-audit-2026-06-14/10-sidebar-forced-open-desktop.png
  - Evidence/01-ui-ux-audit-2026-06-14/11-404-page-desktop.png
  - Evidence/01-ui-ux-audit-2026-06-14/12-public-live-coverpage-desktop.png
  - Evidence/01-ui-ux-audit-2026-06-14/README.md
  - docs/ui-ux/last-light-site-audit-2026-06-14.md
Title: UI/UX audit of The Last Light Docsify site
Source/System: Kimi WebBridge | Playwright viewport emulation
Action: Inspected local and public site with desktop and mobile viewports; tested navigation, search, language switcher, and 404 behavior.
Shows:
  - site is structurally sound and responsive
  - coverpage is clear but sparse
  - search returns relevant results
  - mobile menu is functional
  - visible editorial markup in Author's Note
  - Dutch route shows English content and unstyled CTAs
  - 404 page is bare
  - sidebar labels are truncated and all-caps
Proves:
  - the site is functional but not launch-ready as a book landing page
  - the highest-ROI next slice is scrubbing visible editorial markup (BL-012 / NA-8)
Type: docs-render-verification
as_of: 2026-06-14T19:50:00+02:00
Notes: 11 evidence files total. Mobile screenshots used Playwright because Kimi WebBridge cannot resize the user's real browser window.
```
