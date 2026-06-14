# NEXT_ACTIONS.md

Active queue only. Items must be directly actionable and small enough for one coding-agent slice.

**Updated At:** 2026-06-14

Every active item references a backlog ID in the form `### Pn [BL-XXX] ...`.

---

## Active Work

### P1 [BL-001] Review and approve StateDD bootstrap baseline
- **Agent ID:** NA-1
- **Scope:** User reviews AGENTS.md, STATUS.md, PROJECT_STATE.yaml, PROJECT_DNA.yaml, PROJECT_ADAPTER.yaml, NEXT_ACTIONS.md, BACKLOG.md, WORKLOG.md.
- **Exit:** User confirms or requests edits; repo_mode updated to `operating` if accepted.
- **Risk:** low

### P2 [BL-003] Update or retire legacy combine-book.sh
- **Agent ID:** NA-2
- **Scope:** Decide whether to repurpose `f.Scripts/combine-book.sh` to copy the canonical manuscript into `e.Combined-Book/` with a timestamp, or remove it and document the new canonical-file workflow.
- **Exit:** Script no longer references archived paths; CI passes.
- **Risk:** low
- **Blocked by:** NA-1 baseline acceptance

### P3 [BL-004] Verify Docsify site renders correctly
- **Agent ID:** NA-3
- **Scope:** Run docsify-cli locally or inspect generated output; confirm sidebar loads, search works, and all chapter anchors resolve.
- **Exit:** No 404s on primary English route; any broken anchors documented.
- **Risk:** low
- **Blocked by:** NA-1 baseline acceptance

### P4 [BL-006] Review Dutch/Flemish sample gate
- **Agent ID:** NA-4
- **Scope:** Review `flemish-market/samples_for_publishers/sample_auteursnoot_inleiding_h1.md` for Dutch/Flemish voice, authority posture, compression, and market fit.
- **Exit:** Sample voice accepted for downstream adaptation or specific revision requirements recorded.
- **Risk:** medium — voice acceptance gates all downstream Flemish work
- **Blocked by:** NA-1 baseline acceptance

### P5 [BL-007] Convert source TODO/VERIFY markers into working verification ledger
- **Agent ID:** NA-5
- **Scope:** Expand `flemish-market/editorial/factual_claims_to_verify.md` into a fuller table using source locations.
- **Exit:** High-risk factual claims grouped by chapter with action labels: verify, soften, remove, or keep internal.
- **Risk:** low
- **Blocked by:** NA-1 baseline acceptance
