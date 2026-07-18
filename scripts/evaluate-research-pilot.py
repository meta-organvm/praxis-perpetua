#!/usr/bin/env python3
"""Evaluate the live four-run Perplexity pilot across explicit owner roots."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

from research_pilot_aggregate import (
    PilotAggregateError,
    evaluate_pilot,
    parse_owner_roots,
)


def _write_if_changed(path: Path, payload: str) -> None:
    path = path.resolve()
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.is_file() and path.read_text(encoding="utf-8") == payload:
        return
    temporary = path.with_name(f".{path.name}.tmp")
    temporary.write_text(payload, encoding="utf-8")
    os.replace(temporary, path)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Praxis repository root containing the canonical pilot requests",
    )
    parser.add_argument(
        "--owner-root",
        action="append",
        default=[],
        metavar="OWNER_REPO=/ABSOLUTE/PATH",
        help="explicit owner repository resolution; repeat for every owner",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="optionally write the deterministic aggregate record",
    )
    parser.add_argument(
        "--require-settled",
        action="store_true",
        help="exit 3 while the result remains wait_relay",
    )
    parser.add_argument(
        "--require-pass",
        action="store_true",
        help="exit 1 unless the settled verdict is pass; implies --require-settled",
    )
    args = parser.parse_args()
    try:
        roots = parse_owner_roots(args.owner_root)
        result = evaluate_pilot(args.root, roots)
    except PilotAggregateError as error:
        print(
            json.dumps(
                {
                    "schema_version": "1.0",
                    "commission_id": "INQ-2026-014",
                    "state": "invalid",
                    "error": {"code": error.code, "message": error.message},
                },
                indent=2,
                sort_keys=True,
            )
        )
        return 2

    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    print(payload, end="")
    if result["state"] != "settled" and (args.require_settled or args.require_pass):
        return 3
    if args.output is not None:
        _write_if_changed(args.output, payload)
    if args.require_pass and result["verdict"] != "pass":
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
