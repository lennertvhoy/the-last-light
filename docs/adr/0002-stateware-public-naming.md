# ADR 0002: Stateware public naming

Status: accepted
Date: 2026-07-14

## Decision

The public category is **Stateware**, the engineering method is
**State-Centric Engineering**, and the portable application specification is
**StateSpec**. Current workflow copy uses StateSpec. Chapter 14 of the current
manuscript and its published navigation use State-Centric Engineering.

## Compatibility boundary

Existing `statedd-*` workflow names, helper filenames, paths, schema/version
identifiers, Git history, presentation filenames, proper names of third-party
programs, archived sources, and evidence remain valid legacy identifiers. They
are not silently rewritten because that would break automation, misname
external artifacts, or falsify the record of what was produced.

The current combined manuscript copies are synchronized with the canonical
manuscript because they are active publication derivatives. Historical source
captures under `archive/`, `Evidence/`, `docs/evidence/`,
`flemish-market/source_preserved/`, and presentation workspaces retain their
original wording.

## Migration rule

New public prose uses Stateware, State-Centric Engineering, and StateSpec.
Parsers and operators continue to accept legacy StateDD identifiers until a
separately versioned physical migration supplies aliases, compatibility tests,
and rollback.
