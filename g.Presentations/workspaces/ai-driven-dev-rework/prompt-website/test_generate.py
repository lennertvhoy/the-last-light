#!/usr/bin/env python3
"""Tests for the AI-Driven Development prompt-copy website generator."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[4]
GENERATOR_DIR = REPO_ROOT / "g.Presentations" / "workspaces" / "ai-driven-dev-rework" / "prompt-website"
GENERATOR = GENERATOR_DIR / "generate.py"
PROMPT_INDEX = GENERATOR_DIR / "prompt-index.yaml"
OUTPUT_DIR = REPO_ROOT / "ai-driven-dev" / "prompts"

REQUIRED_SLUGS = {
    "start",
    "contract",
    "evidence",
    "runtime",
    "review",
    "handoff",
    "bootstrap",
    "cto",
    "override",
}


def load_index() -> dict:
    with PROMPT_INDEX.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def test_required_slugs_present() -> None:
    index = load_index()
    found = {p["slug"] for p in index.get("prompts", [])}
    missing = REQUIRED_SLUGS - found
    assert not missing, f"Missing required slugs: {sorted(missing)}"


def test_canonical_prompt_files_exist() -> None:
    index = load_index()
    for prompt in index.get("prompts", []):
        source = REPO_ROOT / prompt["source"]
        assert source.is_file(), f"Canonical source not found: {source}"


def test_generator_runs() -> None:
    result = subprocess.run(
        [sys.executable, str(GENERATOR)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, f"Generator failed: {result.stderr}"


def test_generated_files_exist() -> None:
    for name in ("README.md", "_sidebar.md", "one-pager.md"):
        path = OUTPUT_DIR / name
        assert path.is_file(), f"Generated file missing: {path}"


def test_generated_readme_contains_all_slugs() -> None:
    readme = (OUTPUT_DIR / "README.md").read_text(encoding="utf-8")
    for slug in REQUIRED_SLUGS:
        assert f'<a id="{slug}"></a>' in readme, f"README missing anchor for #{slug}"


def test_generated_one_pager_contains_all_slugs() -> None:
    one_pager = (OUTPUT_DIR / "one-pager.md").read_text(encoding="utf-8")
    for slug in REQUIRED_SLUGS:
        assert f"(#{slug})" in one_pager, f"One-pager missing heading for #{slug}"


def test_generated_sidebar_contains_all_phases() -> None:
    index = load_index()
    sidebar = (OUTPUT_DIR / "_sidebar.md").read_text(encoding="utf-8")
    for phase in index.get("phases", []):
        assert phase["title"] in sidebar, f"Sidebar missing phase: {phase['title']}"


def test_prompt_bodies_preserved_exactly() -> None:
    """Verify that generated code blocks contain the exact canonical prompt body."""
    import re

    index = load_index()
    # Import the generator helpers to reuse the same extraction logic.
    sys.path.insert(0, str(GENERATOR_DIR))
    try:
        import generate as gen
    finally:
        sys.path.pop(0)

    readme = (OUTPUT_DIR / "README.md").read_text(encoding="utf-8")
    phase_map = gen.build_phase_map(index)
    prompts = gen.sort_prompts(gen.parse_prompts(index), phase_map)

    for prompt in prompts:
        expected_body = gen.load_prompt_body(prompt, index)
        # Find the section for this prompt and extract its code block.
        # Sections end with a separator line "---" followed by the next heading.
        section_pattern = re.compile(
            rf'## {re.escape(prompt.title)}.*?<a id="{re.escape(prompt.hash)}"></a>\n(.*?)\n\n---\n\n(?=## |\Z)',
            re.DOTALL,
        )
        match = section_pattern.search(readme)
        assert match, f"Could not find section for #{prompt.hash}"
        block_match = re.search(r"````text\n(.*?)````", match.group(1), re.DOTALL)
        assert block_match, f"Could not find code block for #{prompt.hash}"
        rendered_body = block_match.group(1).rstrip()
        assert rendered_body == expected_body.rstrip(), (
            f"Prompt body mismatch for #{prompt.slug}. "
            f"Expected {len(expected_body)} chars, got {len(rendered_body)}."
        )


if __name__ == "__main__":
    # Simple runner that exits non-zero on first failure.
    tests = [
        (name, func)
        for name, func in list(globals().items())
        if name.startswith("test_") and callable(func)
    ]
    for name, func in tests:
        try:
            func()
            print(f"PASS: {name}")
        except AssertionError as exc:
            print(f"FAIL: {name}: {exc}", file=sys.stderr)
            sys.exit(1)
        except Exception as exc:
            print(f"ERROR: {name}: {exc}", file=sys.stderr)
            sys.exit(1)
    print("All tests passed.")
