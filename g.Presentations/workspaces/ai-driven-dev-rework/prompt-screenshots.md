# Prompt-Screenshot Sequence — AI-Driven Development Course Rework

**Specialty:** `prompt-screenshots`  
**Scope:** Design the screenshot moments for the reworked CRS-001/004/005/006 AI-Driven Development workshop.  
**Sources:** `g.Presentations/extracted/AI-Driven Development.pptx.md`, `g.Presentations/extracted/AI-Driven Development.pdf.md`, `g.Presentations/workspaces/analysis/AI-Driven Development.*.analysis.md`, `prompts/*.md`.

---

## Design principles

1. **Show the prompt, not only the result.** Trial-lesson feedback showed participants were confused about *which* prompt to paste *when*. Each screenshot therefore displays the exact prompt text in its natural interface (chat window, terminal, IDE side panel, or YAML file).
2. **Anchor on canonical StateDD prompts.** Prompt text is taken from the canonical `prompts/` folder, not invented. Placeholders (`<project-name>`, `<slice-id>`) are used only where the prompt is generic.
3. **Two tracks, same truth.** For a mixed audience, screenshots are shown twice when the interface differs: once in a GUI/chat context (low cognitive load) and once in a CLI/terminal context. The prompt text stays identical so developers and laypeople see the same contract.
4. **No prior PersonaLab knowledge.** BL-002 is introduced as "a consent-gate feature in a demo app" and screenshots always include the slice contract so the example is self-contained.
5. **Minimum 8 screenshot moments.** This sequence specifies 10 moments to cover setup, execution, verification, review, and escalation.

---

## Screenshot moment 1 — Coding Agent Startup Prompt (setup)

| Field | Specification |
|-------|---------------|
| **Slide / section** | Slide 11 ("StateDD als Project-OS") immediately after the 7-file template is shown, and again at Slide 38 before the live BL-002 demo. |
| **What the screenshot shows** | A chat/IDE prompt input area (e.g., Kimi Code, OpenCode, Claude Code, or Copilot Chat). Above the prompt is a file tree showing the 7 StateDD files. Below the prompt is the agent’s first reply: "I have read AGENTS.md, STATUS.md, PROJECT_STATE.yaml, PROJECT_DNA.yaml, NEXT_ACTIONS.md. I will now inspect the repo before coding." |
| **Exact prompt text visible** | `Read these files first in order: 1. AGENTS.md 2. STATUS.md 3. PROJECT_STATE.yaml 4. PROJECT_DNA.yaml 5. NEXT_ACTIONS.md. Then follow the repo contract exactly. Your first job is to determine which of these two situations applies: 1. Fresh bootstrap or unclear repo state 2. Existing repo state with no current CTO prompt.` |
| **Why this prompt matters here** | Participants asked "Where do I start?" This screenshot makes the first action concrete: paste this prompt, and the agent reads the project truth before touching code. |
| **Type** | **Setup prompt** — used once per coding-agent session. |

---

## Screenshot moment 2 — Read Order in Action (setup / maintenance)

| Field | Specification |
|-------|---------------|
| **Slide / section** | Slide 15 ("Rol per file") or the live demo at Slide 38 step 3. |
| **What the screenshot shows** | A terminal or file-explorer split view. Left: the 7 StateDD files highlighted in read order. Right: the coding agent’s context panel listing the files it has already ingested, with `PROJECT_DNA.yaml` expanded to show `<project-name>` and stack. |
| **Exact prompt text visible** | `READ ORDER: 1. AGENTS.md → roles & rules 2. PROJECT_DNA.yaml → identity & stack 3. STATUS.md → current state 4. BACKLOG.md → priorities 5. NEXT_ACTIONS.md → immediate task 6. PROJECT_STATE.yaml → technical snapshot 7. EVIDENCE_LOG.md → previous proofs` |
| **Why this prompt matters here** | Demonstrates that the read order is not optional. It prevents context decay because the agent loads project truth before accepting a workcontract. |
| **Type** | **Setup/maintenance prompt** — repeated at the start of every slice. |

---

## Screenshot moment 3 — Slice Contract for BL-002 (setup)

| Field | Specification |
|-------|---------------|
| **Slide / section** | Slide 21 ("Slechte prompt vs Werkcontract BL-002") and Slide 38 step 2. |
| **What the screenshot shows** | A YAML editor or chat window showing the slice contract side-by-side with the bad prompt "Bouw een AI-kloon app". The bad prompt is crossed out; the contract is highlighted. |
| **Exact prompt text visible** | `slice: id: BL-002 title: Consent Gate type: feature owner: coding-agent user_value: Users can only create a persona after explicit consent, with an audit trail. non_goals: - Do not implement voice cloning. - Do not implement face synthesis. - Do not add persistent memory. - Do not scrape external data. acceptance_criteria: - Block unauthorized persona creation. - Warning visible before creation. - Tests pass. - Browser proof captured. - Worktree clean at handoff.` |
| **Why this prompt matters here** | The trial showed confusion about "what makes a prompt a workcontract." This screenshot makes the transformation explicit: vague wish → bounded contract with acceptance criteria. It also removes the need for prior PersonaLab knowledge by defining BL-002 fully on screen. |
| **Type** | **Setup prompt** — written by the CTO/human before the coding agent starts. |

---

## Screenshot moment 4 — CTO Session Prompt in the Strategy Chat (setup)

| Field | Specification |
|-------|---------------|
| **Slide / section** | Slide 18 ("Van CTO-beslissing naar Werkcontract") or the workshop intro at Slide 45. |
| **What the screenshot shows** | A separate browser tab or chat app labeled "CTO lane" (ChatGPT/Claude/Gemini). A human pastes the CTO session prompt. Below it, the chat replies with a short strategic summary and a draft coding-agent prompt. |
| **Exact prompt text visible** | `You are my CTO and product-architecture lead for this project. I am the CEO and human in the loop. You are not the coding agent. You do not have direct access to the repo or its state files unless I paste them here. Your role is to: reconstruct truth, judge quality, protect architecture, choose the next highest-leverage move, review coding-agent handoffs critically, write the next coding-agent prompt when appropriate.` |
| **Why this prompt matters here** | Participants were unsure how the "CTO" role differed from the coding agent. This screenshot shows the separate strategy chat and its scope: the CTO lane decides, the coding lane executes. |
| **Type** | **Setup prompt** — created once per project, reused every slice. |

---

## Screenshot moment 5 — Runtime Identity Checklist Before Browser Proof (verification)

| Field | Specification |
|-------|---------------|
| **Slide / section** | Slide 33 ("De proof bundle is de overdracht") and Slide 38 step 4/5. |
| **What the screenshot shows** | A terminal window next to a browser screenshot. The terminal lists the running process, working directory, git HEAD, and port. The browser shows the PersonaLab consent gate with the URL bar visible. A checklist overlay marks each runtime-identity item as checked. |
| **Exact prompt text visible** | `Required runtime identity proof: 1. repo path or source tree path serving the app 2. branch 3. HEAD commit 4. process or container serving the app 5. port, base URL, or endpoint under test 6. whether the artifact was rebuilt or restarted in this slice 7. whether duplicate dev servers, stale containers, or stale build artifacts were checked` |
| **Why this prompt matters here** | Prevents the "screenshot from the wrong runtime" failure mentioned in the source (Slide 3). Shows why browser proof alone is not enough. |
| **Type** | **Verification/maintenance prompt** — used before accepting any user-facing proof. |

---

## Screenshot moment 6 — Evidence README / Claim Ledger (execution)

| Field | Specification |
|-------|---------------|
| **Slide / section** | Slide 33 (proof bundle structure) and Slide 55 (Proof Manifest YAML). |
| **What the screenshot shows** | A file editor open at `evidence/E001_consent_gate/README.md`. The claim ledger is visible with three concrete claims mapped to artifacts. Below it, the verification log table is partially filled. |
| **Exact prompt text visible** | `## Claims - Claim: BL-002 blocks unauthorized persona creation. Evidence: evidence/E001_consent_gate/screenshots/002-real-person-blocked.png - Claim: Consent warning is visible before creation. Evidence: evidence/E001_consent_gate/screenshots/003-warning-visible.png - Claim: All tests pass. Evidence: evidence/E001_consent_gate/logs/test-run-YYYY-MM-DD.log` |
| **Why this prompt matters here** | Makes "no proof, no closure" tangible. Participants see that every claim must be paired with an artifact, not just stated in chat. |
| **Type** | **Execution/maintenance prompt** — filled by the evidence/coding agent during the slice. |

---

## Screenshot moment 7 — CTO Review Checklist with ACCEPTED/CONDITIONAL/REJECTED (review)

| Field | Specification |
|-------|---------------|
| **Slide / section** | Slide 35 ("CTO Review: drie mogelijke uitkomsten") and Slide 54 (CTO-Review Checklist appendix). |
| **What the screenshot shows** | A checklist rendered as a GitHub issue comment, a chat message, or a markdown preview. Each of the 11 items has a checkbox. The final decision dropdown shows ACCEPTED selected, with CONDITIONAL and REJECTED visible. |
| **Exact prompt text visible** | `=== CTO REVIEW — 11-PUNT CHECKLIST === 1. SCOPE-CHECK → Alleen geplande changes in diff? 2. DIFF-REVIEW → Geen ongerelateerde files gewijzigd? 3. TEST-RESULTATEN → Alle relevante tests geslaagd? 4. RUNTIME IDENTITY → Screenshots tonen juiste URL + versie? 5. PROOF BUNDLE → Alle 00-07 bestanden aanwezig? 6. STATE UPDATE → PROJECT_STATE en STATUS bijgewerkt? 7. BACKLOG SYNC → BL-ID correct gesloten of voortgezet? 8. WORKTREE CLEAN → Geen ongecommitte of ongetrackte changes? 9. KNOWN LIMITATIONS → Beperkingen expliciet gedocumenteerd? 10. SECURITY CHECK → Geen secrets gelekt, geen scope overreach? 11. NEXT_ACTIONS → Duidelijke vervolgstap geformuleerd? BESLISSING: ACCEPTED / CONDITIONAL / REJECTED` |
| **Why this prompt matters here** | Participants did not know when a slice was truly done. This screenshot gives the explicit review gate and the three possible outcomes. |
| **Type** | **Review/maintenance prompt** — run by the CTO agent or human after each slice. |

---

## Screenshot moment 8 — Final Handoff Template (maintenance)

| Field | Specification |
|-------|---------------|
| **Slide / section** | Slide 38 step 7 ("State update + next action") and Slide 49 ("Wat je morgen kan doen"). |
| **What the screenshot shows** | A chat message or markdown file showing the final handoff. The four-state closure block is filled in. Key fields (repo path, branch, head, port, next action) are highlighted. |
| **Exact prompt text visible** | `Final handoff for CTO lane Current verified truth - ... Slice contract - id: BL-002 - title: Consent Gate Four-state closure - Implemented: yes - Validated: yes - Closure-grade: yes - Accepted: pending Repo and runtime identity - repo path: /home/<user>/<project-name> - branch: main - head: <sha> - port/base URL: http://localhost:3000 - rebuilt in this slice: yes Direct verification - npm test -> pass Evidence refs - evidence/E001_consent_gate/README.md Next recommended action - Review browser proof and accept or reject BL-002.` |
| **Why this prompt matters here** | Shows how one slice ends and the next begins. Reinforces that the coding agent does not self-approve; it produces a handoff for the CTO lane. |
| **Type** | **Maintenance prompt** — used at the end of every implementation session. |

---

## Screenshot moment 9 — Closure Gates & Autonomy Budget (review / maturity)

| Field | Specification |
|-------|---------------|
| **Slide / section** | Slide 23 ("Closure Gates"), Slide 41 ("Autonomie-ladder"), and Slide 44 ("Autonomy Budget"). |
| **What the screenshot shows** | Two panes. Left: the closure gates checklist with all items checked. Right: the autonomy budget YAML showing `max backlog items: 3`, `max changed files per slice: 8`, and `human review required on: security, auth, data, architecture, failed tests`. |
| **Exact prompt text visible** | `Closure Gates: 1. Geen ongerelateerde changes in diff 2. Geen "klaar" zonder bewijs 3. Tests geslaagd en gedocumenteerd 4. Runtime identity bewezen 5. Worktree clean bij handoff 6. STATE.md bijgewerkt 7. PROJECT_STATE.yaml bijgewerkt 8. NEXT_ACTIONS.md logisch Autonomy Budget — PersonaLab BL-002 Max backlog items: 3 Max changed files per slice: 8 Allowed risk: low / medium Human review required on: security, auth, data, architecture, failed tests Stop conditions: dirty worktree, missing proof, scope drift, rejected CTO review` |
| **Why this prompt matters here** | Bridges proof bundles and autonomy. Participants see that autonomy is not granted freely; it is budgeted against verifiable gates. |
| **Type** | **Review/maintenance prompt** — used when deciding how many slices can run unsupervised. |

---

## Screenshot moment 10 — Human Override Rule (escalation)

| Field | Specification |
|-------|---------------|
| **Slide / section** | Slide 19 ("De mens is supervisor, niet bottleneck") and Slide 53/54 appendix when discussing exceptions. |
| **What the screenshot shows** | A chat window where the user says "Skip browser proof for this docs-only change." The agent replies: "Recording human override. Result will be marked as override-approved, not closure-grade." The evidence README shows `Human override used: yes` with the rule, requester, reason, and remaining risk. |
| **Exact prompt text visible** | `human_override: allowed: true protocol: | The human product owner may override workflow steps. The agent must not use "the workflow" to ignore explicit human direction. Override must be recorded in the evidence README and final handoff as Human override used: yes. acceptable_override_examples: - Skip browser proof for a docs-only or urgent internal change. - Use a temporary workaround when the user explicitly accepts the tradeoff.` |
| **Why this prompt matters here** | Prevents the workflow from feeling rigid. Shows laypeople that the human stays in charge and that overrides are documented, not hidden. |
| **Type** | **Escalation/maintenance prompt** — used whenever normal gates are skipped. |

---

## Insertion map for the 3.5-hour workshop

| Time block | Screenshot moments to show | Purpose |
|------------|----------------------------|---------|
| 09:00–09:20 Opening & problem | 1 (briefly, as a promise) | Show that there is a concrete starting prompt. |
| 09:20–10:00 StateDD as Project-OS | 1, 2 | How to start a coding-agent session; how the read order prevents context decay. |
| 10:20–11:00 CTO decision → workcontract | 3, 4 | From vague wish to bounded slice contract; the CTO lane vs coding lane. |
| 11:00–11:30 Subagents & MCP | 2 (MCP file read), 5 | Tools verify instead of guessing; runtime identity before browser proof. |
| 11:30–12:00 Proof bundles & autonomy | 6, 7, 9 | Claim ledger, CTO review, closure gates, autonomy budget. |
| 12:00–12:20 Autonomy ladder & budget | 8, 9, 10 | Handoff, autonomy budget, and documented human override. |
| 12:20–12:30 Takeaways | 1 (reprise) | Participants leave with the first prompt they can paste tomorrow. |

---

## Production notes

- **Interfaces to capture:** For the mixed-audience goal, produce each screenshot in two variants where feasible:
  - **GUI variant:** ChatGPT/Claude web UI, Kimi Code IDE panel, OpenCode GUI, or GitHub Copilot Chat.
  - **CLI variant:** Terminal with the same prompt text, for developers who prefer the command line.
  The prompt body must be pixel-identical so the two variants teach the same contract.
- **Placeholder policy:** Use `<project-name>`, `<slice-id>`, `<sha>`, `<user>`, and `<port>` consistently. Do not show real repo paths or secrets.
- **Sync with canonical prompts:** Before final capture, diff the screenshot text against `prompts/CODING_AGENT_STARTUP_PROMPT.md`, `prompts/CTO_SESSION_PROMPT.md`, `prompts/SLICE_CONTRACT_TEMPLATE.md`, `prompts/RUNTIME_IDENTITY_CHECKLIST.md`, `prompts/EVIDENCE_README_TEMPLATE.md`, `prompts/CTO_REVIEW_CHECKLIST.md`, and `prompts/FINAL_HANDOFF_TEMPLATE.md`.
- **No new StateDD rules invented:** All prompt text is taken from existing canonical templates or directly quoted from the source deck.

---

## Blockers / open questions

- The original deck is in Dutch/Flemish. Screenshots for an English delivery must be translated, but the canonical `prompts/` are already in English. A decision is needed on whether the course delivery language is Dutch or English.
- Live demo screenshots of PersonaLab BL-002 require a running instance of the demo app to capture real browser proof. If the demo is not runnable during production, staged screenshots with clear "fictional UI" labels are acceptable.
- Tool-specific visuals (OpenCode, Kimi Code, Claude Code, Copilot) will age. Consider generic chat/IDE chrome with tool name blurred or replaced by a placeholder.
