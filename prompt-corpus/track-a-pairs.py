#!/usr/bin/env python3
"""Track A: Prompt↔Response Pairing — What was intended vs what was produced.

For every human prompt, extract the first substantive AI response that followed.
The delta between the two reveals: done, partially done, misheard, or lost.

Outputs pairs.jsonl with {prompt, response, delta_classification}
"""

import json
import glob
import hashlib
import sys
from pathlib import Path
from collections import defaultdict


def extract_user_text(entry: dict) -> str:
    """Extract human-written text from a user JSONL entry."""
    msg = entry.get("message", entry.get("content", {}))
    if isinstance(msg, dict):
        content = msg.get("content", "")
        if isinstance(content, str):
            return content.strip()
        if isinstance(content, list):
            texts = []
            for block in content:
                if isinstance(block, dict):
                    if block.get("type") == "text":
                        texts.append(block.get("text", ""))
            return "\n".join(texts).strip()
    if isinstance(msg, str):
        return msg.strip()
    return ""


def extract_assistant_text(entry: dict) -> str:
    """Extract substantive text from an assistant JSONL entry."""
    msg = entry.get("message", entry.get("content", {}))
    if isinstance(msg, dict):
        content = msg.get("content", [])
        if isinstance(content, list):
            texts = []
            for block in content:
                if isinstance(block, dict) and block.get("type") == "text":
                    texts.append(block.get("text", ""))
            return "\n".join(texts).strip()
    return ""


def is_tool_result(entry: dict) -> bool:
    """Check if a user message is just a tool result (not human-written)."""
    msg = entry.get("message", entry.get("content", {}))
    if isinstance(msg, dict):
        content = msg.get("content", "")
        if isinstance(content, list):
            for block in content:
                if isinstance(block, dict) and block.get("type") == "tool_result":
                    return True
    if entry.get("toolUseResult"):
        return True
    return False


def classify_delta(prompt_text: str, response_text: str) -> str:
    """Quick heuristic classification of prompt→response alignment."""
    if not response_text:
        return "no_response"
    if len(response_text) < 20:
        return "minimal_response"

    pt = prompt_text.lower()
    rt = response_text.lower()

    # Check for explicit acknowledgment patterns
    if any(w in rt[:200] for w in ["understood", "i'll", "let me", "starting", "good"]):
        if len(response_text) > 200:
            return "executed"
        return "acknowledged"

    # Check for questions back
    if "?" in response_text[:300] and any(w in rt[:200] for w in ["would you", "should i", "do you want", "which"]):
        return "clarification_requested"

    # Check for plan/analysis output
    if any(w in rt[:500] for w in ["plan", "phase", "step 1", "approach", "strategy"]):
        return "planned"

    if len(response_text) > 500:
        return "substantive_response"

    return "brief_response"


def process_session(session_path: str) -> list[dict]:
    """Extract prompt→response pairs from a single session JSONL."""
    pairs = []
    try:
        with open(session_path) as f:
            entries = [json.loads(l) for l in f if l.strip()]
    except (json.JSONDecodeError, UnicodeDecodeError):
        return []

    session_id = Path(session_path).stem
    project_slug = ""

    for i, entry in enumerate(entries):
        if entry.get("type") != "user":
            continue
        if is_tool_result(entry):
            continue

        prompt_text = extract_user_text(entry)
        if not prompt_text or len(prompt_text) < 10:
            continue

        # Skip system/tool messages
        if prompt_text.startswith("[Request interrupted") or prompt_text.startswith("Tool loaded"):
            continue

        timestamp = entry.get("timestamp", "")
        if not project_slug:
            project_slug = entry.get("slug", "") or entry.get("cwd", "").split("/")[-1]

        # Find next assistant text response
        response_text = ""
        response_ts = ""
        for j in range(i + 1, min(i + 30, len(entries))):
            if entries[j].get("type") == "assistant":
                text = extract_assistant_text(entries[j])
                if text and len(text) > 5:
                    response_text = text
                    response_ts = entries[j].get("timestamp", "")
                    break

        delta = classify_delta(prompt_text, response_text)

        pairs.append({
            "id": hashlib.sha256(f"{session_id}:{i}:{prompt_text[:100]}".encode()).hexdigest()[:12],
            "session_id": session_id,
            "project_slug": project_slug,
            "timestamp": timestamp,
            "prompt": {
                "text": prompt_text[:8000],
                "char_count": len(prompt_text),
                "truncated": len(prompt_text) > 8000,
            },
            "response": {
                "text": response_text[:8000],
                "char_count": len(response_text),
                "truncated": len(response_text) > 8000,
            },
            "response_timestamp": response_ts,
            "delta": delta,
        })

    return pairs


def main():
    corpus_dir = Path(__file__).parent
    output_path = corpus_dir / "pairs.jsonl"
    report_path = corpus_dir / "PAIRS-REPORT.md"

    all_pairs = []
    delta_dist = defaultdict(int)
    project_dist = defaultdict(int)
    sessions_processed = 0

    # Process all Claude sessions
    print("Processing Claude sessions...")
    claude_sessions = sorted(glob.glob(str(Path.home() / ".claude/projects/*/*.jsonl")))
    for sp in claude_sessions:
        pairs = process_session(sp)
        all_pairs.extend(pairs)
        sessions_processed += 1
        for p in pairs:
            delta_dist[p["delta"]] += 1
            project_dist[p["project_slug"]] += 1

    # Sort by timestamp
    all_pairs.sort(key=lambda p: p.get("timestamp", "") or "9999")

    # Write pairs JSONL
    with open(output_path, "w") as f:
        for pair in all_pairs:
            f.write(json.dumps(pair) + "\n")

    # Find "lost" prompts — those with no_response, minimal_response, or clarification_requested
    lost_or_partial = [p for p in all_pairs if p["delta"] in ("no_response", "minimal_response", "clarification_requested")]

    # Write report
    with open(report_path, "w") as f:
        f.write("# Track A: Prompt↔Response Pairs Report\n\n")
        f.write(f"**Generated:** {__import__('datetime').datetime.now().isoformat()[:19]}Z\n")
        f.write(f"**Sessions processed:** {sessions_processed}\n")
        f.write(f"**Total pairs:** {len(all_pairs)}\n\n")

        f.write("## Delta Distribution\n\n")
        f.write("| Delta | Count | % |\n")
        f.write("|-------|-------|---|\n")
        for delta, count in sorted(delta_dist.items(), key=lambda x: -x[1]):
            pct = count * 100 // max(len(all_pairs), 1)
            f.write(f"| {delta} | {count} | {pct}% |\n")

        f.write(f"\n## Lost or Partial ({len(lost_or_partial)} prompts)\n\n")
        f.write("These prompts received no substantive response — potential recoverable seeds:\n\n")
        for p in lost_or_partial[-50:]:  # Most recent 50
            ts = p.get("timestamp", "")[:10]
            slug = p.get("project_slug", "?")
            text = p["prompt"]["text"][:200].replace("\n", " ")
            delta = p["delta"]
            f.write(f"- **[{delta}]** ({ts} / {slug}) {text}...\n\n")

    print(f"\nTrack A complete:")
    print(f"  Sessions: {sessions_processed}")
    print(f"  Total pairs: {len(all_pairs)}")
    print(f"  Lost/partial: {len(lost_or_partial)}")
    print(f"\n  Delta distribution:")
    for delta, count in sorted(delta_dist.items(), key=lambda x: -x[1]):
        print(f"    {delta}: {count}")
    print(f"\n  Written to: {output_path}")
    print(f"  Report: {report_path}")


if __name__ == "__main__":
    main()
