# Formatting Cleanup Report

**Audit date:** 2026-06-04  
**Source:** `../source_preserved/the_last_light_source_2026-06-04.md`

## Extraction Result

- DOCX extraction succeeded with Pandoc.
- Plain-text word count: about 118,962 words.
- Markdown regex word count: about 117,523 words.
- Markdown line count: 4,581.
- Heading count: 254.

## Artifact Search

| Artifact | Count | Status |
| --- | ---: | --- |
| Soft hyphen U+00AD | 0 | not found |
| Replacement character U+FFFD | 0 | not found |
| Noncharacter U+FFFE | 0 | not found |
| Object replacement U+FFFC | 0 | not found |
| Unusual Unicode control characters | 0 | not found |
| Double spaces | 4 | observed |
| TODO/VERIFY markers | 75 | observed |

## Formatting Issues To Handle During Adaptation

- Remove or resolve every TODO/VERIFY marker.
- Normalize chapter numbering, especially the unnumbered chapter 2 heading.
- Remove the generated table-of-contents heading from the publisher-facing manuscript unless a DOCX table of contents is intentionally generated.
- Use clean Dutch quotation marks and consistent chapter separators in the final Markdown.
- Keep page breaks for DOCX export, but avoid raw page-break artifacts in Markdown.

## Evidence

Detailed audit output is stored in `../../docs/evidence/2026-06-04-bootstrap-docx-audit/`.

