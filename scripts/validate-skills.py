#!/usr/bin/env python3
"""Validate Agent Skills compliance for coferlandia-powers."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / ".agents" / "skills"
PLACEHOLDERS = ["TODO", "FIXME", "TBD", "lorem ipsum"]
VAGUE = {"helps", "misc", "stuff", "things", "general", "useful"}
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def parse_frontmatter(text: str):
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must start with YAML frontmatter delimiter '---'")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("Missing closing YAML frontmatter delimiter")
    raw = text[4:end]
    body = text[end + 5:].strip()
    data = {}
    current_key = None
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if not line.startswith((" ", "\t")) and ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip().strip('"\'')
            data[key] = value
            current_key = key
        elif current_key:
            continue
        else:
            raise ValueError(f"Cannot parse frontmatter line: {line!r}")
    return data, body


def warn_if_vague(description: str) -> bool:
    words = set(re.findall(r"[a-z]+", description.lower()))
    return len(description.strip()) < 40 or bool(words & VAGUE) and len(description.strip()) < 90


def main() -> int:
    errors = []
    warnings = []
    if not SKILLS_DIR.is_dir():
        print(f"ERROR: skills directory not found: {SKILLS_DIR}")
        return 1

    skill_dirs = sorted([p for p in SKILLS_DIR.iterdir() if p.is_dir()])
    if not skill_dirs:
        errors.append("No skill directories found under .agents/skills/")

    for skill_dir in skill_dirs:
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.exists():
            errors.append(f"{skill_dir.name}: missing SKILL.md")
            continue
        text = skill_file.read_text(encoding="utf-8")
        try:
            data, body = parse_frontmatter(text)
        except ValueError as exc:
            errors.append(f"{skill_dir.name}: {exc}")
            continue

        name = data.get("name", "").strip()
        description = data.get("description", "").strip()

        if not name:
            errors.append(f"{skill_dir.name}: missing required field 'name'")
        elif name != skill_dir.name:
            errors.append(f"{skill_dir.name}: name field {name!r} does not match parent directory")
        elif not NAME_RE.match(name):
            errors.append(f"{skill_dir.name}: invalid name format")

        if not description:
            errors.append(f"{skill_dir.name}: missing required field 'description'")
        elif len(description) > 1024:
            errors.append(f"{skill_dir.name}: description exceeds 1024 characters")
        elif warn_if_vague(description):
            warnings.append(f"{skill_dir.name}: description may be too vague")

        if len(name) > 64:
            warnings.append(f"{skill_dir.name}: name is longer than 64 characters")
        if not body:
            errors.append(f"{skill_dir.name}: empty skill body")

        lowered = text.lower()
        for marker in PLACEHOLDERS:
            if marker.lower() in lowered:
                warnings.append(f"{skill_dir.name}: unresolved placeholder marker found: {marker}")

    print("Agent Skills validation summary")
    print(f"Root: {ROOT}")
    print(f"Skills checked: {len(skill_dirs)}")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")

    if warnings:
        print("\nWarnings:")
        for warning in warnings:
            print(f"  - {warning}")
    if errors:
        print("\nErrors:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print("\nValidation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
