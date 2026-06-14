# Course Map — The Last Light Presentation Assets

This map synthesizes the eight per-presentation analyses in `g.Presentations/workspaces/analysis/` into a coherent course architecture for *The Last Light: How to Stay Human When Everything Can Be Outsourced*. The proposed courses are derived directly from the course-module ideas listed in each analysis. Where analyses overlap, modules have been consolidated to avoid duplication; where they conflict, the conflict is noted honestly.

| Course ID | Title | Source Presentations | Target Audience | Description | Priority | Dependencies |
|-----------|-------|----------------------|-----------------|-------------|----------|--------------|
| CRS-001 | StateDD Fundamentals — From Vibe Coding to Repo Truth | `StateDD_ Een Project-OS voor AI Coding Agents.pptx`; `StateDD v2_ Controleerbare AI-Coding Workflow.pptx`; `AI-Driven Development.pptx`; `AI-Driven Development.pdf` | Software developers, tech leads, CTOs, engineering managers | Introduces State Driven Development (StateDD) as a lightweight project operating system: repo-centric truth, the seven state files, bootstrap vs. operating mode, and the shift from chat-as-truth to repo-as-truth. Draws on all three StateDD analyses. | P0 | None |
| CRS-002 | AI for the ICT Helpdesk — From Prompt to Safe Solution | `AI-20251103_lenny_remix.pptx`; `AI-20251103_lenny_remix.pdf` | ICT helpdesk staff, system administrators, IT support professionals | Hands-on module covering prompt preparation, the 4C method, evaluating AI-generated scripts/commands, and responsible documentation for helpdesk tasks. | P0 | None |
| CRS-003 | Human-AI Collaboration and Cognitive Resilience | `AI-20251103_lenny_remix.pptx/pdf`; `Digitale dubbelgangers_ wanneer AI zelf initiatief neemt.pptx`; `Moltbook_MiddagSessie.pptx` | Knowledge workers, managers, team leads, trainers | Explores the "nivelleringseffect" (leveling effect), cognitive atrophy, the jagged boundary, and how to design workflows where AI augments rather than replaces human judgment. | P0 | None |
| CRS-004 | Writing Verifiable Work Contracts for AI Agents | `AI-Driven Development.pptx/pdf`; `StateDD v2_ Controleerbare AI-Coding Workflow.pptx` | CTOs, product owners, tech leads, reviewers | Teaches how to translate product goals into scoped backlog slices with explicit out-of-scope boundaries, acceptance criteria, and closure gates. | P1 | CRS-001 recommended |
| CRS-005 | Proof Bundles, Evidence, and CTO Review | `AI-Driven Development.pptx/pdf`; `StateDD_ Een Project-OS voor AI Coding Agents.pptx`; `StateDD v2_ Controleerbare AI-Coding Workflow.pptx` | Tech leads, reviewers, quality engineers, audit stakeholders | Covers proof-bundle structure, manifest templates, runtime identity proof, the CTO-review checklist, and the "no proof, no closure" rule. | P1 | CRS-001 recommended; CRS-004 helpful |
| CRS-006 | Subagents, MCP, and Tool Orchestration | `AI-Driven Development.pptx/pdf`; `StateDD v2_ Controleerbare AI-Coding Workflow.pptx` | Software engineers, agent builders, platform engineers | Focuses on role separation (coding/test/evidence/review agents), MCP tools that turn agents from guessers into tool users, and permission boundaries. | P1 | CRS-001 recommended |
| CRS-007 | Governance, Compliance, and Risk Management for Generative AI | `AI-20251103_lenny_remix.pptx/pdf`; `Digitale dubbelgangers_ wanneer AI zelf initiatief neemt.pptx`; `Moltbook_MiddagSessie.pptx` | Compliance officers, managers, IT teams, product designers | Covers privacy, security, bias, human-in-the-loop / human-on-the-loop, the EU AI Act, consent, disclosure, liability, drift, and organizational policy. | P1 | None |
| CRS-008 | Proactive Social Agents and Digital Doubles | `Digitale dubbelgangers_ wanneer AI zelf initiatief neemt.pptx` | AI practitioners, product managers, designers | From chatbot to proactive agent: the observe-filter-score-send attention loop, consent-first design, social presence, and the framing "real enough for what purpose?" | P2 | CRS-003 and CRS-007 recommended |
| CRS-009 | Agents Demystified — From Hype to Orchestrated Loop | `Moltbook_MiddagSessie.pptx` | IT professionals, trainers, educators, technical decision makers | Uses Moltbook as a case study to teach the anatomy of an AI agent, autonomy vs. hype, the four gaps (identity, memory, governance, economics), and context-reload costs. | P2 | None |
| CRS-010 | Building Your First Teaching Agent with Copilot | `Moltbook_MiddagSessie.pptx` | Trainers, educators, IT professionals | Hands-on workshop based on the Copilot demo: build an agent that generates a lesson page, quiz, and lab validated against external sources. | P2 | CRS-009 recommended |

## Cross-Cutting Themes

The following *Last Light* themes appear across multiple presentations and should be treated as threads woven through the curriculum rather than isolated modules.

### Human Agency and Staying Human
- Primary sources: all eight analyses.
- Key concepts: keep humans in or on the loop, "human expertise heruitvinden," humans as supervisors not bottlenecks, cognitive atrophy risk.
- Best placed in: CRS-001, CRS-002, CRS-003, CRS-007.

### Conscious Delegation
- Primary sources: StateDD decks, `AI-Driven Development`, `Digitale dubbelgangers`, `Moltbook`.
- Key concepts: decide what to delegate and what to exclude, scope boundaries, human-in-the-loop / human-on-the-loop / human-out-of-the-loop, autonomy budget.
- Best placed in: CRS-001, CRS-004, CRS-006, CRS-007, CRS-008.

### AI Collaboration
- Primary sources: all eight analyses.
- Key concepts: human + AI as tandem, multi-agent setup, coding agent + reviewer agent separation, agents as capable but memoryless partners.
- Best placed in: CRS-001, CRS-003, CRS-006, CRS-008, CRS-009.

### State Driven Development (StateDD)
- Primary sources: StateDD decks, `AI-Driven Development` (both formats).
- Key concepts: repo as source of truth, seven state files, work contracts, proof bundles, closure gates, runtime identity.
- Best placed in: CRS-001, CRS-004, CRS-005, CRS-006.

### Cognitive Atrophy and Staying Relevant
- Primary sources: `AI-20251103_lenny_remix` (both formats), `Moltbook`, `Digitale dubbelgangers`.
- Key concepts: nivelleringseffect, jagged boundary, skill degradation, reinvention of human expertise, filter bubbles.
- Best placed in: CRS-003, CRS-007, CRS-008.

### Governance, Safety, and Compliance
- Primary sources: `AI-20251103_lenny_remix`, `Digitale dubbelgangers`, `Moltbook`, StateDD decks.
- Key concepts: EU AI Act, security/privacy/copyright, bias, transparency, consent, disclosure, liability, drift, acceptance freezes.
- Best placed in: CRS-001, CRS-002, CRS-005, CRS-007, CRS-008.

## Recommended Sequence

The curriculum can be entered from either a **helpdesk/practitioner** angle or a **StateDD/developer-leadership** angle.

### Practitioner Track (helpdesk → governance → resilience)
1. **CRS-002** — AI for the ICT Helpdesk (foundational skills).
2. **CRS-003** — Human-AI Collaboration and Cognitive Resilience (mindset shift).
3. **CRS-007** — Governance, Compliance, and Risk Management (controls).
4. *(Optional)* **CRS-008** — Proactive Social Agents (advanced/specialized).

### Leadership / Engineering Track (StateDD → contracts → evidence)
1. **CRS-001** — StateDD Fundamentals (project OS).
2. **CRS-004** — Writing Verifiable Work Contracts (scoping).
3. **CRS-005** — Proof Bundles, Evidence, and CTO Review (verification).
4. **CRS-006** — Subagents, MCP, and Tool Orchestration (scale).
5. *(Optional)* **CRS-009/CRS-010** — Agents Demystified / Building a Teaching Agent.

### Hybrid Recommended Order
For audiences that span both tracks, the following order respects dependencies and keeps engagement high:
1. CRS-001 or CRS-002 (choose entry point by audience).
2. CRS-003.
3. CRS-007.
4. CRS-004.
5. CRS-005.
6. CRS-006.
7. CRS-008 / CRS-009 / CRS-010 (electives).

## Merge / Consolidate Recommendations

1. **StateDD curriculum spine.** `StateDD_ Een Project-OS voor AI Coding Agents.pptx`, `StateDD v2_ Controleerbare AI-Coding Workflow.pptx`, and `AI-Driven Development` (PPTX + PDF) cover nearly the same StateDD ground. Treat them as a single source family for CRS-001, CRS-004, CRS-005, and CRS-006. Prefer `AI-Driven Development` for the PersonaLab BL-002 case study and `StateDD v2` for the maturity ladder and workshop agendas.

2. **Duplicate format pairs.** `AI-20251103_lenny_remix.pptx` and `.pdf`, plus `AI-Driven Development.pptx` and `.pdf`, are the same presentation in two formats. Do not build separate courses from each; use the extracted pair as one source.

3. **Governance consolidation.** Governance, compliance, and risk content appears in `AI-20251103_lenny_remix`, `Digitale dubbelgangers`, and `Moltbook`. Consolidate into CRS-007 rather than creating parallel ethics/compliance modules.

4. **Cognitive-atrophy / staying-relevant consolidation.** The nivelleringseffect, cognitive atrophy, and "reinvent human expertise" content in `AI-20251103_lenny_remix` overlaps with Moltbook's autonomy/hype framing and `Digitale dubbelgangers`' "real enough for what purpose?" Consolidate these threads in CRS-003.

5. **Agent-loop consolidation.** `Digitale dubbelgangers` (observe → filter → score → time → send) and `Moltbook` (orchestrated loop with context/tools/routing/state/memory) describe similar agent architectures. Cross-reference them in CRS-008 and CRS-009 rather than duplicating.

6. **Canonical template alignment.** The StateDD prompt templates, proof-bundle YAML, and review checklists in the presentations should be merged with the canonical project files (`AGENTS.md`, `prompts/`, `docs/adr/`) to avoid maintaining parallel copies.

## Caveats

- All content is in **Dutch/Flemish**. Any English-language course will require translation; analyses note that some Dutch phrasing in the extracted text is broken or fragmented.
- **Tool names age quickly.** ChatGPT, Gemini, Copilot, NotebookLM, Deep Research, KiloCode, Cursor, and MCP examples will need periodic review cycles.
- **Sparse sections.** Several analyses report slides that are nearly empty in the extracted text (e.g., `AI-20251103_lenny_remix` sections 04–09, `Moltbook` slides 7/13/15/17/18/22/23, `Digitale dubbelgangers` slides 14/16/17). Course designs relying on these sections require direct inspection of the original PPTX/PDF before delivery.
- **Unverified claims.** Specific percentages (e.g., Moltbook context-reload cost), model pricing, benchmark scores, and timeline predictions are reported as-is from the analyses and should be fact-checked before reuse.
