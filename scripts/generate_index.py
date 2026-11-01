#!/usr/bin/env python3
"""Generate INDEX.md from metadata comments in the solutions directory."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOLUTIONS_DIR = ROOT / "solutions"
OUTPUT_FILE = ROOT / "INDEX.md"

FIELD_PATTERNS = {
    "problem": re.compile(
        r"^\s*(?:#|//|<!--)?\s*Problem\s*[:—-]\s*(.*?)\s*(?:-->)?\s*$",
        re.IGNORECASE,
    ),
    "source": re.compile(
        r"^\s*(?:#|//|<!--)?\s*Source\s*[:—-]\s*(.*?)\s*(?:-->)?\s*$",
        re.IGNORECASE,
    ),
}
COMMENT_PATTERN = re.compile(r"^\s*(?:#|//)\s*(.+?)\s*$")
PRACTICE_NUMBER = re.compile(r"practice(\d+)", re.IGNORECASE)


def read_metadata(path: Path) -> tuple[str, str]:
    """Read problem and source metadata, tolerating missing or unreadable headers."""
    try:
        lines = path.read_text(encoding="utf-8-sig").splitlines()
    except (OSError, UnicodeError):
        return path.stem, ""

    problem = ""
    source = ""
    first_comment = ""

    for line in lines:
        comment = COMMENT_PATTERN.match(line)
        if comment and not first_comment:
            first_comment = comment.group(1).strip()

        for field, pattern in FIELD_PATTERNS.items():
            match = pattern.match(line)
            if match and match.group(1):
                if field == "problem":
                    problem = match.group(1).strip()
                else:
                    source = match.group(1).strip()

        if problem and source:
            break

    if not problem:
        problem = re.sub(
            r"^Problem\s*[—:-]\s*", "", first_comment, flags=re.IGNORECASE
        )
    return problem or path.stem, source


def solution_number(path: Path) -> int:
    """Return the numeric suffix used to sort practice files."""
    match = PRACTICE_NUMBER.search(path.stem)
    return int(match.group(1)) if match else 0


def markdown_cell(value: str) -> str:
    """Escape values for a Markdown table cell."""
    return value.replace("|", r"\|").replace("\n", " ").strip()


def render_index() -> str:
    """Build a row for every solution, including files with incomplete headers."""
    paths = sorted(
        (path for path in SOLUTIONS_DIR.rglob("*") if path.is_file()),
        key=lambda path: (
            path.parent.name.casefold(),
            solution_number(path),
            path.as_posix().casefold(),
        ),
    )
    rows = [
        "# Solutions index",
        "",
        "Generated from metadata comments in the solutions directory by "
        "python scripts/generate_index.py.",
        "",
        "| Problem | Source | Language | File path |",
        "| --- | --- | --- | --- |",
    ]

    for path in paths:
        problem, source = read_metadata(path)
        relative_path = path.relative_to(ROOT).as_posix()
        source_cell = (
            f"[source](<{source.replace('>', '%3E')}>)"
            if source.startswith(("https://", "http://"))
            else markdown_cell(source) or "—"
        )
        rows.append(
            f"| {markdown_cell(problem)} | {source_cell} | "
            f"{markdown_cell(path.parent.name)} | [{relative_path}]({relative_path}) |"
        )

    return "\n".join(rows) + "\n"


def main() -> None:
    OUTPUT_FILE.write_text(render_index(), encoding="utf-8")
    print(f"Generated {OUTPUT_FILE.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
