#!/usr/bin/env python3
"""Print the skill catalog as JSON, for the runcomfy.com/skills pages.

The website keeps a copy. Run this when a skill's name, title, category,
description, example or models change, and update that copy.
"""
import json
import re
from pathlib import Path

catalog = []
for path in sorted(Path(__file__).resolve().parents[1].glob("*/SKILL.md")):
    _, frontmatter, body = path.read_text(encoding="utf-8").split("---\n", 2)
    fields = dict(line.split(": ", 1) for line in frontmatter.strip().splitlines())
    entry = {key: fields[key] for key in ("name", "title", "category", "description", "example")}
    # Model ids are the backticked words with a slash, in the order the skill names them.
    entry["models"] = list(dict.fromkeys(re.findall(r"`([a-z0-9-]+/[a-zA-Z0-9./-]+)`", body)))
    catalog.append(entry)
print(json.dumps(catalog, indent=2, ensure_ascii=False))
