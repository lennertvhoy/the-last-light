# NEXT_ACTIONS.md

Active queue only. Items must be directly actionable and small enough for one coding-agent slice.

**Updated At:** 2026-06-14

Every active item references a backlog ID in the form `### Pn [BL-XXX] ...`.

---

## Active Work

### P0 [BL-021] Build AI-Driven Development prompt-copy website and start slide rework
- **Agent ID:** NA-18
- **Scope:** User confirms language and PersonaLab demo approach, then passes `g.Presentations/workspaces/ai-driven-dev-rework/HANDOFF_BUILD_PROMPT_SITE.md` to another coding agent. That agent builds the prompt-copy website on the user's existing preferred site (do not rebuild from scratch in a different stack), adds the missing `cto`/`strategy` and `override` slugs, wires one-click copy buttons, and generates a printable one-pager. After the site is live, begin updating the AI-Driven Development slide outline with the 10 new screenshot moments and hybrid CLI/GUI notes.
- **Exit:** Prompt site renders on user's existing site, all planned slugs resolve, copy buttons work, printable one-pager exists, and a revised slide outline is saved to `g.Presentations/workspaces/ai-driven-dev-rework/`.
- **Risk:** medium — depends on language decision (Dutch vs English) and live-vs-staged demo choice
- **Blocked by:** user confirms language and PersonaLab demo approach
- **Deliverables:**
  - `g.Presentations/workspaces/ai-driven-dev-rework/HANDOFF_BUILD_PROMPT_SITE.md`
  - `g.Presentations/workspaces/ai-driven-dev-rework/INTEGRATED_ACTION_PLAN.md`
  - `g.Presentations/workspaces/ai-driven-dev-rework/DESIGN_DECISIONS.md`

### P1 [BL-011] Review remaining agent-swarm course/slide maps and choose next build target
- **Agent ID:** NA-17 (completed analysis; awaiting review)
- **Scope:** After AI-Driven Development, user reviews `g.Presentations/workspaces/courses/COURSE_MAP.md` and `g.Presentations/workspaces/slides/SLIDE_MAP.md` for the other 7 presentations and picks the next course/deck to build.
- **Exit:** User approves the maps or records edits; next coding-agent slice picks the chosen build target.
- **Risk:** medium — interpretation of slide content without visuals
- **Deliverables:**
  - `g.Presentations/workspaces/courses/COURSE_MAP.md` (10 proposed courses)
  - `g.Presentations/workspaces/slides/SLIDE_MAP.md` (14 proposed decks)

### P2 [BL-001] Review and approve StateDD bootstrap baseline
- **Agent ID:** NA-1
- **Scope:** User reviews AGENTS.md, STATUS.md, PROJECT_STATE.yaml, PROJECT_DNA.yaml, PROJECT_ADAPTER.yaml, NEXT_ACTIONS.md, BACKLOG.md, WORKLOG.md.
- **Exit:** User confirms or requests edits; repo_mode updated to `operating` if accepted.
- **Risk:** low

### P2 [BL-003] Update or retire legacy combine-book.sh
- **Agent ID:** NA-2
- **Scope:** Decide whether to repurpose `f.Scripts/combine-book.sh` to copy the canonical manuscript into `e.Combined-Book/` with a timestamp, or remove it and document the new canonical-file workflow.
- **Exit:** Script no longer references archived paths; CI passes.
- **Risk:** low
- **Blocked by:** NA-1 baseline acceptance

### P3 [BL-004] Verify Docsify site renders correctly
- **Agent ID:** NA-3
- **Scope:** Run docsify-cli locally or inspect generated output; confirm sidebar loads, search works, and all chapter anchors resolve.
- **Exit:** No 404s on primary English route; any broken anchors documented.
- **Risk:** low
- **Blocked by:** NA-1 baseline acceptance

### P4 [BL-006] Review Dutch/Flemish sample gate
- **Agent ID:** NA-4
- **Scope:** Review `flemish-market/samples_for_publishers/sample_auteursnoot_inleiding_h1.md` for Dutch/Flemish voice, authority posture, compression, and market fit.
- **Exit:** Sample voice accepted for downstream adaptation or specific revision requirements recorded.
- **Risk:** medium — voice acceptance gates all downstream Flemish work
- **Blocked by:** NA-1 baseline acceptance

### P5 [BL-007] Convert source TODO/VERIFY markers into working verification ledger
- **Agent ID:** NA-5
- **Scope:** Expand `flemish-market/editorial/factual_claims_to_verify.md` into a fuller table using source locations.
- **Exit:** High-risk factual claims grouped by chapter with action labels: verify, soften, remove, or keep internal.
- **Risk:** low
- **Blocked by:** NA-1 baseline acceptance

### P0 [BL-015] Fix or retire Dutch (`/nl/`) route
- **Agent ID:** NA-11
- **Scope:** Replace the current stale/broken `/nl/` route with either a real Dutch translation or a clean "coming soon" page. No English body copy, no unstyled CTA buttons, no contradictory messaging. Do not delete `nl/` without user approval; hide or clearly deprecate it.
- **Exit:** `/nl/` renders either a real Dutch translation or a clean deprecation page; mobile and desktop screenshots captured as evidence; no 404s or unstyled links.
- **Risk:** medium — requires a user-facing decision on whether to invest in translation or deprecate
- **Blocked by:** none — hide/deprecate path does not require a full translation
- **Recommended because:** second-highest audit blocker; a broken translation route is a strong negative trust signal for Flemish/Dutch visitors.

### P1 [BL-013] Redesign coverpage as a book landing page
- **Agent ID:** NA-9
- **Scope:** Redesign `_coverpage.md` to clearly position the book: title, subtitle, one-sentence promise, primary/secondary CTAs, audience paths (reader, teacher, professional, publisher), and basic trust signals.
- **Exit:** Coverpage answers "Who is this for?" and "Why read it now?"; desktop + mobile screenshots captured.
- **Risk:** medium — copy and positioning decisions are product calls
- **Blocked by:** none
- **Recommended because:** audit ranked weak homepage positioning as a high-leverage improvement after markup cleanup and Dutch route.
