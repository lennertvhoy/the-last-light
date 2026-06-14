# Analysis: StateDD: Een Project-OS voor AI Coding Agents

## 1. Title & Source

- **Presentation title:** StateDD: Een Project-OS voor AI Coding Agents (subtitle: *Hoe je context decay, fake progress en chaotische agent-sessies voorkomt*)
- **Original file:** `/home/ff/Documents/Projects/the-last-light/g.Presentations/curated/StateDD_ Een Project-OS voor AI Coding Agents.pptx`
- **Format:** PPTX
- **Slides:** 28

## 2. Language

Dutch (Flemish/Dutch — Nederlandstalige content).

## 3. Topic Summary

This presentation introduces **StateDD (State Driven Development)** as a lightweight "project operating system" for AI coding agents. It diagnoses why agent sessions derail — context decay, hallucinated file structures, fake progress, and untested claims — and proposes a disciplined workflow centered on repo-based truth rather than chat history. The deck walks through the StateDD template files, a practical workflow from bootstrap to handoff, compatible coding agents and tools, and ends with a short hands-on workshop. The core message is that AI collaboration works best when the repository, not the chat window, is the source of truth.

## 4. Target Audience

- Software developers and engineers already experimenting with AI coding agents
- Team leads, tech leads, and CTOs managing AI-assisted delivery
- Product architects who want disciplined human-in-the-loop workflows
- Dutch-speaking professional audiences interested in structured AI collaboration

## 5. Key Takeaways

- AI coding agents have no persistent memory across sessions; after ~10–20 prompts they often lose grip on project reality (**context decay**).
- Agents frequently claim "done" while code does not compile, tests fail, or the wrong runtime was tested — **"klaar" is not the same as "bewezen"**.
- StateDD replaces chat-as-truth with a set of repo files that form a shared, machine-checkable contract: `AGENTS.md`, `STATUS.md`, `PROJECT_STATE.yaml`, `NEXT_ACTIONS.md`, `BACKLOG.md`, `EVIDENCE_LOG.md`, `WORKLOG.md`.
- **AGENTS.md** is the operating contract every agent must read first; it defines repo mode (bootstrap vs operating) and universal rules such as "no fake completeness" and "active queue stays short."
- `PROJECT_STATE.yaml` holds structured current truth; `NEXT_ACTIONS.md` is an active-only queue capped at 10 items and linked to stable backlog IDs.
- Every user-facing claim requires evidence recorded in `EVIDENCE_LOG.md`, preferably with runtime identity proof (repo path, branch, HEAD, process/container, endpoint, rebuild status).
- **Separate planning from execution:** the CTO chat/agent chooses the next backlog slice; the coding agent implements, verifies, records, and hands off.
- Every session ends with a **paste-ready handoff** covering what changed, what was verified, runtime identity, evidence references, and the next recommended action.
- StateDD supports multi-agent setups (CTO agent, coding agent, human) and works across tools: Claude Code, Codex, Cursor, Kimi, OpenCode/Aider.
- StateDD is presented as **discipline, not a magic bullet** — a way to make AI-assisted projects more reliable without becoming "process theater."

## 6. The Last Light Themes

- **Human agency:** keeps humans responsible for decisions, acceptance, and override — agents execute, humans judge.
- **Conscious delegation:** explicitly separates the CTO/planning role from the coding/execution role.
- **AI collaboration:** treats AI agents as capable but memoryless partners that need structured context and verification.
- **State Driven Development (StateDD):** the central methodology of the project; this deck is essentially a StateDD primer.
- **Outsourcing without losing oversight:** the presentation warns against outsourcing cognition to the chat window and losing track of what is real.
- **Staying relevant when AI can do more:** humans add value through judgment, verification, and maintaining repo truth, not through raw output volume.

## 7. Course Module Ideas

1. **StateDD Fundamentals: From Ad-Hoc Prompting to Repo Truth**  
   A module that walks learners through the StateDD file system and why "chat as source of truth" fails.

2. **Runtime Identity & Evidence: Proving AI Output Works**  
   Focuses on acceptance freezes, runtime identity proof, evidence logs, and the discipline of verifying before claiming "done."

3. **Bootstrap vs Operating Mode: Managing AI Project Lifecycles**  
   Teaches when to stay in discovery/bootstrap mode, how to know the project DNA is stable enough, and how to transition to operating/delivery mode safely.

## 8. Slide Deck Ideas

1. **The StateDD File System: A Guided Tour**  
   A deeper, file-by-file deck explaining `AGENTS.md`, `STATUS.md`, `PROJECT_STATE.yaml`, `PROJECT_DNA.yaml`, `NEXT_ACTIONS.md`, `BACKLOG.md`, and `EVIDENCE_LOG.md` with concrete examples.

2. **Prompting Like a CTO: Planning vs Execution with AI Agents**  
   Contrasts vague prompts ("fix the bug") with StateDD-style prompts; emphasizes slice scope, verification instructions, and handoff requirements.

3. **StateDD for Teams: Scaling AI Collaboration**  
   Expands the multi-agent setup, team rituals, audit trails, and how to roll StateDD out beyond solo developers.

## 9. Reuse Notes

- **High reuse value:**
  - The five-section narrative arc (Problem → StateDD solution → Workflow → Tools → Workshop).
  - The "bad vs good prompting" slide and concrete StateDD prompt examples.
  - The universal rules from `AGENTS.md`.
  - Runtime identity checklist and handoff template content.
  - The list of compatible agents/tools and how each maps to StateDD.

- **Likely needs updating:**
  - The GitHub URL `github.com/lennertvhoy/StateDD_Template` should be checked against the current canonical project repo.
  - Tool-specific advice (Claude, Codex, Cursor, Kimi, OpenCode/Aider) may need refresh as these products evolve rapidly.
  - Demo screenshots and the `init_template.py` workflow should be verified against the latest project scripts.

- **Good merge candidates:**
  - Other StateDD or agent-management presentations in `g.Presentations/extracted/`.
  - Material on human agency, acceptance freezes, and evidence logging.
  - Workshop activities that let learners touch the StateDD files themselves.

## 10. Confidence & Gaps

- **Confidence:** High for textual content and slide structure. The extracted file contains all 28 slides with full text, so the analysis is based on complete source material.
- **Likely missed because only text was available:**
  - Visual diagrams, especially the "Schone Start → Context Verlies → Chaos" decay diagram on slide 5.
  - Slide design, branding, color coding, and typography.
  - Speaker delivery, pacing, and emphasis.
  - Embedded screenshots, icons, or animated transitions.
  - Any speaker notes or hidden slides not included in the extraction.
  - The live demo flow on slide 22 and how the audience workshop was facilitated.
