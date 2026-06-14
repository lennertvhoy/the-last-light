# CLI vs GUI Recommendation for the AI-Driven Development Session

**Scope:** `cli-gui-recommendation` subagent deliverable for the AI-Driven Development course rework.  
**Source family:** CRS-001 / CRS-004 / CRS-005 / CRS-006 (StateDD leadership / engineering track).  
**Trial feedback integrated:**
- Participants were confused about which prompts to use when.
- Caner finds CLI sufficient.
- Lennert thinks GUI lowers cognitive load for non-developers.
- Target audience is mixed: laypeople, developers, and everyone in between.

## 1. The Real Decision

The debate is not CLI *or* GUI. The real teaching objective is:

> *Both interface styles must produce the same StateDD artifacts (state files, work contract, proof bundle, closure gates, CTO review outcome).*

If an interface cannot produce those artifacts reproducibly, it is a bad fit regardless of how friendly it looks. Once that threshold is met, the choice depends on the learner's background, role, and what the demo must prove.

## 2. Audience Segments and Interface Fit

| Segment | Likely background | Best fit | Why |
|---|---|---|---|
| **A. Pure laypeople** (managers, policy, writers, support staff, no command-line comfort) | GUI-first, may fear the terminal | GUI track | Immediate affordances; file tree, chat, and buttons reduce activation energy. |
| **B. Casual tech users** (IT helpdesk, citizen developers, analysts, power users of no-code tools) | Some scripts, Excel, low-code | GUI + optional CLI peek | Start GUI; show CLI as an advanced / reproducible variant so they are not locked out. |
| **C. Developers / DevOps / sysadmins** | Terminal-native | CLI track | Faster, scriptable, version-controlled workflows; matches daily tooling. |
| **D. CTOs / reviewers / auditors** | Mixed | Review-agnostic interface | They mainly inspect proof bundles and state files; interface used to produce them is irrelevant. |

**Practical implication for a mixed workshop:** Offer two parallel onboarding lanes in the first 20 minutes, then merge around the shared StateDD workflow.

## 3. Specific Tools to Compare

| Tool | CLI version | GUI version | Verdict for this course |
|---|---|---|---|
| **Kimi Code** | CLI (`kimi-code` in terminal) | IDE plugins / Kimi WebBridge | Good for both tracks. CLI is mature; GUI lowers barrier. |
| **OpenCode / Claude Code / similar agent CLIs** | CLI-first | Often IDE integrations or web dashboards | Strong CLI; GUI maturity varies. Avoid teaching a CLI-only tool to laypeople unless a web GUI is available. |
| **GitHub Copilot** | `gh copilot` CLI | VS Code / JetBrains / GitHub.com Copilot Chat | Best GUI entry point for developers already in an IDE; CLI is secondary. |
| **Cursor / Windsurf / Zed** | Command palette + terminal inside IDE | IDE-native chat panels | GUI-like but code-centric; good for dev-heavy audiences. Too code-focused for pure laypeople. |
| **Docsify / web prompt helper** | Static Markdown / GitHub Pages | Browser-rendered site | Neutral support layer; works for both tracks. |

**Recommended teaching pair:**
- **CLI track:** Kimi Code CLI or OpenCode CLI (whichever the instructor can actually demo live).
- **GUI track:** Kimi IDE plugin / Kimi WebBridge or GitHub Copilot Chat inside VS Code.

The course should not present a false binary. It should say: *"CLI gives you reproducibility and scriptability; GUI gives you low-friction onboarding. Pick by audience, not by religion."*

## 4. Proposed Hybrid Track

### 4.1 Structure

| Phase | CLI learners | GUI learners | Common output |
|---|---|---|---|
| **Setup** (5 min) | Install CLI, verify `kimi-code --version` | Open IDE plugin / web app, sign in | Both create the same starter repo. |
| **Bootstrap** (15 min) | Run bootstrap prompt in terminal | Run same bootstrap prompt in chat panel | Both produce identical `AGENTS.md`, `STATUS.md`, `PROJECT_STATE.yaml`, `PROJECT_DNA.yaml`, `NEXT_ACTIONS.md`, `BACKLOG.md`, `EVIDENCE_LOG.md`. |
| **Work contract** (20 min) | Paste CTO work-contract prompt into CLI | Paste same prompt into GUI chat | Both produce the same `BACKLOG.md` slice + acceptance criteria. |
| **Implementation** (30 min) | Coding-agent prompt in terminal | Coding-agent prompt in chat panel | Both modify the same files, run tests, create `evidence/BL-002-001/` folder. |
| **Proof bundle** (10 min) | CLI tools generate logs, screenshots, diff | GUI buttons / built-in tools generate same artifacts | Same `proof_manifest.yaml`, same browser screenshot, same git diff. |
| **CTO review** (10 min) | Run review checklist prompt | Run same review checklist prompt | Same ACCEPTED / CONDITIONAL / REJECTED outcome. |
| **State update** (5 min) | Update `STATUS.md`, `NEXT_ACTIONS.md` by hand or agent | Same | Identical state files. |

Total active workshop time after intro: **95 minutes**, fitting inside a 3.5-hour slot alongside opening, breaks, and discussion.

### 4.2 Developer Track

Use CLI for the full workflow. Emphasize:
- Version-controlled prompts (paste prompts from the prompt-copy website, not ad-hoc typing).
- Reproducible proof bundles.
- Scriptable batch runs for the autonomy ladder.

### 4.3 Non-Developer Track

Use GUI. Emphasize:
- Reading the seven state files before asking the agent to do anything.
- Pasting the canonical prompts from the prompt-copy website instead of improvising.
- Inspecting the proof bundle in the file explorer / browser.

## 5. How to Demo Both Without Doubling Prep Time

### 5.1 One Repo, Two Interfaces

Prepare a single canonical repo (the PersonaLab / StateDD template). Run the same prompts through CLI in one window and through GUI in another. This proves the artifacts are identical and avoids maintaining two demo projects.

### 5.2 Screenshot Coverage

Capture the same prompt moments in both interfaces:
1. Bootstrap prompt — terminal vs. chat panel.
2. Coding-agent work-contract prompt — terminal vs. chat panel.
3. Test-run output — terminal vs. integrated test runner.
4. Browser proof — screenshot file in `evidence/` folder (same for both).
5. CTO review prompt — terminal vs. chat panel.
6. State-update prompt / handoff — terminal vs. chat panel.

Pairing screenshots side-by-side on a single slide is high-impact: it shows CLI and GUI as two skins over the same workflow.

### 5.3 Prompt-Website as Shared Ground Truth

Instead of asking Caner to remember CLI prompts and Lennert to remember GUI prompts, both groups pull prompts from the same short-link site (`/prompts/ai-driven-development/`). The course becomes interface-agnostic at the content layer.

## 6. Risks and Mitigations

| Risk | Likely cause | Mitigation |
|---|---|---|
| **CLI intimidates laypeople** | Black terminal, unfamiliar commands | Start GUI; show CLI only as an optional "power user" path. Provide exact copy-paste commands. |
| **GUI hides important mechanics** | Learners do not see file changes, tests, or git diff | Require proof-bundle inspection as a visible step. Make the GUI generate and open the same `evidence/` folder. |
| **Tool versions differ between CLI and GUI** | Feature parity gaps | Choose tools with known parity (Kimi Code CLI + IDE plugin; Copilot Chat + `gh copilot`). Test the exact prompts before delivery. |
| **Instructor cannot demo both live** | Time or screen real estate | Pre-record the second interface; show paired screenshots; run live only on the primary interface for the room's dominant audience. |
| **Participants confuse interface with workflow** | They think StateDD is a tool, not a discipline | Open with: "StateDD is a workflow. The tool is just the pen. Today we will use two pens." |
| **CLI track finishes faster, GUI track falls behind** | Different typing / navigation speeds | Use the prompt website so both groups paste the same content; the time difference is only mechanical, not cognitive. |
| **Caner vs. Lennert debate derails session** | Strong personal preferences | Acknowledge both are valid, anchor on shared artifacts, and offer a 5-minute "interface choice clinic" during exercises. |

## 7. Final Recommendation

**Use a hybrid track, not a single default.**

- **Default for developers and technical leads:** CLI. It is faster, more reproducible, and closer to their existing workflow.
- **Default for laypeople and mixed teams:** GUI. It lowers the activation barrier and keeps the focus on StateDD concepts rather than terminal mechanics.
- **Mandatory equalizer:** Both tracks use the **same canonical prompts** from the prompt-copy website and produce the **same StateDD artifacts**. The course must repeatedly demonstrate this equivalence with paired screenshots.
- **Live demo strategy:** The instructor should choose one interface to run live based on the room's dominant audience, then show the other interface through paired screenshots or a short pre-recorded clip.

**One-sentence handoff for the course-rework subagent:**

> *Teach the StateDD workflow as interface-agnostic, route developers to CLI and non-developers to GUI, and make the prompt-copy website the single source of truth that keeps both tracks aligned.*

## 8. Open Questions for CTO / Course-Design Review

1. Which exact tools can the instructor demo live in the next trial? (Kimi Code CLI + IDE plugin? OpenCode CLI + GUI? Copilot Chat?)
2. Should the prompt-copy website auto-generate both CLI and GUI "paste modes" for each prompt, or keep prompts neutral and add tool-specific notes?
3. Do we want a short "interface selector" diagnostic at registration so learners arrive in the right track?
4. How do we record Caner's StateDD-based program as a student project / community artifact? (Suggested: add a `community-projects/` note in the course appendix and link it from the StateDD template README.)
