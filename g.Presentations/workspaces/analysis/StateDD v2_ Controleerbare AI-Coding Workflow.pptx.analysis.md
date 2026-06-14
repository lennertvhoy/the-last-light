# Analysis: StateDD v2: Controleerbare AI-Coding Workflow

## 1. Title & Source

- **Presentation title:** StateDD: Controleerbare AI-Coding Workflow
- **Original file:** `/home/ff/Documents/Projects/the-last-light/g.Presentations/curated/StateDD v2_ Controleerbare AI-Coding Workflow.pptx`
- **Format:** PPTX
- **Slides:** 44 (per extraction header)

## 2. Language

- Dutch

## 3. Topic Summary

This deck introduces StateDD (State Driven Development) as a disciplined, controllable workflow for AI coding agents. It contrasts ad-hoc "vibe coding" with a repo-centric approach where the codebase becomes the single source of truth, agents operate within scoped roles, and every claim is backed by a numbered proof bundle reviewed by a CTO or review agent. The presentation also maps out a half-day and full-day workshop format, plus an eight-step maturity ladder for teams adopting the practice.

## 4. Target Audience

- Software teams already experimenting with AI coding agents
- Tech leads, CTOs, and engineering managers who need accountability
- Workshop facilitators teaching agent governance
- Readers of *The Last Light* interested in concrete delegation workflows

## 5. Key Takeaways

1. **Vibe coding ends at "it seems to work"; StateDD ends at "it is proven."**
2. **The repo—not the chat history—is the source of truth.** State files (AGENTS.md, PROJECT_STATE.yaml, NEXT_ACTIONS.md, BACKLOG.md, EVIDENCE_LOG.md, STATUS.md) make project truth persistent and auditable.
3. **Every prompt should be a work contract:** scope, out-of-scope, acceptance criteria, verification steps, and handoff.
4. **No agent should judge its own work.** Coding, testing, evidence-gathering, documentation, and review should be separated across roles or subagents.
5. **MCP servers turn agents from guessers into tool users** by giving them real, verifiable filesystem, terminal, browser, and git output.
6. **Proof bundles replace chat claims.** A numbered folder with handoff, manifest, changed files, test results, browser proof, git status, and known limitations makes progress reviewable and transferable.
7. **Closure gates must be explicitly answered, not silently assumed.**
8. **Maturity ranges from Level 0 (loose prompts) to Level 7 (team-wide adoption with peer review).**
9. **Start small:** read AGENTS.md first, keep NEXT_ACTIONS.md under 10 items, demand runtime identity proof, and separate coding from review.
10. **The real enemy is not dumb AI; it is missing project truth.**

## 6. The Last Light Themes

- **Human agency and conscious delegation:** Humans (or human-like reviewers) define the operating contract, set scope boundaries, and hold the final review gate.
- **Outsourcing / AI collaboration:** The deck is explicitly about delegating coding work to AI agents without surrendering control.
- **State Driven Development:** Core framework of the presentation; directly maps to the project’s StateDD contract.
- **Staying relevant when AI can do more:** The human role shifts from writing every line to orchestrating truth, verifying proof, and governing the workflow.
- **Project truth vs. hallucination:** Strong thematic link to the book’s emphasis on not outsourcing judgment without verifiable evidence.

## 7. Course Module Ideas

1. **StateDD Fundamentals: From Vibe Coding to Proven Delivery**  
   A practical module that walks learners through the six core files, the difference between chat-truth and repo-truth, and how to write a StateDD-style prompt.

2. **Subagents, MCP & Tool Orchestration**  
   Covers role separation for coding, test, evidence, documentation, and review agents, plus which MCP tools to expose, restrict, or audit.

3. **Proof Bundles & CTO Review**  
   Teaches the proof-bundle folder structure, the manifest template, the 11-point CTO-review checklist, and the "no proof, no closure" rule.

## 8. Slide Deck Ideas

1. **StateDD in 15 Slides: A Leadership Pitch**  
   A condensed version for CTOs and tech leads that focuses on risks, the source-of-truth shift, and business value.

2. **The Six StateDD Files Explained**  
   One short deck per file (AGENTS.md, PROJECT_STATE.yaml, etc.) with examples, anti-patterns, and checklists.

3. **StateDD Maturity Ladder: Where Is Your Team?**  
   A self-assessment deck mapping levels 0–7 to team behaviors, blockers, and next concrete steps.

## 9. Reuse Notes

- **Highly reusable:** The full-day and half-day workshop agendas, the coding-agent prompt template, the proof-bundle folder layout, the proof-manifest YAML, and the CTO-review checklist are all ready to copy into training materials or repo templates.
- **Visuals likely missing from text:** Slides 8 ("De Scherpe Scheiding"), 24 (aannemer analogy), and the demo flow on slide 30 probably rely on diagrams or icons that should be captured from the PPTX.
- **Link to reuse:** The deck points to `github.com/lennertvhoy/StateDD_Template`; verify license and current version before integrating.
- **Merge opportunities:** Content overlaps with other StateDD material in the repo (e.g., `AGENTS.md`, `prompts/`, `docs/adr/`). Consider merging the prompt templates and proof-bundle specs into the canonical project files rather than maintaining parallel copies.
- **Update needs:** Workshop timings and MCP tool lists may need refresh as the MCP ecosystem evolves; runtime identity examples (localhost ports) should be generalized.

## 10. Confidence & Gaps

- **Confidence:** High for the textual content. The extracted file contains 44 complete slides with headings, bullet points, examples, and templates.
- **Likely missed:** Speaker notes, animations, presenter delivery, color emphasis, layout hierarchy, and any diagrams or screenshots embedded in the PPTX.
- **Sparse slides:** A few slides are mostly section headers (e.g., slide 4, 8, 10, 17, 23, 31, 38, 43, 44), so their full impact depends on accompanying visuals or narration.
- **Not verified:** Whether the GitHub template link is still current, and whether any speaker notes contain additional case studies or Q&A guidance.
