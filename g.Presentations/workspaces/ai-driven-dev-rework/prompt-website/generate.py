#!/usr/bin/env python3
"""Generate the AI-Driven Development prompt-copy website for Docsify.

Reads g.Presentations/workspaces/ai-driven-dev-rework/prompt-website/prompt-index.yaml
and the canonical prompt files in prompts/ (repo root), then emits:
  - docs/ai-driven-dev/prompts/README.md
  - docs/ai-driven-dev/prompts/_sidebar.md
  - docs/ai-driven-dev/prompts/one-pager.md

Usage from repo root:
    python3 g.Presentations/workspaces/ai-driven-dev-rework/prompt-website/generate.py

Run this whenever a canonical prompt in prompts/ changes.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml


REPO_ROOT = Path(__file__).resolve().parents[4]
WORKSPACE_ROOT = REPO_ROOT / "g.Presentations" / "workspaces" / "ai-driven-dev-rework"
PROMPT_WEBSITE_DIR = WORKSPACE_ROOT / "prompt-website"
PROMPT_INDEX_PATH = PROMPT_WEBSITE_DIR / "prompt-index.yaml"
OUTPUT_DIR = REPO_ROOT / "ai-driven-dev" / "prompts"


@dataclass
class PromptMeta:
    slug: str
    title: str
    hash: str
    phase: str
    source: str
    when: str
    cli_gui: str
    copy_tip: str
    slide_moments: list[str]
    aliases: list[str]


def load_index(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not isinstance(data, dict):
        raise ValueError(f"{path} did not parse as a YAML mapping")
    return data


def extract_text_codeblock(text: str) -> str:
    """Return the content of the first ```text ... ``` block, or the full text."""
    pattern = re.compile(r"```text\n(.*?)```", re.DOTALL)
    match = pattern.search(text)
    if match:
        return match.group(1).rstrip()
    return text.strip()


def extract_agents_section(text: str, section_title: str) -> str:
    """Extract a section from AGENTS.md by heading title prefix."""
    # Match a heading line that starts with the section title (allows subtitles)
    pattern = re.compile(
        rf"^##\s+{re.escape(section_title)}.*?\n(.*?)(?=^##\s|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(text)
    if not match:
        raise ValueError(f"Section '{section_title}' not found in AGENTS.md")
    return match.group(1).strip()


def load_prompt_body(meta: PromptMeta, index: dict[str, Any]) -> str:
    source_path = REPO_ROOT / meta.source
    if not source_path.is_file():
        raise FileNotFoundError(f"Canonical prompt source not found: {source_path}")
    text = source_path.read_text(encoding="utf-8")

    if meta.source.endswith("AGENTS.md"):
        section = index.get("override", {}).get("source_section", "Human Override Rule")
        return extract_agents_section(text, section)

    return extract_text_codeblock(text)


def escape_markdown_fences(text: str, fence: str = "````") -> str:
    """Return text safe to embed inside a fenced code block with the given fence."""
    # If the text contains the closing fence, we would need a longer fence.
    # For simplicity, assert our chosen fence does not appear.
    if fence in text:
        raise ValueError("Prompt body contains the fence sequence; choose a longer fence")
    return text


def build_phase_map(index: dict[str, Any]) -> dict[str, dict[str, Any]]:
    phases = index.get("phases", [])
    return {p["id"]: p for p in phases}


def sort_prompts(prompts: list[PromptMeta], phase_map: dict[str, dict[str, Any]]) -> list[PromptMeta]:
    def key(p: PromptMeta) -> tuple[int, int]:
        order = phase_map.get(p.phase, {}).get("order", 99)
        return (order, p.slide_moments[0] if p.slide_moments else p.slug)
    return sorted(prompts, key=key)


def render_sidebar(index: dict[str, Any], prompts: list[PromptMeta], phase_map: dict[str, dict[str, Any]]) -> str:
    ui = index["ui"]
    site_path = index.get("site_path", "#/ai-driven-dev/prompts")
    lines: list[str] = [
        f"* [{ui['title']}]({site_path})",
        f"* [{ui['print_link']}]({site_path.replace('/prompts', '/prompts/one-pager')})",
        "",
    ]
    for phase_id, phase in sorted(phase_map.items(), key=lambda kv: kv[1].get("order", 99)):
        phase_prompts = [p for p in prompts if p.phase == phase_id]
        if not phase_prompts:
            continue
        lines.append(f"* {phase['title']}")
        for p in phase_prompts:
            lines.append(f"  - [#{p.hash} {p.title}]({site_path}#{p.hash})")
    return "\n".join(lines) + "\n"


def render_readme(index: dict[str, Any], prompts: list[PromptMeta], phase_map: dict[str, dict[str, Any]]) -> str:
    ui = index["ui"]
    site_path = index.get("site_path", "#/ai-driven-dev/prompts")
    synced = index.get("last_synced", datetime.now(timezone.utc).isoformat())
    source_dir = index.get("prompt_source_dir", "prompts")
    source_link = index.get("prompt_source_link", f"../../{source_dir}")

    lines: list[str] = [
        f"# {ui['title']}",
        "",
        ui["subtitle"],
        "",
        ui["home_intro"],
        "",
        f"> **{ui['sync_warning']}:** {synced}  ",
        f"> **{ui['source_note']}:** [`{source_dir}/`]({source_link}/) in deze repo.",
        "",
        "## Fase-navigatie",
        "",
    ]

    for phase_id, phase in sorted(phase_map.items(), key=lambda kv: kv[1].get("order", 99)):
        phase_prompts = [p for p in prompts if p.phase == phase_id]
        if not phase_prompts:
            continue
        lines.append(f"### {phase['title']}")
        lines.append("")
        for p in phase_prompts:
            anchor = f"#{p.hash}"
            lines.append(f"- [{p.title}]({anchor}) — `{site_path}{anchor}`")
        lines.append("")

    lines.append(f"### [{ui['print_link']}](#one-pager)")
    lines.append("")
    lines.append("---")
    lines.append("")

    for p in prompts:
        anchor = f"#{p.hash}"
        aliases = f" / ook bekend als `{'`, `'.join(p.aliases)}`" if p.aliases else ""
        lines.append(f"## {p.title}{aliases} <a id=\"{p.hash}\"></a>")
        lines.append("")
        lines.append(f"**Slug:** `{p.hash}` · **Fase:** {phase_map[p.phase]['title']}")
        if p.slide_moments:
            moments = ", ".join(p.slide_moments)
            lines.append(f"**Screenshot-momenten:** {moments}")
        lines.append("")
        lines.append(f"**{ui['when_label']}** {p.when}")
        lines.append("")
        lines.append(f"**{ui['cli_gui_label']}** {p.cli_gui}")
        lines.append("")
        if p.copy_tip:
            lines.append(f"> **Kopieer-tip:** {p.copy_tip}")
            lines.append("")

        body = load_prompt_body(p, index)
        body = escape_markdown_fences(body, "````")
        lines.append("````text")
        lines.append(body)
        lines.append("````")
        lines.append("")
        lines.append(f"[⬆ {ui['back_to_top']}](#ai-driven-development-workshop-prompten)")
        lines.append("")
        lines.append("---")
        lines.append("")

    # Staged screenshot notice
    lines.append(f"## {ui['staged_label']}")
    lines.append("")
    lines.append(ui["staged_note"])
    lines.append("")
    lines.append("---")
    lines.append("")

    # Community section
    lines.append(f"## {ui['community_title']}")
    lines.append("")
    lines.append(ui["community_intro"])
    lines.append("")

    return "\n".join(lines)


def render_one_pager(index: dict[str, Any], prompts: list[PromptMeta], phase_map: dict[str, dict[str, Any]]) -> str:
    ui = index["ui"]
    site_path = index.get("site_path", "#/ai-driven-dev/prompts")
    synced = index.get("last_synced", datetime.now(timezone.utc).isoformat())

    lines: list[str] = [
        f"# {ui['title']} — {ui['print_link']}",
        "",
        f"**{ui['sync_warning']}:** {synced}",
        "",
        "## Snelle link-lijst",
        "",
    ]

    for phase_id, phase in sorted(phase_map.items(), key=lambda kv: kv[1].get("order", 99)):
        phase_prompts = [p for p in prompts if p.phase == phase_id]
        if not phase_prompts:
            continue
        lines.append(f"### {phase['title']}")
        lines.append("")
        for p in phase_prompts:
            anchor = f"#{p.hash}"
            lines.append(f"- `{p.title}` — {site_path}{anchor}")
        lines.append("")

    lines.append("---")
    lines.append("")

    for p in prompts:
        lines.append(f"## {p.title} (#{p.hash})")
        lines.append("")
        lines.append(f"**Fase:** {phase_map[p.phase]['title']}")
        lines.append("")
        lines.append(f"**{ui['when_label']}** {p.when}")
        lines.append("")
        lines.append(f"**{ui['cli_gui_label']}** {p.cli_gui}")
        lines.append("")
        body = load_prompt_body(p, index)
        lines.append("```text")
        lines.append(body)
        lines.append("```")
        lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def parse_prompts(index: dict[str, Any]) -> list[PromptMeta]:
    prompts: list[PromptMeta] = []
    for item in index.get("prompts", []):
        prompts.append(
            PromptMeta(
                slug=item["slug"],
                title=item["title"],
                hash=item["hash"],
                phase=item["phase"],
                source=item["source"],
                when=item.get("when", ""),
                cli_gui=item.get("cli_gui", ""),
                copy_tip=item.get("copy_tip", ""),
                slide_moments=[str(m) for m in item.get("slide_moments", [])],
                aliases=[str(a) for a in item.get("aliases", [])],
            )
        )
    return prompts


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate AI-Driven Development prompt-copy website")
    parser.add_argument("--check", action="store_true", help="Fail if generated files differ from committed versions")
    parser.add_argument("--index", type=Path, default=PROMPT_INDEX_PATH, help="Path to prompt-index.yaml")
    args = parser.parse_args()

    index = load_index(args.index)
    phase_map = build_phase_map(index)
    prompts = parse_prompts(index)
    prompts = sort_prompts(prompts, phase_map)

    required_slugs = {"start", "contract", "evidence", "runtime", "review", "handoff", "bootstrap", "cto", "override"}
    found_slugs = {p.slug for p in prompts}
    missing = required_slugs - found_slugs
    if missing:
        print(f"ERROR: missing required prompt slugs: {sorted(missing)}", file=sys.stderr)
        return 1

    # Update sync timestamp
    index["last_synced"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    readme = render_readme(index, prompts, phase_map)
    sidebar = render_sidebar(index, prompts, phase_map)
    one_pager = render_one_pager(index, prompts, phase_map)

    readme_path = OUTPUT_DIR / "README.md"
    sidebar_path = OUTPUT_DIR / "_sidebar.md"
    one_pager_path = OUTPUT_DIR / "one-pager.md"

    if args.check:
        for path, content in [(readme_path, readme), (sidebar_path, sidebar), (one_pager_path, one_pager)]:
            existing = path.read_text(encoding="utf-8") if path.exists() else ""
            if existing != content:
                print(f"ERROR: generated file would differ from committed version: {path}", file=sys.stderr)
                return 1
        print("Generated files match committed versions.")
        return 0

    readme_path.write_text(readme, encoding="utf-8")
    sidebar_path.write_text(sidebar, encoding="utf-8")
    one_pager_path.write_text(one_pager, encoding="utf-8")

    # Update the index file with the new sync timestamp so subsequent runs are stable
    args.index.write_text(yaml.safe_dump(index, sort_keys=False, allow_unicode=True), encoding="utf-8")

    print(f"Generated {readme_path}")
    print(f"Generated {sidebar_path}")
    print(f"Generated {one_pager_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
