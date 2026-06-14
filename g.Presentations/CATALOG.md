# Presentation Asset Catalog

**Project:** The Last Light  
**Source share:** `//192.168.122.204/Presentations`  
**Source path on Windows:** `C:\Users\lenne\PresentationBackup`  
**Retrieved:** 2026-06-14  
**Total files in source:** 11 presentations + 2 meta files (HANDOFF, MANIFEST)

## Directory layout

```text
g.Presentations/
├── archive/
│   └── older-versions/        # (reserved for removed older/duplicate copies if needed)
├── curated/                   # deduplicated, canonical working set
├── extracted/                 # (reserved for text/image extraction output)
├── meta/
│   ├── HANDOFF_Fedora_Host_Agent.md
│   └── MANIFEST.txt
├── originals/                 # exact mirror of the SMB share tree
├── workspaces/
│   ├── courses/               # agent-swarm course-development outputs
│   └── slides/                # agent-swarm slide-development outputs
└── CATALOG.md                 # this file
```

## Deduplication decisions

| Curated file | Source | Decision |
|---|---|---|
| `AI-Driven Development.pdf` | `originals/Documents/AI-Driven Development.pdf` | Kept one of three exact duplicates (Desktop, Documents, Downloads all identical by size and timestamp). Documents copy chosen as canonical location. |
| `AI-Driven Development.pptx` | `originals/Desktop/Presentaties/AI-Driven Development.pptx` | Kept; different format and much larger than PDF, so treated as distinct asset. |
| `AI-20251103_lenny_remix.pdf` | `originals/Desktop/Presentaties/AI-20251103_lenny_remix.pdf` | Kept; related to PPTX but format differs; flagged for review as possible export. |
| `AI-20251103_lenny_remix.pptx` | `originals/Desktop/Presentaties/AI-20251103_lenny_remix.pptx` | Kept; source presentation. |
| `Digitale dubbelgangers_ wanneer AI zelf initiatief neemt.pptx` | `originals/Documents/Digitale dubbelgangers_ wanneer AI zelf initiatief neemt.pptx` | Kept newer/larger Documents copy (2026-05-05, 30.7 MB). Older Desktop/Presentaties copy (2026-05-04, 5.0 MB) excluded from curated. |
| `Moltbook_MiddagSessie.pptx` | `originals/Desktop/Presentaties/Moltbook_MiddagSessie.pptx` | Kept; only copy. |
| `StateDD v2_ Controleerbare AI-Coding Workflow.pptx` | `originals/Desktop/Presentaties/StateDD v2_ Controleerbare AI-Coding Workflow.pptx` | Kept; larger and later on same day, likely newer revision. |
| `StateDD_ Een Project-OS voor AI Coding Agents.pptx` | `originals/Desktop/Presentaties/StateDD_ Een Project-OS voor AI Coding Agents.pptx` | Kept; title differs from v2, may be a distinct base talk rather than strictly superseded. Flagged for content review. |

## Files excluded from curated (preserved in originals)

| File | Reason | Location in originals |
|---|---|---|
| `AI-Driven Development.pdf` | Exact duplicate | `originals/Desktop/AI-Driven Development.pdf` |
| `AI-Driven Development.pdf` | Exact duplicate | `originals/Downloads/AI-Driven Development.pdf` |
| `Digitale dubbelgangers_ wanneer AI zelf initiatief neemt.pptx` | Older/smaller version | `originals/Desktop/Presentaties/Digitale dubbelgangers_ wanneer AI zelf initiatief neemt.pptx` |

## Notes for downstream work

- The curated folder is the canonical input for agent-swarm course/slide development.
- The `workspaces/courses/` and `workspaces/slides/` directories are intentionally empty; outputs go there.
- Some filenames contain spaces and Dutch characters; scripts should quote paths.
- Related-format pairs to review:
  - `AI-20251103_lenny_remix.pptx` + `.pdf`
  - `AI-Driven Development.pptx` + `.pdf`
- Versioned pair to review:
  - `StateDD v2_ Controleerbare AI-Coding Workflow.pptx` vs `StateDD_ Een Project-OS voor AI Coding Agents.pptx`
