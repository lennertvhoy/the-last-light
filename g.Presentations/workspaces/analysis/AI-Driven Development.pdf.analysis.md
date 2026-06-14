# Analysis: AI-Driven Development

## 1. Title & Source

- **Presentation title:** AI-Driven Development
- **Original file:** `/home/ff/Documents/Projects/the-last-light/g.Presentations/curated/AI-Driven Development.pdf`
- **Format:** PDF
- **Extracted text source:** `/home/ff/Documents/Projects/the-last-light/g.Presentations/extracted/AI-Driven Development.pdf.md`

## 2. Language

Dutch (Nederlands)

## 3. Topic Summary

This presentation argues that the real challenge in AI-driven development is not generating code, but verifying it and handing it off reliably. It introduces State Driven Development (StateDD) as a project operating system that replaces loose "vibe coding" with a structured workflow built around explicit state files, verifiable work contracts, subagents/MCP tools, and proof bundles. A running case study — PersonaLab backlog item BL-002, a consent gate — illustrates how a CTO-level reviewer turns a vague goal into a scoped, evidence-backed assignment.

## 4. Target Audience

Software developers, engineering team leads, CTOs, and technical product owners who are already experimenting with AI coding agents and need a governance framework to keep control, avoid context decay, and produce auditable outcomes.

## 5. Key Takeaways

- Code generation has become easy; verification and handoff remain hard.
- AI coding agents commonly suffer from **context decay**, **fake progress**, and **runtime confusion**.
- **StateDD** makes the repository — not the chat thread — the source of truth.
- The seven StateDD files (AGENTS.md, STATUS.md, PROJECT_STATE.yaml, PROJECT_DNA.yaml, NEXT_ACTIONS.md, BACKLOG.md, EVIDENCE_LOG.md) each have a distinct role and audience.
- The CTO/human translates product goals into a **verifiable work contract** with scope, out-of-scope boundaries, and acceptance criteria.
- Agents execute but do **not** self-approve; a separate CTO/reviewer decides ACCEPTED / CONDITIONAL / REJECTED.
- **Closure gates** demand proof: passing tests, browser proof, clean worktree, updated state files, and documented known limitations.
- **Subagents and MCP tools** connect agents to real outputs (git, terminal, browser, database) instead of guesses.
- **Proof bundles** are numbered, git-tracked evidence folders that create an auditable handoff.
- Teams can climb a **maturity ladder** from loose prompts (level 0) to a full team workflow (level 7), starting small in behavior but complete in truth.

## 6. The Last Light Themes

- **Human agency:** the human/CTO sets direction; the agent executes and does not judge its own work.
- **Conscious delegation:** deciding what to delegate, what to exclude, and how to verify.
- **AI collaboration:** framing AI as a teammate that needs governance, not as a replacement.
- **State Driven Development (StateDD):** the central methodology presented.
- **Project truth and memory:** combating context decay by persisting decisions in machine-readable state files.
- **Staying relevant when AI can code:** the human role shifts toward reviewer, architect, and governance owner.

## 7. Course Module Ideas

1. **"Van vibe coding naar StateDD"** — Recognize context decay, fake progress, and runtime confusion; introduce the StateDD project-OS and the seven state files.
2. **"Het CTO-werkcontract schrijven"** — Practice translating product goals into scoped assignments with explicit out-of-scope boundaries, acceptance criteria, and closure gates.
3. **"Subagents, MCP en proof bundles"** — Build verifiable AI workflows using tool-using agents, subagent swarms, and numbered evidence bundles that survive review.

## 8. Slide Deck Ideas

1. **"StateDD in 7 bestanden"** — Visual tour of each state file, its role, its users, and when to update it.
2. **"PersonaLab BL-002: van CTO-beslissing tot accepted bundle"** — Step-by-step walkthrough of the consent-gate slice from contract to closure.
3. **"De CTO-review checklist"** — Interactive training deck where participants decide whether a proof bundle is ACCEPTED, CONDITIONAL, or REJECTED.

## 9. Reuse Notes

- **Highly reusable:** the PersonaLab BL-002 consent-gate case study; the StateDD file-role table; the 11-point CTO review checklist; the coding-agent prompt template; the proof-bundle folder tree and manifest.
- **Ready-to-use handouts:** the appendix items (coding-agent prompt, proof manifest, closure gates, bundle tree) are almost template-grade.
- **Directly reusable:** the 3.5-hour workshop agenda and the "Jij bent de CTO-reviewer" exercise.
- **Needs updating if reused:** tool/MCP examples may need refreshing as the agent-tool ecosystem evolves; fictional screenshots and dates in the proof manifest should be replaced with real artifacts for live training.
- **Merge potential:** this deck pairs naturally with other StateDD or human-AI-collaboration presentations to form a multi-module curriculum.

## 10. Confidence & Gaps

- **Confidence:** high. The extracted text is detailed, well-structured, and preserves slide boundaries, section numbers, bullet lists, tables, and appendix templates.
- **Likely missed from the PDF:** exact slide layouts, diagrams (e.g., the StateDD control-loop diagram, maturity-ladder visual), typography and color emphasis, speaker delivery notes, animations, and any branding.
- **Limitations:** the text captures what was said on each slide but not visual hierarchy or pacing; some long vertical whitespace in the extraction suggests slides contained large graphics or section breaks that are not described.
