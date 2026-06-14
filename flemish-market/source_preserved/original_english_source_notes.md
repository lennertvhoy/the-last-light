# Original English Source Notes

**Current active source:** `the_last_light.docx`  
**Preserved copy:** `the_last_light_source_2026-06-04.docx`  
**Extracted Markdown:** `the_last_light_source_2026-06-04.md`

## Source Selection

Two DOCX files exist at the repository root:

- `the_last_light.docx` - observed filesystem mtime: 2026-06-04 09:03:52 +0200, DOCX core created/modified: 2026-06-04T05:58:31Z.
- `The_Last_Light_Manuscript.docx` - observed filesystem mtime: 2026-06-03 21:51:50 +0200, DOCX core created/modified: 2026-06-03T19:45:07Z.

The current source for adaptation is therefore `the_last_light.docx`.

## Extraction

Extraction command:

```bash
pandoc the_last_light.docx -t markdown --wrap=none -o the_last_light_flemish_market/source_preserved/the_last_light_source_2026-06-04.md
```

The extracted source includes front matter, prologue, introduction, and 27 chapters.

## Observed Caveats

- The source contains TODO/VERIFY markers that must not be carried into the publisher-facing Dutch manuscript.
- The source has at least one top-level heading inconsistency: chapter 2 appears as `# The Blessing and the Danger` rather than `# Chapter 2 --- The Blessing and the Danger`.
- The current English manuscript is longer than the intended Dutch/Flemish target and requires compression.

