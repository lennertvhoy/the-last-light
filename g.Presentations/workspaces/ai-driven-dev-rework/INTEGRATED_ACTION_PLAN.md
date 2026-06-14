# Integrated Action Plan — AI-Driven Development Course Rework

**Scope:** Merge the four sub-deliverables for the CRS-001/004/005/006 rework into one build-ready plan.  
**Source files:**
- `course-rework.md`
- `prompt-screenshots.md`
- `prompt-website.md`
- `cli-gui-recommendation.md`

---

## 1. Executive summary

The trial lesson exposed five hard friction points:

1. **Which prompt when?** Setup, execution, and review prompts were hidden in appendix slides shown *after* the demo.
2. **No copy-paste source.** Attendees saw static screenshots but could not grab the exact wording during or after the session.
3. **CLI-only framing alienated non-developers.** One participant (Caner) was fine with CLI; another (Lennert) found GUI tools lower cognitive load.
4. **PersonaLab BL-002 needed context.** Attendees did not know the demo app, so the consent gate and folder tree felt abstract.
5. **MCP section was tool-heavy, not decision-heavy.** Listing nine MCP types did not map to the five verification verbs attendees actually need.

The rework therefore:

- Re-sequences the 3.5-hour workshop so technical foundations (StateDD files, work contracts, proof bundles) come before the break and application exercises (CTO review, autonomy budget) come after.
- Inserts **ten short screenshot moments** at the exact workflow handoffs, each tied to a canonical prompt in `prompts/`.
- Adds a **prompt-copy website** with stable hash-fragment slugs so attendees copy the real text, not a slide approximation.
- Adopts a **hybrid CLI/GUI track** with a shared StateDD output: developers see CLI, non-developers see GUI, both produce the same artifacts.
- Treats **Caner’s StateDD-based program** as an emergent community artifact, listed on the prompt site once details are available.

The language question (Dutch source deck vs. English delivery) and the live-vs-staged PersonaLab demo remain unresolved and are tracked as blockers in §7.

---

## 2. Reworked workshop outline

**Total duration:** 210 minutes (3.5 hours), including a 20-minute break.

| Time | Phase | What happens | Screenshot / prompt moment | Prompt slug |
|------|-------|--------------|----------------------------|-------------|
| 0:00–0:20 | **Opening: the two-hour "done"** | Hook slides 2–4. Poll on recent AI "done" surprises. Set mixed-audience ground rules; preview CLI/GUI split. | None. | — |
| 0:20–0:40 | **The real problem: missing project truth** | Context decay, fake progress, runtime confusion. Introduce repo-as-truth. | **A** — Bootstrap intake prompt. | `#bootstrap` |
| 0:40–0:55 | **Meet PersonaLab BL-002** | 3-minute demo-app context: a sandbox for AI personas where consent must be proven. Show consent-flow diagram. | Context sandwich (no prompt). | — |
| 0:55–1:10 | **StateDD as Project-OS** | 7-file template walkthrough. Emphasize: complete in truth, small in behavior. | **B / 1 / 2** — Coding-agent startup prompt + read order. | `#start` |
| 1:10–1:35 | **From CTO decision to work contract** | Goal → scope → out-of-scope → acceptance criteria. Attendees rewrite one bad prompt into a work contract. | **C / 3** — Filled `SLICE_CONTRACT_TEMPLATE.md` for BL-002. **4** — CTO session prompt. | `#contract` |
| 1:35–1:55 | **Break** | | | — |
| 1:55–2:20 | **Proof bundles: no proof, no closure** | What belongs in a bundle, numbering, review outcomes. Keep depth light; focus on auditable handoff. | **D / 6** — Coding-agent execution prompt + evidence README for BL-002. **5** — Runtime identity checklist. | `#evidence`, `#runtime` |
| 2:20–2:40 | **Subagents, MCP, and separation of powers** | Two-role story (doer + checker). Condensed tool list mapped to five verification verbs. | Optional live GUI/CLI demo. | — |
| 2:40–3:00 | **CTO review in practice** | Interactive review of a pre-built BL-002 proof bundle. Participants vote ACCEPTED / CONDITIONAL / REJECTED. | **E / 7** — `CTO_REVIEW_CHECKLIST.md` as prompt. | `#review` |
| 3:00–3:20 | **Autonomy ladder and budget** | Ladder as roadmap. Attendees draft an autonomy budget for their own team/slice. | **F / 9** — Closure gates + autonomy budget. **8** — Final handoff template. **10** — Human override rule. | `#handoff` |
| 3:20–3:30 | **Tomorrow: one line, one prompt, one site** | Closing. | **G** — "Your first prompt tomorrow." **H** — Prompt-copy website QR/short URL. | `#bootstrap` or `#start`, home page |

**Pedagogical rationale:** Foundations are front-loaded before the break; the second half is application and decision-making. Non-developers get context before tools appear, and the autonomy ladder now functions as a visible roadmap rather than a late appendix.

---

## 3. Screenshot/prompt list

This table consolidates the screenshot moments from `course-rework.md` (letters A–H) and `prompt-screenshots.md` (numbers 1–10). Gaps in prompt-website slug coverage are flagged explicitly.

| ID | Workshop timing | Screenshot content | Prompt file reference | Prompt slug | GUI/CLI variant |
|----|-----------------|--------------------|------------------------|-------------|-----------------|
| A | 0:20–0:40 | Bootstrap intake prompt shown in chat/IDE. | `prompts/BOOTSTRAP_INTAKE_PROMPT.md` | `#bootstrap` | Both |
| B | 0:55–1:10 | Coding-agent startup prompt with 7-file read order. | `prompts/CODING_AGENT_STARTUP_PROMPT.md` | `#start` | Both |
| 1 | 0:55–1:10 | Coding agent startup prompt in chat/IDE; agent reply confirms files read. | `prompts/CODING_AGENT_STARTUP_PROMPT.md` | `#start` | Both |
| 2 | 0:55–1:10 | Split view: 7 StateDD files highlighted in read order, agent context panel showing ingestion. | `prompts/CODING_AGENT_STARTUP_PROMPT.md` (read-order block) | `#start` | Both |
| C | 1:10–1:35 | Filled slice contract for BL-002 side-by-side with crossed-out bad prompt. | `prompts/SLICE_CONTRACT_TEMPLATE.md` | `#contract` | Both |
| 3 | 1:10–1:35 | YAML editor or chat showing BL-002 slice contract. | `prompts/SLICE_CONTRACT_TEMPLATE.md` | `#contract` | Both |
| 4 | 1:10–1:35 | Separate "CTO lane" chat with CTO session prompt pasted. | `prompts/CTO_SESSION_PROMPT.md` | **No slug defined** — add to site index. | Both |
| D | 1:55–2:20 | Coding-agent execution prompt for BL-002, with placeholders and proof-bundle rule. | Derived from `prompts/CODING_AGENT_STARTUP_PROMPT.md` + `#contract`; no single canonical file. | `#start` + `#contract` combined | Both |
| 5 | 1:55–2:20 | Terminal + browser screenshot with runtime-identity checklist overlay. | `prompts/RUNTIME_IDENTITY_CHECKLIST.md` | `#runtime` | Both |
| 6 | 1:55–2:20 | Evidence README claim ledger for BL-002. | `prompts/EVIDENCE_README_TEMPLATE.md` | `#evidence` | Both |
| E | 2:40–3:00 | CTO review checklist rendered as GitHub issue comment or chat; ACCEPTED selected. | `prompts/CTO_REVIEW_CHECKLIST.md` | `#review` | Both |
| 7 | 2:40–3:00 | CTO review checklist with 11 items and ACCEPTED/CONDITIONAL/REJECTED decision. | `prompts/CTO_REVIEW_CHECKLIST.md` | `#review` | Both |
| F | 3:00–3:20 | Closure gates + autonomy budget YAML for PersonaLab BL-002. | `prompts/FINAL_HANDOFF_TEMPLATE.md` + autonomy fields | `#handoff` | Both |
| 8 | 3:00–3:20 | Final handoff message with four-state closure and runtime identity block. | `prompts/FINAL_HANDOFF_TEMPLATE.md` | `#handoff` | Both |
| 9 | 3:00–3:20 | Two-pane: closure gates checked + autonomy budget YAML. | `prompts/FINAL_HANDOFF_TEMPLATE.md` + autonomy fields | `#handoff` | Both |
| 10 | 3:00–3:20 | Human override rule: user says "skip browser proof," agent records override in evidence README. | `AGENTS.md` (Human Override Rule) | **No slug defined** — add to site index or link to `AGENTS.md`. | Both |
| G | 3:20–3:30 | "Your first prompt tomorrow" starter sentence. | `prompts/BOOTSTRAP_INTAKE_PROMPT.md` or `prompts/CODING_AGENT_STARTUP_PROMPT.md` | `#bootstrap` or `#start` | Both |
| H | 3:20–3:30 | Browser showing the prompt-copy website home page with QR/short URL. | Generated site home | Home (`/#/ai-driven-dev/prompts`) | N/A (web only) |

**Required slug additions to the prompt-copy website:**
- `cto` or `strategy` → `prompts/CTO_SESSION_PROMPT.md`
- `override` → Human Override Rule in `AGENTS.md` (or create a short canonical prompt file)

---

## 4. Prompt-copy website spec

### Tech stack

- **Primary:** Docsify page under the existing Docsify site.
- **Secondary export:** Static HTML one-pager for offline handouts.
- **Rationale:** The project already uses Docsify; no new hosting pipeline is needed; markdown source stays version-controlled.

### URL structure

| Page / section | URL fragment | Content |
|----------------|--------------|---------|
| Home / how to use | `/#/ai-driven-dev/prompts` | One-line explanation + phase links + printable one-pager link. |
| Start / setup | `/#/ai-driven-dev/prompts#start` | Coding-agent startup prompt. |
| Bootstrap | `/#/ai-driven-dev/prompts#bootstrap` | Bootstrap intake prompt. |
| Contract | `/#/ai-driven-dev/prompts#contract` | Slice / work contract template. |
| Evidence | `/#/ai-driven-dev/prompts#evidence` | Evidence README template. |
| Runtime | `/#/ai-driven-dev/prompts#runtime` | Runtime identity checklist. |
| Review | `/#/ai-driven-dev/prompts#review` | CTO review checklist. |
| Accept | `/#/ai-driven-dev/prompts#accept` | Acceptance freeze template. |
| Handoff | `/#/ai-driven-dev/prompts#handoff` | Final handoff template. |
| Routing | `/#/ai-driven-dev/prompts#routing` | Tool/model routing guide. |
| Community | `/#/ai-driven-dev/prompts#community` | Caner’s StateDD project placeholder + submission note. |
| One-pager | `/#/ai-driven-dev/prompts#one-pager` | All prompts as plain text, printer-friendly. |

**Short-link format for slide footers:**
```text
https://<site>/#/ai-driven-dev/prompts#<slug>
```

### File paths

**Canonical prompts (existing, read-only for this slice):**
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
prompts/CTO_SESSION_PROMPT.md
```

**Website generator (new):**
```text
g.Presentations/workspaces/ai-driven-dev-rework/prompt-website/
├── generate.py                 # reads prompts/ and writes site files
├── prompt-index.yaml           # slug → source + metadata
├── README.md                   # how to run the generator
├── site-source/
│   ├── README.md               # generated main page
│   ├── _sidebar.md             # generated phase navigation
│   ├── style.css               # card/copy-button styling
│   └── copy.js                 # one-click copy logic
└── one-pager.html              # generated printable export
```

**Generated Docsify page (new):**
```text
docs/ai-driven-dev/prompts/
├── README.md
└── _sidebar.md
```

### Per-prompt card UX

Each card contains:
1. Prompt title.
2. Slug badge (e.g., `#start`).
3. "When to use it" sentence tied to a workshop phase.
4. CLI vs GUI note.
5. Exact copy-pasteable prompt body.
6. One-click copy button.
7. BL-002 example output / notes where applicable.

### Sync strategy

1. **Single source of truth:** `prompts/` remains canonical.
2. **Generator:** `generate.py` reads `prompt-index.yaml` and each prompt file, then writes:
   - `docs/ai-driven-dev/prompts/README.md`
   - `docs/ai-driven-dev/prompts/_sidebar.md`
   - `prompt-website/one-pager.html`
3. **CI/regeneration check:** Run `generate.py` before each delivery; fail if generated files differ from committed versions.
4. **Update cadence:** Regenerate whenever any file in `prompts/` changes.

---

## 5. CLI/GUI delivery strategy

### Final recommendation

**Use a hybrid track, not a single default.**

- **Developers / power users:** CLI-first (OpenCode CLI, Kimi Code CLI, Claude Code). They get traceability, reproducible commands, and direct git integration.
- **Non-developers / managers:** GUI-first (GitHub Copilot Chat in VS Code, Kimi IDE, Cursor, OpenCode GUI when available). They get lower setup friction and visual feedback.
- **Mandatory equalizer:** Both tracks produce the same artifacts: the seven StateDD files, a numbered proof bundle, and a CTO-review outcome.

### Mixed-room time split

- Spend **60% of tool-demonstration time on GUI** to lower the floor for laypeople.
- Spend **40% on CLI** to show developers the power-user path.
- Always return to the same question: *"Does the artifact meet the closure gate?"*

### Demo strategy to avoid doubling prep time

1. Prepare **one canonical PersonaLab BL-002 repo**.
2. Pre-record **one full CLI run** and **one full GUI run** of the same BL-002 slice.
3. In the live session, run **one track live** based on the dominant audience; show the other via paired screenshots or a short pre-recorded clip.
4. Pair screenshots side-by-side on slides to prove the prompts and artifacts are identical across interfaces.
5. Offer the alternative recording as homework.

### Risks and mitigations

| Risk | Mitigation |
|------|-----------|
| GUI tool version drift | Name the tested version on the prompt-copy website; schedule quarterly review. |
| GUI cannot run all StateDD scripts | GUI track skips `scripts/statedd_audit.py` execution; explains what it checks and shows its output as a screenshot. |
| Attendees argue about "best" tool | Frame it as *interface choice*, not *tool religion*. Both tracks pass the same closure gates. |
| Non-developers feel behind | Start the GUI demo 5 minutes earlier; reassure that the workflow, not the terminal, is the learning target. |
| Instructor cannot demo both live | Pre-record the second interface; rely on paired screenshots. |

---

## 6. Implementation checklist

| # | Task | Owner | Acceptance criteria |
|---|------|-------|---------------------|
| 1 | Decide course delivery language (Dutch vs. English). | User / stakeholder | Documented in `DESIGN_DECISIONS.md` and confirmed before prompt translation begins. |
| 2 | Decide whether PersonaLab BL-002 is shown live or via staged screenshots. | User / Caner | Decision recorded; if staged, screenshots get clear "fictional UI" labels. |
| 3 | Confirm which exact CLI/GUI tools the instructor can demo live. | User / instructor | Tool names and tested versions recorded in `prompt-index.yaml`. |
| 4 | Add missing prompt slugs to `prompt-website/prompt-index.yaml` (`cto`/`strategy`, `override`). | Coding agent | All screenshot moments map to a stable slug. |
| 5 | Build `prompt-website/generate.py` and first generated `docs/ai-driven-dev/prompts/README.md`. | Coding agent | Runs with `python3 generate.py`; generated files match committed versions; one-click copy works. |
| 6 | Add generated Docsify page to existing site navigation (`_sidebar.md`). | Coding agent | `/#/ai-driven-dev/prompts` reachable from book site. |
| 7 | Generate printable one-pager HTML and verify print layout. | Coding agent | Plain text, phase order, short URLs visible, prints cleanly. |
| 8 | Produce the ten screenshot moments in both GUI and CLI variants. | Coding agent / Caner | Text is pixel-identical across variants; placeholders used consistently; each image referenced in the slide build. |
| 9 | Build reworked slide deck with inserted screenshot moments and short-link QR codes. | Coding agent / user | Slide sequence matches §2; screenshot moments fit without overcrowding. |
| 10 | Record or prepare live PersonaLab BL-002 demo material (CLI + GUI). | Caner / coding agent | One canonical repo; both runs produce identical StateDD artifacts; video/screenshots ready. |
| 11 | Obtain Caner’s consent and one-paragraph description for community artifact listing. | User | Placeholder on prompt site updated with real text and optional repo link. |
| 12 | Add CI/regeneration check for prompt-copy website. | Coding agent | `generate.py` diff check runs in repo workflow. |
| 13 | Run a second trial lesson with at least one non-developer and collect feedback. | User / instructor | Feedback logged; open questions in §7 closed or updated. |
| 14 | Update `BACKLOG.md` / `NEXT_ACTIONS.md` with the resulting course-rework slice. | User / coding agent | State files reflect closure-grade completion only after items 1–13 are verified. |

---

## 7. Open questions / blockers

| # | Question / blocker | Why it blocks building | Owner | Suggested resolution |
|---|-------------------|------------------------|-------|----------------------|
| 1 | **Course language:** Dutch or English? | Affects prompt wording, handout tone, screenshot text, and whether the Dutch source deck must be translated. | Human / stakeholder | Confirm before any prompt or screenshot production begins. |
| 2 | **PersonaLab BL-002 demo:** live app vs. staged screenshots? | Live demo needs a runnable instance; staged needs "fictional UI" labels and may reduce credibility. | Caner / human | Decide by task #2 in §6. |
| 3 | **Exact live tools:** Which CLI/GUI tools can the instructor actually demo? | Determines screenshot chrome, prompt notes, and hybrid-track feasibility. | Instructor / human | Lock to tested versions (e.g., Kimi Code CLI + IDE plugin, or OpenCode CLI + GUI). |
| 4 | **Prompt site hosting path:** Docsify sub-page vs. standalone static site? | Affects URL short links, build pipeline, and whether the site is coupled to the book. | Human / coding agent | Default to Docsify sub-page unless a detached course site is required. |
| 5 | **Missing prompt slugs:** `CTO_SESSION_PROMPT.md` and Human Override Rule have no website slug. | Two screenshot moments (4 and 10) cannot be linked from slides until slugs exist. | Coding agent | Add `cto`/`strategy` and `override` slugs to `prompt-index.yaml`. |
| 6 | **Caner’s StateDD project details and consent to list.** | Community artifact section is a placeholder until real text/link exists. | Caner / human | Request one-paragraph description and optional repo link. |
| 7 | **Visual review of original PPTX layouts and speaker notes.** | Affects where screenshots fit without overcrowding and whether slide renumbering is needed. | Human / subagent | Review original deck against §2 before screenshot production. |

---

## 8. Handoff note

This plan is synthesis-only. No source deliverables, canonical prompts, or project state files were modified. The next step is to resolve the open questions in §7, then execute the checklist in §6 in order.
