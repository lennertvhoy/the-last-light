# Handoff Prompt — Build the AI-Driven Development Prompt-Copy Website

**For:** another coding agent (the user already has a preferred site setup)  
**Context:** AI-Driven Development course rework for *The Last Light*  
**Source planning documents:**
- `g.Presentations/workspaces/ai-driven-dev-rework/INTEGRATED_ACTION_PLAN.md`
- `g.Presentations/workspaces/ai-driven-dev-rework/DESIGN_DECISIONS.md`
- `g.Presentations/workspaces/ai-driven-dev-rework/prompt-website.md`
- `g.Presentations/workspaces/ai-driven-dev-rework/prompt-screenshots.md`
- `g.Presentations/workspaces/ai-driven-dev-rework/cli-gui-recommendation.md`

## Goal

Build a small, fast prompt-copy website that attendees of the AI-Driven Development session can use during and after the workshop. The user already has a preferred site/stack, so **adapt the spec below to that existing site** rather than forcing Docsify.

The site must expose every prompt used in the 10 screenshot moments as a stable, copy-pasteable page/section with a short link.

## Required prompt slugs

Each slug maps to a canonical prompt file in `prompts/`.

| Slug | Canonical source | When used in workshop |
|---|---|---|
| `start` | `prompts/CODING_AGENT_STARTUP_PROMPT.md` | Coding agent starts a slice; reads StateDD files first. |
| `contract` | `prompts/SLICE_CONTRACT_TEMPLATE.md` | Translate a goal into a scoped work contract. |
| `evidence` | `prompts/EVIDENCE_README_TEMPLATE.md` | Build the proof bundle / evidence README. |
| `runtime` | `prompts/RUNTIME_IDENTITY_CHECKLIST.md` | Verify user-facing behavior with runtime identity proof. |
| `review` | `prompts/CTO_REVIEW_CHECKLIST.md` | Run the CTO review and decide ACCEPTED / CONDITIONAL / REJECTED. |
| `handoff` | `prompts/FINAL_HANDOFF_TEMPLATE.md` | Produce the final handoff to the CTO lane. |
| `bootstrap` | `prompts/BOOTSTRAP_INTAKE_PROMPT.md` | Initialize or re-baseline a repo in bootstrap mode. |
| `cto` / `strategy` | `prompts/CTO_SESSION_PROMPT.md` | CTO lane frames the next coding-agent slice. |
| `override` | `AGENTS.md` Human Override Rule | User explicitly overrides a StateDD rule; agent records it. |

## Core UX requirements

1. **One-click copy.** Every prompt card has a copy button that copies the full prompt body to the clipboard.
2. **Short URL per prompt.** Each slug gets a stable short link that can be shown as a QR code or footnote on slides.
3. **Phase navigation.** Group prompts by workshop phase: Start → Contract → Build & Prove → Review & Close → Override/Governance.
4. **CLI/GUI note.** On each card, briefly note whether the prompt is pasted into a CLI tool, IDE chat, or GUI chat, and that both tracks produce the same StateDD artifacts.
5. **Printable one-pager.** Generate/export a single-page handout with all prompts for offline attendees.
6. **Sync warning.** Add a visible "last synced" timestamp and a note that the canonical source lives in `prompts/` in this repo.

## Content rules

- Do not rewrite the canonical prompts unless necessary for web formatting.
- Preserve placeholder syntax like `<project-name>`, `<slice-id>`, `<goal>`.
- For `cto` and `override`, create short prompt cards even though the canonical source is not a standalone prompt file.
- Include a short "When to use this" sentence and a "Copy-paste tip" on each card.

## Integration with the slide deck

The website must support these slide moments (see `prompt-screenshots.md`):
- Moment A/B/1/2 → `#start`
- Moment C/3 → `#contract`
- Moment 4 → `#cto`
- Moment D/6 → `#evidence`
- Moment 5 → `#runtime`
- Moment E/7 → `#review`
- Moment F/8/9 → `#handoff`
- Moment 10 → `#override`
- Moment G → `#bootstrap` or `#start`
- Moment H → site home page

## Suggested tech approach (adapt to user's existing site)

If the user's site is static/React/Vue/etc.:
- Add a new route/page `/ai-driven-dev/prompts` (or equivalent).
- Store prompt content in a JSON/YAML index generated from `prompts/`.
- Use a small script (e.g. `g.Presentations/scripts/generate-prompt-index.py`) to regenerate the index when prompts change.

If the user's site is Docsify:
- Add `docs/ai-driven-dev-prompts.md` and link it from `_sidebar.md`.
- Use hash fragments for slugs: `/#/ai-driven-dev-prompts#start`.

## Acceptance criteria

- [ ] Site/page renders without errors.
- [ ] All 9 slugs resolve and scroll to the correct prompt card.
- [ ] Every copy button copies the full prompt body.
- [ ] Printable one-pager exists and contains all prompts.
- [ ] Prompt content matches the canonical `prompts/` files (verified by diff or checksum).
- [ ] CLI/GUI note visible on every card.
- [ ] Evidence captured in `docs/EVIDENCE_LOG.md` with screenshots of the rendered site and a copy-button test.
- [ ] State files updated if paths or slugs change.

## Evidence to produce

- Screenshot of the prompt site home page.
- Screenshot of one prompt card with copy button.
- Screenshot or log showing a successful copy-to-clipboard test.
- Screenshot of the printable one-pager.
- Entry in `docs/EVIDENCE_LOG.md`.

## State files to update if you change paths or slugs

- `PROJECT_STATE.yaml` → `ai_driven_dev_rework` section
- `NEXT_ACTIONS.md` → NA-18
- `BACKLOG.md` → BL-021
- `docs/EVIDENCE_LOG.md`

## What NOT to do

- Do not discard the user's existing site and rebuild from scratch in a different stack.
- Do not modify the canonical prompt files in `prompts/` unless asked.
- Do not over-design; keep the page fast and copy-paste-first.

## Final handoff

When done, write a brief handoff summarizing:
- what was built,
- the exact URL/path of the prompt site,
- which slugs work,
- how to regenerate the index when `prompts/` changes,
- any blockers or deviations from this spec.
