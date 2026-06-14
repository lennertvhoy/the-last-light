# Slide Deck Map — The Last Light Presentation Assets

This map turns the slide-deck ideas from the eight per-presentation analyses into a single inventory of proposed slide decks. Each entry maps back to its source presentation(s), gives an estimated slide count, notes priority, and flags decks that are mostly ready to build from extracted text versus those that need visual review of the original assets.

| Deck ID | Title | Source Presentation(s) | Slide Count Estimate | Description | Priority |
|---------|-------|------------------------|----------------------|-------------|----------|
| DECK-001 | StateDD in 7 Files — A Visual Tour | `AI-Driven Development.pptx`; `AI-Driven Development.pdf`; `StateDD_ Een Project-OS voor AI Coding Agents.pptx` | ~25 | File-by-file walkthrough of `AGENTS.md`, `STATUS.md`, `PROJECT_STATE.yaml`, `PROJECT_DNA.yaml`, `NEXT_ACTIONS.md`, `BACKLOG.md`, and `EVIDENCE_LOG.md` with roles, users, and update triggers. | P0 |
| DECK-002 | From Vibe Coding to StateDD — A Leadership Primer | `AI-Driven Development.pptx/pdf`; `StateDD v2_ Controleerbare AI-Coding Workflow.pptx`; `StateDD_ Een Project-OS voor AI Coding Agents.pptx` | ~15 | Condensed executive pitch: the cost of vibe coding, the repo-as-truth shift, and the first three steps to regain control. | P0 |
| DECK-003 | The 4C Prompt Method for IT Professionals | `AI-20251103_lenny_remix.pptx`; `AI-20251103_lenny_remix.pdf` | ~20 | Focused deck teaching Context-Constraints-Criteria-Checkvraag with before/after examples from Active Directory, Outlook, and Linux/UFW. | P0 |
| DECK-004 | AI in the Helpdesk — Workflows and Pitfalls | `AI-20251103_lenny_remix.pptx/pdf` | ~25 | Practical deck mapping research, troubleshooting, documentation, meeting-to-output, scripting, and vibe-coding workflows to helpdesk tasks plus common pitfalls. | P0 |
| DECK-005 | Cognitive Atrophy and the Leveling Effect | `AI-20251103_lenny_remix.pptx/pdf`; `Moltbook_MiddagSessie.pptx` | ~15 | Conceptual deck on the nivelleringseffect, cognitive atrophy, the jagged boundary, and designing resilient human-AI collaboration. | P1 |
| DECK-006 | Evaluating AI Output — From Hallucination to Compliance | `AI-20251103_lenny_remix.pptx/pdf` | ~20 | Decision-support deck built around six evaluation dimensions (correctness, efficiency, security, bias, transparency, compliance) with real IT examples. | P1 |
| DECK-007 | The Proof Bundle — Evidence That AI Work Is Done | `AI-Driven Development.pptx/pdf`; `StateDD v2_ Controleerbare AI-Coding Workflow.pptx` | ~20 | Focused deck on proof-bundle contents, numbering, review, and why "no proof, no closure" matters. | P1 |
| DECK-008 | The CTO Review Checklist | `AI-Driven Development.pptx/pdf`; `StateDD v2_ Controleerbare AI-Coding Workflow.pptx` | ~15 | Interactive training deck where participants decide whether a proof bundle is ACCEPTED, CONDITIONAL, or REJECTED using the 11-point checklist. | P1 |
| DECK-009 | Subagents, MCP, and Separation of Powers | `AI-Driven Development.pptx/pdf`; `StateDD v2_ Controleerbare AI-Coding Workflow.pptx` | ~20 | Visual deck explaining why one agent should not build, test, and approve its own work, plus MCP tool categories and permission boundaries. | P1 |
| DECK-010 | Proactive Social Agents — The Attention Loop | `Digitale dubbelgangers_ wanneer AI zelf initiatief neemt.pptx` | ~15 | Technical slide deck visualizing the observe → filter → score → time → send loop with governance gates. | P2 |
| DECK-011 | Digital Doubles — Consent-First Demo Playbook | `Digitale dubbelgangers_ wanneer AI zelf initiatief neemt.pptx` | ~12 | Practical deck for teams on how to run a labeled, consent-based AI simulation without crossing into impersonation. | P2 |
| DECK-012 | Moltbook — Gamechanger or Hype? | `Moltbook_MiddagSessie.pptx` | ~18 | Updated version of the case-study deck for a general audience, trimming promotional slides and clarifying the agent loop. | P2 |
| DECK-013 | The Four Gaps in Autonomous Agent Networks | `Moltbook_MiddagSessie.pptx` | ~12 | Focused deck expanding identity, memory, governance/liability, and economics into a decision framework for teams. | P2 |
| DECK-014 | Vibe Coding for IT Professionals | `AI-20251103_lenny_remix.pptx/pdf` | ~15 | Concise introduction to AI-assisted coding for scripts, GUIs, and small applications, with review and testing caveats. | P2 |

## Quick-Win Decks

These decks can be built mostly from existing, text-rich slides and reusable artifacts identified in the analyses.

- **DECK-002 — From Vibe Coding to StateDD.** The five-section narrative arc (problem → StateDD solution → workflow → tools → workshop) is already well structured across the StateDD analyses. Reuse the bad-vs-good prompting slide and the "no proof, no closure" rule.
- **DECK-003 — The 4C Prompt Method.** The 4C framework, before/after examples, and printable checklist are explicitly present and highly reusable in `AI-20251103_lenny_remix`.
- **DECK-007 — The Proof Bundle.** Proof-bundle structure, manifest YAML, and examples are directly copyable from `AI-Driven Development` and `StateDD v2`.
- **DECK-008 — The CTO Review Checklist.** The 11-point checklist and ACCEPTED/CONDITIONAL/REJECTED framing are almost template-grade in the StateDD analyses.
- **DECK-010 — Proactive Social Agents — The Attention Loop.** The chatbot-vs-agent comparison, attention loop, and governance checklist are strong, self-contained concepts in `Digitale dubbelgangers`.

## Needs Visual Review

These decks contain sparse extracted text, placeholder slides, or content that depends heavily on diagrams, screenshots, or speaker notes. The original PPTX/PDF must be inspected before building the final deck.

- **DECK-004 — AI in the Helpdesk — Workflows and Pitfalls.** Sections 04 (tool landscape), 05 (reusable workflows), 06 (vibe coding), 07 (governance), 08 (audience-specific packages), and 09 (workshop blocks) in `AI-20251103_lenny_remix` are mostly slide titles in the extraction; many slides are blank placeholders.
- **DECK-005 — Cognitive Atrophy and the Leveling Effect.** Visual diagrams (e.g., neural network, jagged-boundary illustrations) and screenshots are referenced but not captured in the extracted text.
- **DECK-006 — Evaluating AI Output.** Likely relies on tables, checklists, and visual case examples (hallucination, bias, security) that need the original PDF/PPTX.
- **DECK-009 — Subagents, MCP, and Separation of Powers.** The StateDD control-loop diagram, MCP layer, and agent-chain-with-escalation visuals are described but not rendered in the extraction.
- **DECK-012 — Moltbook — Gamechanger or Hype?** Slides 7, 13, 15, 17, 18, 22, and 23 contain almost no on-slide text; their content is only in speaker notes or visuals. The Copilot demo screenshots and "brain with four zones" image must be retrieved from the PPTX.
- **DECK-013 — The Four Gaps in Autonomous Agent Networks.** The "brain with four zones" diagram on slide 12 of `Moltbook` is not described in the extracted text.
- **DECK-014 — Vibe Coding for IT Professionals.** Section 06 (vibe coding) in `AI-20251103_lenny_remix` is sparse in the extraction and likely contains tool screenshots or demo visuals.

## Merge / Consolidate Recommendations

1. **StateDD leadership spine.** DECK-001, DECK-002, DECK-007, DECK-008, and DECK-009 all draw from the StateDD/AI-Driven Development source family. Consider packaging them as a single "StateDD for Teams" deck series with consistent branding.

2. **Avoid double-building from PPTX + PDF.** `AI-Driven Development.pptx` and `.pdf`, and `AI-20251103_lenny_remix.pptx` and `.pdf`, are the same content in different containers. Build one deck per conceptual source, not one per file format.

3. **Governance fragments.** Governance content from `AI-20251103_lenny_remix` (security, bias, EU AI Act), `Digitale dubbelgangers` (consent, disclosure, manipulation), and `Moltbook` (HIL/HOL, liability, drift) should be merged into DECK-006 and any future governance deck rather than maintained separately.

4. **Agent-loop merge.** DECK-010 (attention loop) and DECK-012/DECK-013 (orchestrated loop / four gaps) describe related agent architectures. Consider a single advanced-agent elective that cross-references both, or keep them as companion decks.

5. **Promotional material separation.** Slides 22–27 of `Moltbook` are BoostMeUp promotional content. Strip them from DECK-012 but retain them in a separate branded version if needed.

6. **Canonical asset alignment.** The StateDD prompt templates, proof-manifest YAML, and review checklists in DECK-007 and DECK-008 should be aligned with the canonical project files (`AGENTS.md`, `prompts/`, `docs/adr/`) rather than kept as isolated slide artifacts.

## Caveats

- **Language:** All source decks are Dutch/Flemish. English delivery requires translation; some extracted Dutch phrasing is fragmented.
- **Tool churn:** Specific AI tools, MCP servers, and model comparisons will age quickly and should be versioned or reviewed before each delivery.
- **Placeholder content:** The `Digitale dubbelgangers` analysis notes a placeholder screenshot ("Screenshot toestemming Mikey hier invoegen vóór publicatie") that must be resolved before any public reuse.
- **Unverified claims:** Statistics and predictions from `Moltbook` (e.g., context-reload cost percentages, 2030–2040 timelines) should be fact-checked before inclusion in published decks.
