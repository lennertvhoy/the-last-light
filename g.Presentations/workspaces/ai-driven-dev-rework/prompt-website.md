# Prompt-Copy Website Design — AI-Driven Development Course Rework

**Subagent specialty:** `prompt-website`  
**Scope:** Design the small, copy-paste-friendly prompt website requested after the trial lesson.  
**Sources used:**
- `g.Presentations/extracted/AI-Driven Development.pptx.md` (slides 1–58, especially appendix slides 53–58)
- `g.Presentations/workspaces/analysis/AI-Driven Development.pptx.analysis.md`
- `g.Presentations/workspaces/courses/COURSE_MAP.md`
- `g.Presentations/workspaces/slides/SLIDE_MAP.md`
- Canonical StateDD prompts in `prompts/` at repo root

**Constraint:** This file is a deliverable only. No source files, state files, or project governance files were modified.

---

## 1. Purpose & Problem Statement

Trial-lesson feedback showed that participants were confused about **which prompt to use when** during setup and maintenance of a StateDD workflow. The fix is twofold:

1. Insert prompt-screenshot moments in the slide deck at the exact workflow steps.
2. Provide a lightweight website where attendees can copy-paste the canonical prompts during and after the session.

The website must work for a mixed audience: laypeople, developers, and everyone in between. It must therefore be tooling-agnostic (CLI vs GUI) and include short, stable URLs that the presenter can put on slides.

---

## 2. Site Structure

Three main views, all reachable from a single page:

| Section | Slug | Purpose |
|---------|------|---------|
| Home / How to use this site | `/#/ai-driven-dev/prompts` | One-line explanation + links to phases + printable one-pager. |
| Prompts by session phase | `/#/ai-driven-dev/prompts#<phase>` | Group prompts in the order they are used during the workshop. |
| Printable one-pager | `/#/ai-driven-dev/prompts#one-pager` | All prompts as plain text, printer-friendly, no copy buttons. |
| Community artifacts | `/#/ai-driven-dev/prompts#community` | Links to student/community projects, including Caner’s StateDD-based program. |

### Phase-based prompt index

The course follows the StateDD control loop from the deck (slides 10–13, 38, 45). Map prompts to these phases:

1. **Start / Setup** — initialize the agent and repo contract.
2. **Contract** — write a scoped, verifiable work contract.
3. **Build & Prove** — generate evidence and capture runtime identity.
4. **Review & Close** — run the CTO review, acceptance, and handoff.

Each phase is a collapsible/anchorable section on the same page.

---

## 3. Prompt Slugs & Canonical Mapping

Every prompt gets a short, stable slug that appears on slides and in the URL fragment. Each slug maps directly to one canonical file in `prompts/`.

| Slug | URL fragment | Canonical source | When to use it |
|------|--------------|------------------|----------------|
| `start` | `#start` | `prompts/CODING_AGENT_STARTUP_PROMPT.md` | First thing you paste into a coding agent when a session begins. |
| `bootstrap` | `#bootstrap` | `prompts/BOOTSTRAP_INTAKE_PROMPT.md` | When the repo is new or state is unclear; forces inspection before coding. |
| `contract` | `#contract` | `prompts/SLICE_CONTRACT_TEMPLATE.md` | Before any non-trivial implementation slice. |
| `evidence` | `#evidence` | `prompts/EVIDENCE_README_TEMPLATE.md` | When creating a new evidence folder / proof bundle. |
| `runtime` | `#runtime` | `prompts/RUNTIME_IDENTITY_CHECKLIST.md` | Before claiming a UI/user-facing change is done. |
| `review` | `#review` | `prompts/CTO_REVIEW_CHECKLIST.md` | When reviewing a completed slice / proof bundle. |
| `accept` | `#accept` | `prompts/ACCEPTANCE_FREEZE_TEMPLATE.md` | When accepting a milestone and freezing acceptance criteria. |
| `handoff` | `#handoff` | `prompts/FINAL_HANDOFF_TEMPLATE.md` | At the end of every implementation session, before returning to the CTO lane. |
| `routing` | `#routing` | `prompts/TOOL_MODEL_ROUTING_GUIDE.md` | When tool/model choice matters (advanced / CTO lane). |

**Stable short-link format for slides:**

```text
https://<site>/#/ai-driven-dev/prompts#<slug>
```

Example for a slide footer:

```text
Copy this prompt: thelastlight.example/#/ai-driven-dev/prompts#start
```

---

## 4. Per-Prompt Card UX

Each prompt is rendered as a card with the following elements:

1. **Prompt title** (e.g., "Coding Agent Startup Prompt").
2. **Slug badge** (e.g., `#start`) — shown so attendees can type it if the QR/link fails.
3. **When to use it** — one sentence tied to the course phase.
4. **CLI vs GUI note** — one or two lines explaining how to use the prompt in either interface.
5. **Prompt body** — the exact, copy-pasteable text (Markdown code block).
6. **One-click copy button** — copies the prompt body to the clipboard.
7. **Example output / notes** — a short, concrete example from the PersonaLab BL-002 case study where applicable.

### Example card: `#start`

```markdown
## #start — Coding Agent Startup Prompt

**When to use:** Paste this into the coding agent as the very first message of a new session.

**CLI vs GUI:** Same text works in OpenCode CLI, Kimi Code CLI/IDE, GitHub Copilot Chat, or Claude Code. In GUI tools, paste it into the first chat turn.

<button>Copy prompt</button>

```text
Read these files first in order:
1. AGENTS.md
2. STATUS.md
3. PROJECT_STATE.yaml
4. PROJECT_DNA.yaml
5. NEXT_ACTIONS.md

Then follow the repo contract exactly.

Your first job is to determine which of these two situations applies:

1. Fresh bootstrap or unclear repo state
2. Existing repo state with no current CTO prompt

If this is a fresh bootstrap or the repo is still unclear:
- do not start implementing yet
- inspect the repo
- ask only the minimum strategic questions needed to establish truthful bootstrap state
- update nothing until the project intent is clear enough to do so safely

If this is an existing repo state but no CTO prompt was provided:
- reconstruct the current verified state from the repo files
- identify what appears to be the highest-leverage next step
- do not begin non-trivial implementation yet
- first produce a CTO-ready handoff and a draft CTO prompt ...

[truncated for brevity in this design; full text pulled from prompts/CODING_AGENT_STARTUP_PROMPT.md]
```

**Example output / notes:**
- BL-002 Consent Gate session begins here. The agent reads the seven state files before touching any code.
- If the agent starts coding before reading the files, the prompt was not pasted first.
```

### Example card: `#contract`

```markdown
## #contract — Slice / Work Contract Template

**When to use:** Before the coding agent is allowed to implement anything.

**CLI vs GUI:** In GUI tools, create a new chat or project note and paste the filled-in contract there before the build chat starts.

<button>Copy prompt</button>

```text
Slice contract
- id: BL-002
- title: Consent Gate for PersonaLab
- type: feature
- user_value: Users cannot interact with an AI persona until they have explicitly granted consent.
- non_goals: voice cloning, face synthesis, data scraping, persistent memory
- acceptance_criteria:
  1. Block unauthorized personas before consent.
  2. Warning visible in the UI.
  3. All tests pass.
  4. Browser proof captured from running runtime.
```

**Example output / notes:**
- This replaces the bad prompt "Bouw een AI-kloon app" from slide 21.
- Out-of-scope items are as important as scope items.
```

---

## 5. Tech Stack Recommendation

### Recommended: Docsify page under the existing site

**Why this stack:**
- The project already runs on Docsify (`index.html`, `_sidebar.md`, `_coverpage.md`).
- No new build pipeline or hosting account is needed.
- Markdown source is human-readable and version-controlled with the rest of the repo.
- Hash fragments (`#start`, `#contract`) give stable short links.
- Easy to keep in sync with canonical prompts in `prompts/`.

### Alternative: Static HTML site

A plain static site (generated HTML + CSS + JS) is acceptable if:
- The course website must be detached from the book site.
- Offline distribution as a single `.zip` is required.

Downside: an extra build step and another artifact to keep in sync.

### Decision

Use **Docsify** for the main site and generate a **printable one-pager** as a secondary static HTML export for offline handouts.

---

## 6. File Paths

### Canonical prompts (existing, do not move)

```text
prompts/CODING_AGENT_STARTUP_PROMPT.md
prompts/BOOTSTRAP_INTAKE_PROMPT.md
prompts/SLICE_CONTRACT_TEMPLATE.md
prompts/EVIDENCE_README_TEMPLATE.md
prompts/RUNTIME_IDENTITY_CHECKLIST.md
prompts/CTO_REVIEW_CHECKLIST.md
prompts/ACCEPTANCE_FREEZE_TEMPLATE.md
prompts/FINAL_HANDOFF_TEMPLATE.md
prompts/TOOL_MODEL_ROUTING_GUIDE.md
```

### Website source generator (new)

```text
g.Presentations/workspaces/ai-driven-dev-rework/prompt-website/
├── generate.py                 # reads prompts/ and writes the Docsify page
├── README.md                   # how to run the generator
└── site-source/
    ├── README.md               # main page content, mostly generated
    ├── _sidebar.md             # optional: phase-based mini sidebar
    ├── style.css               # optional: card/copy-button styling
    └── copy.js                 # one-click copy button logic
```

### Generated Docsify page (new)

```text
docs/ai-driven-dev/prompts/
├── README.md                   # generated from canonical prompts
└── _sidebar.md                 # generated phase navigation
```

### Printable one-pager export (new)

```text
g.Presentations/workspaces/ai-driven-dev-rework/prompt-website/one-pager.html
```

This file is generated by `generate.py` and can be printed or distributed as a handout.

---

## 7. Sync Strategy with Canonical Prompts

Goal: the website must never drift from the canonical prompts in `prompts/`.

### Approach

1. **Single source of truth:** canonical prompts remain in `prompts/`.
2. **Generator script:** `prompt-website/generate.py` reads each canonical prompt and emits:
   - `docs/ai-driven-dev/prompts/README.md`
   - `docs/ai-driven-dev/prompts/_sidebar.md`
   - `prompt-website/one-pager.html`
3. **Metadata file:** `prompt-website/prompt-index.yaml` maps each slug to:
   - canonical source path
   - phase
   - title
   - when-to-use sentence
   - CLI/GUI note
   - example output / notes
4. **CI check:** add a lightweight check (or manual pre-flight) that runs `generate.py` and fails if the generated files differ from the committed versions.
5. **Update cadence:** regenerate whenever a prompt in `prompts/` changes, and before every course delivery.

### `prompt-index.yaml` example

```yaml
prompts:
  - slug: start
    source: prompts/CODING_AGENT_STARTUP_PROMPT.md
    phase: start
    title: Coding Agent Startup Prompt
    when: Paste into the coding agent at the start of every session.
    cli_gui_note: Same text in CLI or GUI chat; paste before any code request.
    example: BL-002 Consent Gate — agent reads all 7 StateDD files first.

  - slug: contract
    source: prompts/SLICE_CONTRACT_TEMPLATE.md
    phase: contract
    title: Slice / Work Contract Template
    when: Fill in before the coding agent is allowed to build anything.
    cli_gui_note: In GUI tools, paste the filled contract into a pinned note or first turn.
    example: BL-002 scope = consent selector + blocking + audit log.
```

---

## 8. Printable One-Pager

The one-pager is a single long page with:

- All prompts in phase order.
- Plain text only, no copy buttons, minimal styling.
- A short URL list at the top.
- QR code placeholders (generated by the site or added manually) for each phase anchor.

Use case: attendees with limited screen space or those who prefer paper notes.

---

## 9. CLI vs GUI Handling

The website is intentionally interface-agnostic. Each card includes a short **CLI vs GUI note** so the presenter does not need to maintain two separate prompt sets.

Example note pattern:

```text
CLI: paste into terminal-based agent (OpenCode CLI, Claude Code, Kimi Code CLI).
GUI: paste into the chat window of OpenCode GUI, Kimi Code IDE, Copilot Chat, Cursor, etc.
```

For the broader CLI vs GUI recommendation, see the dedicated `cli-gui-recommendation.md` deliverable.

---

## 10. Community Artifacts Section

Reserve a section at the bottom of the site for attendee projects.

### Initial entry: Caner’s StateDD-based program

```markdown
## Community artifacts

### Caner — StateDD-based program
Caner is building a program based on the StateDD template from the course.
- Status: student project / early community artifact.
- Maintainer: Caner.
- How to list: link to repo once available; until then, keep as a placeholder entry.
```

This signals that the prompt website is a living resource and encourages other attendees to submit their own projects.

---

## 11. Slide Integration

The prompt website is useless unless attendees know when to open it. Recommended slide moments (to be coordinated with the `prompt-screenshots` subagent):

| Slide / section | Moment | Slug to display |
|-----------------|--------|-----------------|
| Slide 10 — Van losse prompts naar een workflow | After introducing the 7-step workflow | `#start` |
| Slide 18 — Van CTO-beslissing naar Werkcontract | Before the work-contract exercise | `#contract` |
| Slide 33 — De proof bundle is de overdracht | When showing the proof-bundle folder | `#evidence` |
| Slide 35 — CTO Review: drie mogelijke uitkomsten | Before the review exercise | `#review` |
| Slide 38 — Demo: PersonaLab BL-002 in 7 stappen | During the live demo | `#start`, `#contract`, `#evidence`, `#review` |
| Slide 45 — Agenda: Halve dag (3.5 uur) | At the end, as a take-away | Full short-link list |
| Takeaways slide | Final QR code to the website home | `/ai-driven-dev/prompts` |

---

## 12. Acceptance Criteria for This Slice

- [ ] Slugs are stable and short enough for slide footers.
- [ ] Every prompt card maps to exactly one file in `prompts/`.
- [ ] One-click copy works on desktop and mobile.
- [ ] Printable one-pager is generated automatically.
- [ ] Generator script can be run in one command (`python3 generate.py`).
- [ ] Site is reachable from the existing Docsify navigation.
- [ ] CLI vs GUI note is present on every prompt card.
- [ ] Caner’s project is listed as a community artifact placeholder.

---

## 13. Next Recommended Actions

1. Review this design with the `course-rework` and `prompt-screenshots` subagents to ensure slug placement matches the new slide sequence.
2. Implement `prompt-website/generate.py` and the first generated `docs/ai-driven-dev/prompts/README.md`.
3. Add the website link to the AI-Driven Development slide deck takeaways slide.
4. After the `cli-gui-recommendation` deliverable exists, cross-link it from each CLI vs GUI note.
5. After Caner’s repo is available, replace the placeholder community entry with a real link.

---

## 14. Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| Website drifts from canonical prompts. | Generator script + CI/regeneration check. |
| Attendees still paste the wrong prompt. | Each card has a clear "When to use" line and phase grouping. |
| URLs are too long for slides. | Use hash fragments and a short domain; add QR codes for mobile. |
| Mixed CLI/GUI audience gets confused. | Add explicit CLI vs GUI notes; link to the CLI/GUI recommendation doc. |
| Caner’s project changes name or scope. | Community section uses a placeholder until a stable repo link exists. |

---

## 15. Handoff Note

This deliverable is design-only. No files in `prompts/`, `docs/`, or project root state files were modified. The actual website build is a separate implementation slice.
