# AI-Driven Development Course Rework Plan

**Specialty:** course-rework  
**Scope:** Rework CRS-001 / CRS-004 / CRS-005 / CRS-006 (the StateDD/AI-Driven Development family) based on the trial-lesson feedback already collected.  
**Source truth:**
- `g.Presentations/extracted/AI-Driven Development.pptx.md` (slides 1–58)
- `g.Presentations/extracted/AI-Driven Development.pdf.md`
- `g.Presentations/workspaces/analysis/AI-Driven Development.pptx.analysis.md`
- `g.Presentations/workspaces/analysis/AI-Driven Development.pdf.analysis.md`
- `g.Presentations/workspaces/courses/COURSE_MAP.md`
- `g.Presentations/workspaces/slides/SLIDE_MAP.md`
- Canonical StateDD contract: `AGENTS.md`, `STATUS.md`, `NEXT_ACTIONS.md`, `BACKLOG.md`

---

## 1. Trial-lesson diagnosis

The trial ran the existing half-day agenda (slide 45 / PDF `00:00–03:30`). The strongest friction points were:

| # | Confusion observed | Root cause in current deck |
|---|-------------------|---------------------------|
| 1 | **Which prompt when?** Participants did not know which prompt to use to set up the workflow versus to keep it running. | The coding-agent prompt and CTO-review checklist are buried in appendix slides 53–58; they appear *after* the demo, not as live prompts during the demo. |
| 2 | **No copy-paste source.** Attendees wanted the exact wording of the prompts and templates during/after the session. | Slides show prompts as static screenshots/bullets, not as a shareable, versioned web resource. |
| 3 | **CLI-only framing alienated non-developers.** One participant (Caner) was comfortable with CLI; another (Lennert) found GUI tools lower cognitive load for laypeople. | The deck demo (PersonaLab BL-002) implicitly assumes a terminal-first workflow and never names GUI alternatives. |
| 4 | **PersonaLab BL-002 assumed prior knowledge.** Attendees did not know the demo app, so "Consent Gate" and the folder tree felt abstract. | Slide 5 introduces PersonaLab in one line; slide 38 jumps straight into the 7-step demo. |
| 5 | **MCP section was tool-heavy, not decision-heavy.** Slide 29 lists 9 MCP types without linking them back to the verification gates. | Non-developers could not map "Database MCP" to "why this proves runtime identity." |

---

## 2. Keep / cut / reorder

### Keep (high value, reuse as-is)

1. **Opening hook — slides 2–4 / PDF opening.** The "agent says done, you lose two hours" frame lands well and is audience-agnostic.
2. **The 7-file StateDD template — slides 14–17 / PDF `De volledige StateDD-template`.** The role-per-file table is the mnemonic anchor; keep it, but add a one-page printable handout.
3. **Bad prompt vs. work contract — slide 21 / PDF `Slechte prompt vs Werkcontract BL-002`.** This is the course's signature before/after; keep, but update the bad example to be even more generic.
4. **Closure gates — slide 23 / PDF `Closure Gates`.** The 8 gates are concrete; keep as the checklist participants take home.
5. **Autonomy ladder + budget — slides 41, 44, 57 / PDF maturity ladder and budget.** Keep, but move the ladder earlier as a roadmap.
6. **Appendix templates — slides 53–58 / PDF appendix.** Keep, but turn them into the canonical copy-paste web source (see §7).

### Cut or condense

1. **Slide 29: "9 MCP Types" table.** Condense from 9 categories to the **5 verification verbs** the mixed audience actually needs: `see` (browser/screenshot), `run` (terminal/tests), `read` (git/files), `check` (state files), `approve` (review). Keep the table only as a reference handout, not on the main screen.
2. **Slide 26–27: subagent taxonomy.** Cut the 5-role list (coding/test/evidence/doc/CTO) down to a **2-role story** for the 3.5-hour version: the *doer* and the *checker*. Move the 5-role taxonomy to CRS-006 / the full-day track.
3. **Slide 46: full-day agenda.** Remove from the 3.5-hour deck; keep only as a speaker note / handout.
4. **Slide 50: "Begin met één regel" homily.** Keep the idea, but fold it into the closing 5-minute "tomorrow" slide.

### Reorder

1. **Move the autonomy ladder to minute 25–30.** It functions as a roadmap: "today we climb from level 0 to level 2." Currently it appears too late (slide 41, after the technical sections).
2. **Move the PersonaLab context setup before the StateDD files.** Explain the demo app in 3 minutes before asking attendees to care about `PROJECT_DNA.yaml`.
3. **Move proof bundles before subagents/MCP.** Proof bundles answer the attendee question "how do I know it worked?" before the tool discussion.

---

## 3. Where to insert prompt-screenshot moments

Prompt-screenshots are inserted at the **decision points** where the workflow changes hands between human, CTO-agent, and coding agent. The detailed screenshot specifications (exact prompt text, dimensions, UI chrome) are delegated to the `prompt-screenshots` subagent; the course-level insertion plan is below.

| # | Section / slide | New moment | Screenshot content | Why now |
|---|----------------|------------|-------------------|---------|
| A | **After opening (min 0:15)** | "The starting prompt" | Terminal/IDE/chat showing the **bootstrap intake prompt** (`prompts/BOOTSTRAP_INTAKE_PROMPT.md`). | Attendees need to see that the very first interaction is a *setup* prompt, not a coding request. |
| B | **Before StateDD file tour (min 0:35)** | "Ask the agent to read the contract first" | Coding-agent startup prompt (`prompts/CODING_AGENT_STARTUP_PROMPT.md`) with read order visible. | Explains *why* the 7 files matter: the agent is explicitly told to read them. |
| C | **During work-contract section (min 1:05)** | "From goal to work contract" | Chat window or template editor showing `SLICE_CONTRACT_TEMPLATE.md` filled in for BL-002. | Bridges slide 21's bad/good comparison with the actual prompt attendees will reuse. |
| D | **During proof-bundle section (min 1:50)** | "What the coding agent must produce" | Coding-agent prompt appendix (slide 53) rendered as a real prompt, with placeholders `<project-name>` and `<slice-id>`. | Shows that the *execution* prompt enforces the proof-bundle rule. |
| E | **During CTO-review section (min 2:15)** | "The review prompt" | `CTO_REVIEW_CHECKLIST.md` used as a prompt to a CTO-agent or as a human checklist. | Makes the ACCEPTED/CONDITIONAL/REJECTED decision reproducible. |
| F | **During autonomy ladder (min 2:35)** | "The autonomy-budget prompt" | `SLICE_CONTRACT_TEMPLATE.md` extended with autonomy-budget fields (max backlog items, stop conditions). | Shows that autonomy is set by a prompt, not by trust. |
| G | **During closing (min 3:15)** | "Your first prompt tomorrow" | A single-sentence starter prompt: *"Initialize StateDD in repo X and pick one low-risk slice."* | Reduces activation energy; attendees photograph/screenshot it. |
| H | **During closing (min 3:20)** | "Where to copy the prompts" | Browser showing the prompt-copy website (see §7). | Ties the screenshots to a durable, versioned resource. |

Each moment should be **no longer than 90 seconds** of presenter talk plus 30 seconds of silent reading. Screenshot specs for the above are requested from the `prompt-screenshots` subagent; see §8 for expected deliverable.

---

## 4. Revised 3.5-hour module sequence

Total: **210 minutes** including a 20-minute break.

| Time | Module | What happens | Key artifacts / prompts shown |
|------|--------|--------------|------------------------------|
| 0:00–0:20 (20 min) | **Opening: the two-hour "done"** | Hook slides 2–4. Poll: "Who has been surprised by an AI 'done' recently?" Set mixed-audience ground rules. | None yet; establish CLI/GUI split. |
| 0:20–0:40 (20 min) | **The real problem: missing project truth** | Context decay, fake progress, runtime confusion (slides 7–9). Introduce the repo-as-truth idea (slide 12). | Screenshot moment **A**: bootstrap intake prompt. |
| 0:40–0:55 (15 min) | **Meet PersonaLab BL-002** | 3-minute demo-app context: *a controlled sandbox for AI personas where consent must be proven*. Explain consent gate without assuming codebase knowledge. | PersonaLab one-pager handout. |
| 0:55–1:10 (15 min) | **StateDD as Project-OS** | 7-file template walkthrough (slides 14–16). Emphasize: complete in truth, small in behavior. | Screenshot moment **B**: coding-agent startup prompt with read order. |
| 1:10–1:35 (25 min) | **From CTO decision to work contract** | Translate product goal → scope → out-of-scope → acceptance criteria. Workshop: attendees rewrite one bad prompt into a work contract. | Screenshot moment **C**: filled `SLICE_CONTRACT_TEMPLATE.md`. |
| 1:35–1:55 (20 min) | **Break** | | |
| 1:55–2:20 (25 min) | **Proof bundles: no proof, no closure** | What belongs in a bundle, numbering, review outcomes (slides 31–35). Keep technical depth light; focus on *auditable handoff*. | Screenshot moment **D**: coding-agent execution prompt for BL-002. |
| 2:20–2:40 (20 min) | **Subagents, MCP, and separation of powers** | Two-role story (doer + checker). Condensed tool list mapped to the 5 verification verbs. | Optional live GUI demo for non-developers, CLI demo for developers. |
| 2:40–3:00 (20 min) | **CTO review in practice** | Interactive review of a pre-built BL-002 proof bundle. Participants vote ACCEPTED / CONDITIONAL / REJECTED. | Screenshot moment **E**: `CTO_REVIEW_CHECKLIST.md` as prompt. |
| 3:00–3:20 (20 min) | **Autonomy ladder and budget** | Introduce ladder as roadmap. Attendees draft an autonomy budget for their own team/slice. | Screenshot moment **F**: autonomy-budget prompt. |
| 3:20–3:30 (10 min) | **Tomorrow: one line, one prompt, one site** | Closing. Screenshot moments **G** and **H**. Mention Caner's StateDD-based program as a community artifact. | Handout / short URL to prompt-copy site. |

**Rationale:** The technical sections (StateDD files, work contracts, proof bundles) are front-loaded before the break so the afternoon half is *application* (review exercise, autonomy budget). This respects the 3.5-hour fatigue curve and gives non-developers more context before tools appear.

---

## 5. Learning objectives rewritten for a mixed audience

By the end of the 3.5-hour workshop, every participant will be able to:

1. **Explain why chat is not project truth.** Use the terms *context decay*, *fake progress*, and *runtime identity* in their own words, with one example from their own work.
2. **Name the seven StateDD files and one thing each protects.** Non-developers can name the human-facing files (`STATUS.md`, `BACKLOG.md`, `EVIDENCE_LOG.md`); developers must also explain the machine-facing files (`PROJECT_STATE.yaml`, `PROJECT_DNA.yaml`, `NEXT_ACTIONS.md`, `AGENTS.md`).
3. **Rewrite a vague request into a verifiable work contract.** A work contract must contain scope, out-of-scope, acceptance criteria, proof requirement, and review gate.
4. **Judge a proof bundle using the ACCEPTED / CONDITIONAL / REJECTED framework.** Identify at least one missing closure gate in a sample bundle.
5. **Choose a human-in-the-loop vs. human-on-the-loop vs. human-out-of-the-loop level for a given task.** Justify the choice with risk, proof, and autonomy budget.
6. **Copy the correct canonical prompt for setup, execution, or review.** This is measured by the prompt-copy website usage, not by memorization.
7. **Select CLI or GUI entry point based on their own role.** Developers can explain why CLI gives traceability; non-developers can explain why GUI lowers cognitive load.

---

## 6. Handling PersonaLab BL-002 without prior knowledge

The current deck assumes attendees know PersonaLab. The rework introduces a **context sandwich**:

### Before BL-002 appears in detail (min 0:40)
- One slide: *"PersonaLab is a deliberately risky demo app. It generates AI personas that look and sound like real people. Therefore every feature needs consent, scope, and proof."*
- Visual: a simple consent-flow diagram (fictional persona created → warning shown → real-person blocked → audit log entry).
- No code, no repo tree. Just the *user-visible story*.

### During the work-contract section (min 1:10)
- Reuse slide 21, but add a subtitle: *"We do not build the whole app. We build one slice: BL-002 — the consent gate."*
- Define the four acceptance criteria in plain language:
  1. An unauthorized persona cannot be used.
  2. A clear warning is visible.
  3. Automated tests pass.
  4. A browser screenshot proves the right runtime.

### During the proof-bundle review (min 2:40)
- Show the BL-002 bundle folder (slide 33 / PDF `De proof bundle is de overdracht`) but walk it backwards:
  1. Start with the browser screenshot: *"This is the only thing a non-developer needs to understand."*
  2. Then show the test log: *"This is what the developer checks."*
  3. End with the manifest: *"This connects the two."*

### Optional handout
- A one-page *"BL-002 storyboard"* with 4 panels: fictional persona created → warning visible → real person blocked → audit log entry. This lets laypeople follow the demo without reading YAML.

---

## 7. Tooling recommendation: CLI, GUI, or hybrid

The trial produced a real split: Caner (developer) is comfortable with CLI; Lennert (less technical) prefers GUI for lower cognitive load. The target audience is mixed. The course should adopt a **hybrid track with a shared StateDD output**.

### Recommendation

**Use a hybrid path:**
- **Developers / power users:** CLI-first (OpenCode CLI, Claude Code, Kimi Code CLI). They get traceability, reproducible commands, and direct git integration.
- **Non-developers / managers:** GUI-first (GitHub Copilot Chat in VS Code, Kimi IDE, Cursor, OpenCode GUI when available). They get lower setup friction and visual feedback.
- **Both tracks produce the same artifacts:** the seven StateDD files, a numbered proof bundle, and a CTO-review outcome.

### Demo strategy to avoid doubling prep time

1. **Pre-record one full CLI run** of BL-002 setup → work contract → proof bundle → CTO review.
2. **Pre-record one full GUI run** of the *same* BL-002 slice, using a GUI tool that can edit files and run tests.
3. In the live session, show the **CLI run to developers** and the **GUI run to non-developers** in breakout-friendly format. Use split-screen or side-by-side screenshots highlighting identical prompts and identical output artifacts.
4. Keep the live demo to **one track per session**; advertise which track will be shown. Offer the alternative recording as homework.

### Risks and mitigations

| Risk | Mitigation |
|------|-----------|
| GUI tool version drift | Name the tested version on the prompt-copy website; schedule quarterly review. |
| GUI cannot run all StateDD scripts | GUI track skips `scripts/statedd_audit.py` execution; explains what the script checks and shows its output as a screenshot. |
| Attendees argue about "best" tool | Frame it as *interface choice*, not *tool religion*. Both tracks must pass the same closure gates. |
| Non-developers feel behind | Start the GUI demo 5 minutes earlier; reassure that the workflow, not the terminal, is the learning target. |

### Final recommendation for the course

**Default to hybrid presentation.** In a mixed room, spend **60% of tool time on GUI** to lower the floor for laypeople, and **40% on CLI** to show developers the power-user path. Always return to the same question: *"Does the artifact meet the closure gate?"* The interface is secondary.

---

## 8. Prompt-copy website integration

The trial asked for a small website with short links where attendees can copy-paste the prompts during/after the session. This is the deliverable of the `prompt-website` subagent, but the course-rework plan defines the requirements:

- **Scope:** Static site or Docsify page hosting canonical prompts from `prompts/`.
- **URL slugs:** `#setup`, `#workcontract`, `#execute`, `#review`, `#autonomy`, `#handoff`, `#onepager`.
- **UX:** One-click copy button, prompt title, "when to use it," and one example output/notes.
- **Sync:** The site must be generated from `prompts/` so it does not drift. A simple build script that copies/renames canonical templates into the site is preferred over hand-maintained pages.
- **Hosting:** Under the existing Docsify site (e.g., `/#/prompts/`) is simplest and keeps branding; a separate static site is acceptable if it complicates the main repo less.
- **Source location:** `g.Presentations/workspaces/ai-driven-dev-rework/prompt-website/` or `docs/prompts/` depending on the `prompt-website` subagent's recommendation.

The course deck should display the site's QR code/short URL at screenshot moments **G** and **H**.

---

## 9. Student project / community artifact note

**Caner is building a program based on the StateDD template.** This should be tracked as an emergent community artifact, not just anecdote.

- **Name/title:** TBD; working label "Caner StateDD implementation project."
- **What to capture:** Which language/stack, which StateDD files are automated, whether it generates work contracts or proof bundles, and any CLI/GUI choice made.
- **How to use it in the course:** If Caner consents, add a 2-minute "community example" slide after the autonomy budget. It demonstrates that the workflow is being productized by participants, not only by the trainers.
- **Action:** The synthesis subagent (or a follow-up implementation slice) should ask Caner for a one-paragraph description and a link/repo, then add it to the course handout and the prompt-copy website.

---

## 10. Cross-deliverable dependencies

This file is the first of four planned deliverables in `g.Presentations/workspaces/ai-driven-dev-rework/`:

1. **`course-rework.md`** ← this file.
2. **`prompt-screenshots.md`** — Detailed specs for the 8+ screenshot moments listed in §3. Expected from the prompt-screenshots subagent.
3. **`prompt-website.md`** — Design for the prompt-copy site. Expected from the prompt-website subagent.
4. **`cli-gui-recommendation.md`** — Standalone tooling comparison and hybrid-track proposal. Expected from the cli-gui-recommendation subagent.

The **synthesis** subagent will read the four files above and produce a single integrated action plan. This file intentionally does not contain that synthesis.

---

## 11. Blockers and open questions

| # | Blocker / question | Owner | Impact |
|---|-------------------|-------|--------|
| 1 | Need visual review of original `AI-Driven Development.pptx` to confirm slide layouts and speaker notes. | Subagent or human | Medium — affects where screenshots can fit without overcrowding. |
| 2 | Need Caner's consent and details to use his StateDD project as a community example. | Human / synthesis subagent | Low — can be omitted from first rework if unavailable. |
| 3 | Need decision on whether prompt-copy site lives inside Docsify (`docs/prompts/`) or as a standalone static site. | Human / prompt-website subagent | Medium — affects URL short links and build script. |
| 4 | Need tested GUI tool version for the hybrid demo. | Human or tool review | Medium — tool churn risk; must be reviewed quarterly. |
| 5 | Need confirmation whether the 3.5-hour workshop is Dutch or English; translation affects prompt wording and handout tone. | Human | High — this plan assumes English delivery but sources are Dutch/Flemish. |

---

## 12. Next recommended action

1. Review this rework plan against the original PPTX/PDF visuals.
2. Commission the three remaining subagent deliverables (`prompt-screenshots`, `prompt-website`, `cli-gui-recommendation`).
3. Run a synthesis subagent to merge the four files into a single build ticket.
4. Update `BACKLOG.md` / `NEXT_ACTIONS.md` with the resulting course-rework slice only after synthesis.
