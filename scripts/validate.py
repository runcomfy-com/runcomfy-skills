#!/usr/bin/env python3
"""Checks every skill: its frontmatter, its summary sentence and the skills it points to.

That every tool a skill names exists is checked in the MCP server's tests, which
run against the commit of this repository the server uses.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIELDS = ("name", "title", "category", "description", "example")
CATEGORIES = {"marketing", "content", "edit", "audio", "comfyui", "training"}


def read(path):
    parts = path.read_text(encoding="utf-8").split("---\n", 2)
    if len(parts) != 3 or parts[0]:
        raise ValueError("must start with frontmatter between --- lines")
    fields = dict(line.split(": ", 1) for line in parts[1].strip().splitlines())
    return fields, parts[2]


def main():
    problems = []
    if not (ROOT / "_rules.md").is_file():
        problems.append("_rules.md is missing")

    paths = sorted(ROOT.glob("*/SKILL.md"))
    if not paths:
        problems.append("no skills found")
    skills = {}
    for path in paths:
        try:
            skills[path.parent.name] = read(path)
        except ValueError as error:
            problems.append(f"{path.parent.name}: {error}")

    for folder, (fields, body) in skills.items():
        for field in FIELDS:
            if not fields.get(field, "").strip():
                problems.append(f"{folder}: {field} is missing")
        if fields.get("name") != folder:
            problems.append(f"{folder}: name must match the folder")
        if fields.get("category") not in CATEGORIES:
            problems.append(f"{folder}: unknown category {fields.get('category')}")
        description = fields.get("description", "")
        # The website shows the sentence before ". Use for" on its cards.
        if ". Use for " not in description:
            problems.append(f'{folder}: description needs a sentence, then ". Use for ..."')
        pointers = re.findall(r"`([a-z0-9-]+)` skill", body) + re.findall(r"\(([a-z]+(?:-[a-z]+)+)\)", description)
        for pointer in pointers:
            if pointer not in skills:
                problems.append(f"{folder}: points to {pointer}, which does not exist")

    for problem in problems:
        print(problem)
    print(f"{len(skills)} skills, {len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
