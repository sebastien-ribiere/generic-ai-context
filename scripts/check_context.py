#!/usr/bin/env python3
"""Dependency-free, intentionally modest validation of the context skeleton."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "README.md", "AGENTS.md", "CLAUDE.md",
    "docs/constitution.md", "docs/architecture.md",
    "docs/governance.md", "docs/adr/README.md",
    "docs/adr/0000-template.md",
)
STATES = {"Proposed", "Accepted", "Rejected", "Superseded"}
ADR_PATTERN = re.compile(r"^[0-9]{4}-[a-z0-9-]+\.md$")


def validate(root: Path) -> list[str]:
    errors = []
    for name in REQUIRED:
        if not (root / name).is_file():
            errors.append(f"Missing required file: {name}")

    directory = root / "docs/adr"
    if not directory.is_dir():
        return errors

    for file in sorted(directory.glob("*.md")):
        if file.name == "README.md":
            continue
        if not ADR_PATTERN.fullmatch(file.name):
            errors.append(f"Invalid ADR filename: {file.name}")
            continue
        contents = file.read_text(encoding="utf-8")
        if not contents.startswith("# ADR-"):
            errors.append(f"{file.name}: missing ADR title")
        match = re.search(r"(?m)^- \*\*Status:\*\* (\S+)", contents)
        if not match or match.group(1) not in STATES:
            errors.append(f"{file.name}: invalid or missing Status")
        for heading in ("## Context", "## Decision", "## Consequences"):
            if heading not in contents:
                errors.append(f"{file.name}: missing {heading}")
        if file.name != "0000-template.md" and "YYYY-MM-DD" in contents:
            errors.append(f"{file.name}: date not filled in")
        if "Superseded by:** None" not in contents and "Superseded by:** " not in contents:
            errors.append(f"{file.name}: missing supersession metadata")
    return errors


def main() -> int:
    errors = validate(ROOT)
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors))
        return 1
    print("Context structure: OK (not a semantic or security audit)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
