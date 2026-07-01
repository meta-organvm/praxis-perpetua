#!/usr/bin/env python3
"""Wrap ingest-supplementary.py's ingest_specstory() and run it against the
Workspace-anchored .specstory/history/ substrate.

Why: the original script scans ~/.specstory/history which is empty (legacy path
from before SpecStory migrated to project-anchored .specstory/). We point it at
the actual substrate without modifying the original script.
"""

import json
import sys
from pathlib import Path

# Add prompt-corpus to sys.path so we can import the upstream module
sys.path.insert(0, "~/Workspace/organvm/praxis-perpetua/prompt-corpus")

# Import the function we want
import importlib.util
spec = importlib.util.spec_from_file_location(
    "ingest_supplementary",
    "~/Workspace/organvm/praxis-perpetua/prompt-corpus/ingest-supplementary.py"
)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

SUBSTRATE = Path("~/Workspace/.specstory/history")
OUT = Path("~/Workspace/organvm/praxis-perpetua/prompt-corpus/supplementary-prompts-specstory-workspace.jsonl")


def main() -> None:
    files = sorted(SUBSTRATE.glob("*.md"))
    print(f"Scanning {len(files)} files in {SUBSTRATE}...", file=sys.stderr)

    all_entries: list[dict] = []
    per_file_counts: list[tuple[str, int]] = []
    errors = 0

    for p in files:
        try:
            entries = mod.ingest_specstory(p)
            all_entries.extend(entries)
            per_file_counts.append((p.name, len(entries)))
        except Exception as e:
            print(f"  ERROR {p.name}: {e}", file=sys.stderr)
            errors += 1

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        for entry in all_entries:
            fh.write(json.dumps(entry) + "\n")

    print(f"\nIngested {len(all_entries)} prompts across {len(files) - errors} files", file=sys.stderr)
    print(f"Errors: {errors}", file=sys.stderr)
    print(f"Output: {OUT}", file=sys.stderr)

    # Top 5 contributors
    per_file_counts.sort(key=lambda x: -x[1])
    print(f"\nTop 5 most prompt-rich files:", file=sys.stderr)
    for name, n in per_file_counts[:5]:
        print(f"  {n:>5} prompts — {name}", file=sys.stderr)
    print(f"\nFiles with 0 prompts: {sum(1 for _, n in per_file_counts if n == 0)}", file=sys.stderr)


if __name__ == "__main__":
    main()
