#!/usr/bin/env python3
"""Convert ingest-supplementary JSONL → distill-compatible JSON array.

Distill's loader expects either a list of {text, ...} or {prompts: [...]}.
Field mapping:
  content.text       → text
  id                  → id
  source.timestamp    → timestamp
  signals.tags        → signals
  content.word_count  → word_count
  content.char_count  → char_count
  classification.size_class -> category (mapped)
"""

import json
from pathlib import Path

IN = Path("~/Workspace/organvm/praxis-perpetua/prompt-corpus/supplementary-prompts-specstory-workspace.jsonl")
OUT = Path("~/Workspace/.specstory/specstory-prompts-distill-input.json")


def main() -> None:
    converted = []
    with open(IN, "r", encoding="utf-8") as fh:
        for line in fh:
            entry = json.loads(line)
            content = entry.get("content", {})
            source = entry.get("source", {})
            signals = entry.get("signals", {})
            text = content.get("text", "").strip()
            if not text:
                continue
            converted.append({
                "id": entry.get("id", ""),
                "text": text,
                "timestamp": source.get("timestamp", ""),
                "category": "General AI Usage",
                "signals": signals.get("tags", []),
                "word_count": content.get("word_count", 0),
                "char_count": content.get("char_count", 0),
                "source_app": source.get("agent", "specstory"),
                "tech_mentions": [],
                "file_refs": signals.get("mentions_files", []),
                "multi_turn": True,
            })

    OUT.write_text(json.dumps(converted, indent=2), encoding="utf-8")
    print(f"Wrote {len(converted)} entries to {OUT}")


if __name__ == "__main__":
    main()
