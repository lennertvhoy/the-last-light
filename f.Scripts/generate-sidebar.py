#!/usr/bin/env python3
"""Generate a Docsify _sidebar.md from The-Last-Light.md headings."""

import re
import unicodedata
from pathlib import Path


def slugify(text: str) -> str:
    """Approximate Docsify default slugify."""
    text = text.strip().lower()
    # Normalize unicode (e.g., em-dashes to regular dashes)
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    # Replace non-alphanumeric with hyphens
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-")
    return text


def is_chapter_heading(title: str) -> bool:
    """Return True for top-level book headings we want in the sidebar."""
    t = title.strip()
    # Skip the main title and subtitle lines that appear at the very top
    if t.startswith("The Last Light:") or t == "A Field Guide to AI, Agency, and Conscious Delegation":
        return False
    # Keep known front matter / structural headings
    if t in {"Author's Note", "Prologue", "Introduction", "Appendices"}:
        return True
    if t.startswith(("Chapter ", "Interlude ", "Appendix ", "Epilogue")):
        return True
    return False


def main():
    root = Path(__file__).resolve().parent.parent
    manuscript = root / "The-Last-Light.md"
    sidebar = root / "_sidebar.md"

    headings = []
    with manuscript.open("r", encoding="utf-8") as f:
        for line in f:
            m = re.match(r"^(#{1,3})\s+(.+)$", line)
            if not m:
                continue
            level = len(m.group(1))
            title = m.group(2).strip()
            headings.append((level, title))

    lines = []
    lines.append("* [The Last Light](/The-Last-Light.md)")
    lines.append("")
    lines.append("* Front Matter")
    lines.append("  - [Author's Note](/The-Last-Light.md#authors-note)")
    lines.append("  - [Prologue](/The-Last-Light.md#prologue-the-last-animal-that-knew-it-was-dying)")
    lines.append("  - [Introduction](/The-Last-Light.md#introduction-the-question-is-not-replacement)")
    lines.append("")
    lines.append("* Chapters")

    front_matter = {"Author's Note", "Prologue", "Introduction"}
    appendix_started = False
    for level, title in headings:
        if level != 1:
            continue
        if not is_chapter_heading(title):
            continue
        if title in front_matter:
            continue

        if title == "Appendices":
            lines.append("")
            lines.append("* Appendices")
            appendix_started = True
            continue

        anchor = slugify(title)
        link_text = title.replace("#", "").strip()
        entry = f"  - [{link_text}](/The-Last-Light.md#{anchor})"
        lines.append(entry)

    # Remove the empty "Chapters" line if nothing ended up under it (shouldn't happen)
    if lines and lines[-1] == "* Chapters":
        lines.pop()

    sidebar.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {sidebar}")


if __name__ == "__main__":
    main()
