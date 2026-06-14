# BACKLOG.md

Strategic roadmap with stable backlog IDs. Do not close items here; move them to docs/ACCEPTANCE_FREEZES.md when fully accepted.

**Updated At:** 2026-06-14

---

## [BL-001] Complete StateDD bootstrap and transition to operating mode
- **Added:** 2026-06-14
- **Problem:** The project needs a truthful StateDD baseline before entering operating mode.
- **Acceptance criteria:**
  - All contract files accurately reflect the project (book manuscript, Docsify site, archived legacy content).
  - Evidence log contains real entries with durable artifact paths.
  - User reviews and accepts the baseline.
  - `repo_mode:` in AGENTS.md flipped to `operating`.
- **Next action:** NA-1 (user review)

## [BL-002] Decide disposition of legacy Dutch translation
- **Added:** 2026-06-14
- **Problem:** `nl/` contains a Dutch translation of the previous manuscript and no longer matches the canonical English manuscript.
- **Acceptance criteria:**
  - Either update `nl/` to match the new manuscript, or archive/remove it with clear user-facing messaging.
  - No broken links on the Dutch route.
- **Next action:** deferred until after NA-1

## [BL-003] Update or retire legacy combine-book.sh
- **Added:** 2026-06-14
- **Problem:** `f.Scripts/combine-book.sh` still references archived split-file directories.
- **Acceptance criteria:**
  - Script either generates dated copies from `The-Last-Light.md` or is removed and documented as legacy.
  - CI workflow remains valid.
- **Next action:** NA-2

## [BL-004] Verify Docsify site renders correctly
- **Added:** 2026-06-14
- **Problem:** New single-file manuscript + generated sidebar need runtime verification.
- **Acceptance criteria:**
  - Docsify loads without errors.
  - All sidebar chapter links resolve to the correct anchors.
  - Search plugin indexes the new manuscript.
- **Next action:** NA-3

## [BL-005] Establish manuscript update workflow
- **Added:** 2026-06-14
- **Problem:** Future updates from `ff-vault/` need a documented, repeatable process.
- **Acceptance criteria:**
  - A runbook documents how to copy a new author-ready manuscript, regenerate the sidebar, and archive the old canonical file.
  - Evidence captured in docs/EVIDENCE_LOG.md.
- **Next action:** deferred until after NA-1

## [BL-006] Review Dutch/Flemish sample gate
- **Added:** 2026-06-14
- **Source:** Merged from the-last-light-v2
- **Problem:** The drafted Dutch/Flemish sample (Auteursnoot, Inleiding, Hoofdstuk 1) needs human review before downstream adaptation.
- **Acceptance criteria:**
  - Sample voice is either accepted for downstream adaptation or specific revision requirements are recorded.
  - Authority posture, compression, and market fit are evaluated.
- **Next action:** NA-4

## [BL-007] Resolve high-risk source cleanup issues
- **Added:** 2026-06-14
- **Source:** Merged from the-last-light-v2
- **Problem:** Source contains 75 TODO/VERIFY markers and heading inconsistencies that must be resolved before publisher-facing text.
- **Acceptance criteria:**
  - `flemish-market/editorial/factual_claims_to_verify.md` expanded into a fuller table.
  - High-risk claims grouped by chapter with action labels: verify, soften, remove, or keep internal.
- **Next action:** NA-5

## [BL-008] Establish final Dutch chapter architecture
- **Added:** 2026-06-14
- **Source:** Merged from the-last-light-v2
- **Problem:** The 27-chapter English source must be compressed into a Dutch/Flemish architecture targeting 80,000-95,000 words.
- **Acceptance criteria:**
  - Final chapter list and compression map documented.
  - User accepts the architecture.
- **Next action:** deferred until after NA-4

## [BL-009] Adapt full Dutch/Flemish manuscript
- **Added:** 2026-06-14
- **Source:** Merged from the-last-light-v2
- **Problem:** Full Dutch/Flemish manuscript needs to be drafted to the target word count.
- **Acceptance criteria:**
  - Complete manuscript in Dutch/Flemish.
  - Compressed motifs, natural voice, market-appropriate examples.
- **Next action:** deferred until BL-008 accepted

## [BL-010] Research and draft publisher package
- **Added:** 2026-06-14
- **Source:** Merged from the-last-light-v2
- **Problem:** Publisher submission package for Flemish and Dutch publishers needs research and drafting.
- **Acceptance criteria:**
  - Title options finalized.
  - Publisher pitch and supporting materials drafted.
- **Next action:** deferred until BL-006 accepted

## [BL-011] Retrieve and integrate presentation assets
- **Added:** 2026-06-14
- **Problem:** Windows host has 11 presentations shared at `\\192.168.122.204\Presentations`; Fedora agent cannot authenticate to the share.
- **Acceptance criteria:**
  - SMB share mounted and files copied into project under a durable path.
  - Duplicates resolved per Windows agent handoff rules.
  - Presentations catalogued in StateDD state files and evidence log.
  - Agent-swarm analysis slice created to develop courses/slides from the assets.
- **Status:** retrieval, deduplication, extraction, and agent-swarm analysis complete; awaiting user review of course/slide maps
- **Next action:** NA-17 (user review of maps)

## [BL-021] Rework AI-Driven Development course and build prompt-copy website
- **Added:** 2026-06-14
- **Source:** Trial-lesson feedback for AI-Driven Development session
- **Problem:** Trial lesson showed prompt confusion, no copy-paste source, CLI-only framing that alienated non-developers, missing PersonaLab context, and tool-heavy MCP section.
- **Acceptance criteria:**
  - Integrated action plan and design-decisions documents reviewed and accepted.
  - Handoff prompt `HANDOFF_BUILD_PROMPT_SITE.md` delivered to another coding agent.
  - Prompt-copy website built on user's existing preferred site with stable short-link slugs and one-click copy.
  - AI-Driven Development slide outline updated with 10 screenshot moments and hybrid CLI/GUI track.
  - Missing `CTO_SESSION_PROMPT` and human-override slugs resolved.
  - Decision recorded on Dutch vs English delivery and live vs staged PersonaLab demo.
- **Status:** integrated plan ready; handoff prompt written; awaiting user confirmation of open questions
- **Next action:** NA-18 (hand off to another agent after confirming language/demo approach)

## [BL-012] Scrub canonical manuscript of visible editorial markup
- **Added:** 2026-06-14
- **Source:** UI/UX audit (NA-7)
- **Problem:** Rendered Author's Note and other sections contain visible `* edit:` annotations and cleanup markup.
- **Acceptance criteria:**
  - No visible `* edit:`, `TODO`, or `VERIFY` scaffolding in rendered `/The-Last-Light`.
  - Editorial decisions are either resolved in the text or moved to internal notes, not shown to readers.
- **Status:** completed by NA-8 on 2026-06-14; 8 editorial notes removed, rendered page verified clean, evidence captured.
- **Evidence:** Evidence/02-editorial-markup-scrub-2026-06-14/
- **Next action:** awaiting user acceptance before moving to docs/ACCEPTANCE_FREEZES.md

## [BL-013] Redesign coverpage as a book landing page
- **Added:** 2026-06-14
- **Source:** UI/UX audit (NA-7)
- **Problem:** The coverpage is a sparse Docsify cover; it does not clearly position the book for readers, educators, or publishers.
- **Acceptance criteria:**
  - Above-the-fold section states title, subtitle, promise, and primary/secondary CTAs.
  - Includes audience paths (reader, teacher, professional, publisher) and trust signals.
  - Looks credible as a serious book landing page on desktop and mobile.
- **Next action:** NA-9

## [BL-014] Add publisher/media package route
- **Added:** 2026-06-14
- **Source:** UI/UX audit (NA-7)
- **Problem:** Flemish-market publisher materials exist in `flemish-market/` but are not discoverable from the public site.
- **Acceptance criteria:**
  - A `/publisher` or `/media` route exposes title options, sample chapters, author bio, and download/contact CTAs.
  - Route is linked from the coverpage and/or README.
- **Next action:** NA-10

## [BL-015] Fix or retire Dutch (`/nl/`) route
- **Added:** 2026-06-14
- **Source:** UI/UX audit (NA-7)
- **Problem:** `/nl/` displays English content and unstyled CTA links.
- **Acceptance criteria:**
  - Either `/nl/` renders a real Dutch translation or it shows a clean "coming soon" page.
  - No unstyled buttons, no English body copy, no contradictory messaging.
- **Next action:** NA-11

## [BL-016] Improve 404 page
- **Added:** 2026-06-14
- **Source:** UI/UX audit (NA-7)
- **Problem:** Unknown routes show a bare "404 - Not found" with no recovery path.
- **Acceptance criteria:**
  - 404 page contains a home link, a search prompt, and suggested starting chapters.
- **Next action:** NA-12

## [BL-017] Improve sidebar typography and truncation
- **Added:** 2026-06-14
- **Source:** UI/UX audit (NA-7)
- **Problem:** Sidebar link labels are forced to ALL CAPS and heavily truncated, especially on mobile.
- **Acceptance criteria:**
  - Labels use sentence or title case.
  - Chapter titles are readable without excessive truncation on desktop and mobile.
- **Next action:** NA-13

## [BL-018] Add author bio and trust signals
- **Added:** 2026-06-14
- **Source:** UI/UX audit (NA-7)
- **Problem:** The site lacks author identity, endorsements, and institutional trust signals.
- **Acceptance criteria:**
  - Author bio/photo or byline appears on the site.
  - Any available endorsements, affiliations, or media mentions are displayed.
- **Next action:** NA-14

## [BL-019] Fix mobile language switcher overlap
- **Added:** 2026-06-14
- **Source:** UI/UX audit (NA-7)
- **Problem:** Fixed-position EN/NL switcher overlaps body text when scrolling on mobile.
- **Acceptance criteria:**
  - Switcher does not obscure readable text on 390–430 px wide viewports.
- **Next action:** NA-15

## [BL-020] Improve accessibility of icon-only links and language switcher
- **Added:** 2026-06-14
- **Source:** UI/UX audit (NA-7)
- **Problem:** "View source on Github" link and the language switcher lack accessible names.
- **Acceptance criteria:**
  - Icon-only links have `aria-label` text.
  - Language switcher has a clear accessible name describing its function.
- **Next action:** NA-16

## LATER

- [BL-WB-001] Use Kimi WebBridge to browser-verify any user-facing change in the real browser when available.
