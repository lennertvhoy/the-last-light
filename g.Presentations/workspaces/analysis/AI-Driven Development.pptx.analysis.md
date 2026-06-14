# Analysis: AI-Driven Development

## 1. Title & Source

- **Presentation title:** AI-Driven Development
- **Original file:** `/home/ff/Documents/Projects/the-last-light/g.Presentations/curated/AI-Driven Development.pptx`
- **Format:** PPTX
- **Slides:** 58
- **Extracted source text:** `/home/ff/Documents/Projects/the-last-light/g.Presentations/extracted/AI-Driven Development.pptx.md`

## 2. Language

Dutch (Flemish/Dutch)

## 3. Topic Summary

This presentation introduces "AI-Driven Development" as a controlled, workflow-centric alternative to ad-hoc "vibe coding." It argues that generating code is easy, but verifying, transferring, and reproducing it is hard. The core solution presented is State Driven Development (StateDD): a project operating system that makes the repository (not the chat) the source of truth, using explicit work contracts, proof bundles, CTO-agent review, and graduated human/agent autonomy. The PersonaLab demo app (specifically backlog slice BL-002, a consent gate) is used as a running example.

## 4. Target Audience

- Software developers and engineering leads using AI coding agents
- CTOs, tech leads, and product owners who need to delegate to AI without losing control
- Teams struggling with "fake progress," context decay, or unverifiable AI-generated output
- Professionals interested in practical governance of autonomous agent workflows

## 5. Key Takeaways

- Vibe coding is fast but creates hidden costs: verification and handoff remain difficult.
- The real problem is missing project truth; chat is volatile, while the repo should be the persistent source of truth.
- StateDD provides a 7-file project template (AGENTS.md, STATUS.md, PROJECT_STATE.yaml, PROJECT_DNA.yaml, NEXT_ACTIONS.md, BACKLOG.md, EVIDENCE_LOG.md) to keep state machine-readable and shared.
- Humans set goals, risks, and boundaries; the CTO-agent translates these into verifiable work contracts; the coding agent executes.
- Every backlog slice needs scope, out-of-scope items, explicit acceptance criteria, and a mandatory proof bundle.
- Closure gates prevent premature "done": no unrelated changes, tests pass, runtime identity proven, worktree clean, state updated.
- Subagents and MCP tools should be separated so no single agent builds, tests, proves, and approves its own work.
- Autonomy is earned through evidence, using a 6-level maturity ladder and an explicit autonomy budget.
- "No proof, no closure" is the central rule: a claim without evidence is a risk, not progress.
- Start small in behavior (one slice, one proof bundle) but complete in truth (all state files present from the start).

## 6. The Last Light Themes

- **Human agency:** The recurring message is "take back control" — the human stays supervisor, not bottleneck, deciding goals, risks, and review triggers.
- **Conscious delegation:** The framework explicitly asks "which tasks can I safely delegate?" and distinguishes human-in-the-loop, human-on-the-loop, and human-out-of-the-loop operations.
- **AI collaboration:** Presents a multi-agent setup (coding agent, test agent, evidence agent, documentation agent, review/CTO agent) working under human direction.
- **State Driven Development (StateDD):** The presentation is essentially an introduction to StateDD as a "project OS" for AI-driven development.
- **Outsourcing risk:** AI can generate code cheaply, but without proof, state, and review, the cost shifts to rework, context loss, and unverified claims.
- **Ethics/consent:** Uses PersonaLab's BL-002 Consent Gate as the concrete example, tying the workflow to consent, scope, and auditability.

## 7. Course Module Ideas

1. **StateDD Fundamentals for AI-Driven Teams** — Learn the 7-file StateDD template, the control loop, and how to initialize a project so AI agents share a single source of truth.
2. **Writing Verifiable Work Contracts for AI Agents** — Translate product goals into scoped backlog slices with acceptance criteria, out-of-scope rules, proof requirements, and closure gates.
3. **Designing Agent Autonomy and Escalation Policies** — Use the autonomy ladder and autonomy budget to decide which tasks agents can run unsupervised, when to escalate, and how to grow trust with evidence.

## 8. Slide Deck Ideas

1. **From Vibe Coding to StateDD: A 10-Slide Primer** — A condensed executive introduction covering the problem, the StateDD template, and the first steps to regaining control.
2. **The Proof Bundle: Evidence That AI Work Is Done** — Focused deck on what belongs in a proof bundle, how to number and review it, and why "no proof, no closure" matters.
3. **Subagents, MCP, and Separation of Powers** — Visual deck explaining why one agent should not build, test, and approve its own work, plus the nine MCP tool categories and permission boundaries.

## 9. Reuse Notes

- **Highly reusable:**
  - The 7-file StateDD file list and role-per-file explanations (Slides 14–16).
  - The bad-prompt vs. work-contract comparison (Slide 21).
  - The proof bundle structure and examples (Slides 33, 55, 58).
  - The closure gates and CTO-review checklist (Slides 23, 54, 56).
  - The autonomy ladder and budget template (Slides 41, 44, 57).
  - The half-day and full-day agendas (Slides 45–46) and workshop exercises (Slide 47).

- **Needs updating / context:**
  - The PersonaLab BL-002 Consent Gate example is concrete but assumes readers know the demo app. For reuse outside this project, either keep it as a worked example or swap in a more generic feature.
  - The appendix coding-agent prompt (Slide 53) and proof manifest YAML (Slide 55) should be checked against the current canonical StateDD template version in the repository.

- **Should be merged with other presentations:**
  - This deck pairs naturally with any presentation that introduces the PersonaLab demo app, consent/ethics in AI, or the StateDD template in more depth.
  - Consider merging with a "StateDD Deep Dive" or "Running Your First CTO-Agent Review" deck to form a multi-session curriculum.

## 10. Confidence & Gaps

- **Confidence:** High for structure, key claims, and reusable artifacts, because the extracted text is rich and explicit. The full slide-by-slide content is present, including appendix checklists and YAML examples.
- **Gaps / likely missed from text-only extraction:**
  - Speaker notes, delivery emphasis, and any live demo transitions are not captured.
  - Diagrams and visual flowcharts (e.g., the StateDD Control Loop on Slide 13, MCP Layer on Slide 28, Agent Chain with Escalation on Slide 37) are described but not rendered; their visual design and detail level are unknown.
  - Screenshots of the PersonaLab UI are referenced as browser proof but not included in the extracted text.
  - Branding, color scheme, typography, and slide layout are not visible from the text.
  - Audience interaction design (polls, Q&A prompts, handouts) may be present in the PPTX but not in the extraction.
