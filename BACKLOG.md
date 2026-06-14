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
