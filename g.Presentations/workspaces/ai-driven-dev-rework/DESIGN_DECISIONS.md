# Design Decisions — AI-Driven Development Course Rework

**Scope:** Record the major design decisions reached by merging the four sub-deliverables.  
**Source files:**
- `course-rework.md`
- `prompt-screenshots.md`
- `prompt-website.md`
- `cli-gui-recommendation.md`

---

## Decision 1 — Hybrid CLI/GUI track vs. single interface

### Decision
Adopt a **hybrid track** for the 3.5-hour workshop. Developers default to CLI; non-developers default to GUI. Both tracks produce identical StateDD artifacts (seven state files, work contract, proof bundle, CTO-review outcome).

### Rationale
Trial feedback split cleanly: Caner (developer) was comfortable with CLI; Lennert (less technical) found GUI lower cognitive load. The target audience is mixed, so a single default would either alienate laypeople (CLI-only) or undersell developers (GUI-only). The real teaching objective is that the workflow is interface-agnostic.

### Alternatives considered
1. **CLI-only default.** Rejected: raises the floor too high for managers, policy staff, and writers.
2. **GUI-only default.** Rejected: developers see it as toy tooling and lose trust in reproducibility claims.
3. **Single "neutral" demo using only the prompt-copy website.** Rejected: attendees still need to see prompts pasted into a real tool; abstraction alone does not teach execution.

### Trade-offs
| Upside | Downside |
|--------|----------|
| Serves both audience segments. | Requires two demo recordings or live runs. |
| Reinforces that StateDD is a discipline, not a tool. | Risk of "tool religion" debates if not framed carefully. |
| GUI track lowers activation barrier. | GUI tools may lack full feature parity (e.g., running `statedd_audit.py`). |
| CLI track preserves traceability and scriptability. | Non-developers may still feel behind if CLI demo dominates. |

### Related deliverable files
- `cli-gui-recommendation.md` §4, §7
- `course-rework.md` §7
- `prompt-screenshots.md` "Two tracks, same truth" design principle

---

## Decision 2 — Docsify page vs. standalone prompt site

### Decision
Use a **Docsify sub-page** under the existing site (`/#/ai-driven-dev/prompts`) as the primary prompt-copy website, and generate a **static HTML one-pager** as a secondary offline handout.

### Rationale
The project already runs on Docsify (`index.html`, `_sidebar.md`, `_coverpage.md`). A Docsify page requires no new build pipeline or hosting account, keeps branding consistent, and lets the prompt source live in version-controlled Markdown. Hash fragments provide stable short links for slide footers.

### Alternatives considered
1. **Standalone static HTML site.** Rejected as primary: adds a new build pipeline and another artifact to keep in sync. Kept as the printable export only.
2. **PDF handout with prompts.** Rejected: copy-paste from PDF is brittle; links are not clickable in print; version control is awkward.
3. **Third-party documentation platform (Notion, Confluence, etc.).** Rejected: moves canonical truth outside the repo; creates drift risk.

### Trade-offs
| Upside | Downside |
|--------|----------|
| Reuses existing Docsify infrastructure. | Prompt site is coupled to the book site's build and hosting. |
| Markdown source stays in git. | Requires a generator script to stay in sync with `prompts/`. |
| Stable hash-fragment URLs for slides. | Short URL still depends on the project domain. |
| One-pager export supports offline attendees. | One-pager is a second generated artifact that must be regenerated on every prompt change. |

### Related deliverable files
- `prompt-website.md` §5, §6, §7
- `course-rework.md` §8

---

## Decision 3 — PersonaLab BL-002 as live demo vs. staged screenshots

### Decision
**Undecided.** Prepare for both: build one canonical BL-002 repo, attempt a live demo, and keep staged screenshots with clear "fictional UI" labels as a fallback. The live-vs-staged choice is recorded as a blocker until a runnable demo is confirmed.

### Rationale
A live demo has higher credibility and lets attendees see real runtime identity proof. However, the trial showed attendees did not know PersonaLab, so even a live demo needs a heavy context sandwich. If the app is not runnable during production, staged screenshots prevent demo failure.

### Alternatives considered
1. **Always live.** Rejected for now: dependency on a runnable PersonaLab instance, correct tooling, and a stable consent-gate UI during the session.
2. **Always staged.** Rejected as primary: reduces the "runtime identity" teaching impact; attendees may treat screenshots as faked.
3. **Drop BL-002 and use a simpler example.** Rejected: the existing deck already anchors on BL-002; replacing it would require rewriting slides 21, 33, 38, and the proof-bundle exercise.

### Trade-offs
| Upside | Downside |
|--------|----------|
| Live demo proves runtime identity concretely. | Higher risk of technical failure during the workshop. |
| Staged fallback guarantees a clean narrative. | Attendees may discount proof-bundle claims. |
| Context sandwich reduces prior-knowledge dependency either way. | Requires extra prep to produce both live material and screenshots. |

### Related deliverable files
- `course-rework.md` §6
- `prompt-screenshots.md` blockers / open questions

---

## Decision 4 — Screenshot count and placement

### Decision
Insert **ten short screenshot moments** at workflow handoffs where responsibility shifts between human, CTO-agent, and coding-agent. Each moment is capped at 90 seconds of presenter talk plus 30 seconds of silent reading. Produce GUI and CLI variants where interface differs, keeping the prompt text pixel-identical.

### Rationale
Trial participants asked "which prompt when?" Screenshots must appear at decision points, not only in an appendix. Ten moments cover setup, execution, verification, review, and escalation without overcrowding the 3.5-hour agenda.

### Alternatives considered
1. **Fewer screenshots (4–5).** Rejected: would leave gaps in the setup → contract → execute → review → handoff chain.
2. **More screenshots (12+).** Rejected: would fragment the narrative and exceed the 210-minute budget.
3. **Screenshots only in appendix/handout.** Rejected: this is the current deck's failing pattern.
4. **One generic screenshot per phase.** Rejected: attendees need the exact prompt text, not a paraphrase.

### Trade-offs
| Upside | Downside |
|--------|----------|
| Directly answers "which prompt when?" | Doubles production effort for GUI + CLI variants. |
| Anchors on canonical `prompts/` files. | Requires strict sync with prompt changes. |
| Short duration protects the agenda. | Ten moments still demand tight presenter timing. |

### Related deliverable files
- `course-rework.md` §3, §4
- `prompt-screenshots.md` full document
- `prompt-website.md` §11

---

## Decision 5 — Language: Dutch vs. English

### Decision
**Unresolved.** The source deck is Dutch/Flemish and the canonical `prompts/` are already in English. A binding decision is required before prompt translation, screenshot capture, and handout production begins.

### Rationale
Mixed signals exist: the PPTX/PDF sources are Dutch, but the StateDD contract and prompts are English. Delivering in Dutch may feel more natural for the original audience but requires translating canonical prompts and screenshots. Delivering in English aligns with the existing `prompts/` files but may require rethinking Dutch slide copy.

### Alternatives considered
1. **Dutch delivery with English prompts.** Viable but potentially jarring; attendees must context-switch between Dutch narration and English copy-paste text.
2. **English delivery with translated slide deck.** Viable but requires translating all screenshots and handouts.
3. **Bilingual materials, Dutch narration.** Highest prep cost; risks confusing slide/URL references.
4. **Keep Dutch deck, teach concepts in Dutch, point to English prompt site.** Lowest short-term cost; may leave non-English-speaking attendees copying text they do not fully understand.

### Trade-offs
| Upside | Downside |
|--------|----------|
| Dutch matches original sources and likely audience. | Requires translating prompts and screenshots. |
| English matches canonical `prompts/` and is reusable internationally. | Requires reworking Dutch slide copy. |
| Bilingual maximizes accessibility. | Doubles maintenance and proofing effort. |

### Related deliverable files
- `course-rework.md` §11 blocker 5
- `prompt-screenshots.md` blockers / open questions

---

## Decision 6 — How to handle Caner's StateDD program as a community artifact

### Decision
Treat Caner’s StateDD-based program as an **emergent community artifact**, not an official course output. List it as a placeholder on the prompt-copy website community section; replace the placeholder with a one-paragraph description and optional repo link once Caner consents and provides details.

### Rationale
Caner is productizing the workflow he learned. Featuring his project signals that StateDD is being adopted by participants, not only trainers. It also keeps the course honest about student work versus trainer-owned materials.

### Alternatives considered
1. **Make it an official course case study immediately.** Rejected: no verified details or consent yet; would overclaim maturity.
2. **Ignore it as anecdote.** Rejected: misses a high-value community signal and a chance to lower the "can this work for me?" barrier.
3. **Build a full `community-projects/` sub-site now.** Rejected: premature with only one known project; scope creep.

### Trade-offs
| Upside | Downside |
|--------|----------|
| Shows real-world adoption by a peer. | Placeholder may look empty if Caner does not provide details. |
| Low overhead (one section, one link). | Must be kept current if the project changes name or scope. |
| Encourages other attendees to submit projects. | Requires clear consent and accurate attribution. |

### Related deliverable files
- `course-rework.md` §9
- `prompt-website.md` §10
- `cli-gui-recommendation.md` §8 open question 4

---

## Decision log summary

| # | Decision | Status | Blocking next step? |
|---|----------|--------|---------------------|
| 1 | Hybrid CLI/GUI track | Resolved | No |
| 2 | Docsify page + one-pager export | Resolved | No |
| 3 | Live demo with staged fallback | Tentative | Yes — confirm runnable BL-002 |
| 4 | Ten screenshot moments, GUI/CLI variants | Resolved | No |
| 5 | Language (Dutch vs. English) | Unresolved | Yes — blocks prompt translation and screenshot capture |
| 6 | Caner's project as community artifact | Resolved pending consent | Yes — until Caner provides details |
