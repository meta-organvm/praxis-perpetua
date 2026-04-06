"""Shared fixtures for prompt corpus QA tests."""

import importlib.util
import json
import re
from pathlib import Path

import pytest


CORPUS_DIR = Path(__file__).resolve().parent.parent

KNOWN_ORGANS = frozenset({
    "ORGAN-I", "ORGAN-II", "ORGAN-III", "ORGAN-IV", "ORGAN-V",
    "ORGAN-VI", "ORGAN-VII", "META", "LIMINAL", "UNCLASSIFIED",
    "AXIOM", "SEED",
})

# Regex patterns for parsing LAST-WEEK-CLEAN.md
HEADER_RE = re.compile(
    r"### (\d+)\. (\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}) · ([A-Z][A-Z0-9-]*) · (.+)"
)
TIMESTAMP_RE = re.compile(r"`(\d{2}:\d{2}:\d{2})`\s+(.+)")


def _parse_clean_md(path: Path) -> dict:
    """Parse LAST-WEEK-CLEAN.md into structured data."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    # Parse header
    header = {"title": "", "period_start": "", "period_end": "", "clean_prompts": 0, "sequences": 0}
    for line in lines[:10]:
        if line.startswith("# "):
            header["title"] = line.lstrip("# ").strip()
        m = re.search(r"\*\*Period:\*\*\s*(\d{4}-\d{2}-\d{2})\s*→\s*(\d{4}-\d{2}-\d{2})", line)
        if m:
            header["period_start"] = m.group(1)
            header["period_end"] = m.group(2)
        m = re.search(r"\*\*Clean prompts:\*\*\s*(\d+)", line)
        if m:
            header["clean_prompts"] = int(m.group(1))
        m = re.search(r"\*\*Sequences:\*\*\s*(\d+)", line)
        if m:
            header["sequences"] = int(m.group(1))

    # Parse sequences
    sequences = []
    current_seq = None

    for line in lines:
        seq_match = HEADER_RE.match(line)
        if seq_match:
            if current_seq:
                sequences.append(current_seq)
            current_seq = {
                "seq_num": int(seq_match.group(1)),
                "date": seq_match.group(2),
                "time": seq_match.group(3),
                "organ": seq_match.group(4),
                "path": seq_match.group(5).strip(),
                "prompts": [],
            }
            continue

        if current_seq:
            ts_match = TIMESTAMP_RE.match(line)
            if ts_match:
                current_seq["prompts"].append({
                    "timestamp": ts_match.group(1),
                    "text": ts_match.group(2).strip(),
                })

    if current_seq:
        sequences.append(current_seq)

    return {"header": header, "sequences": sequences}


@pytest.fixture(scope="session")
def corpus_dir():
    return CORPUS_DIR


@pytest.fixture(scope="session")
def parsed_corpus():
    """Full parsed representation of LAST-WEEK-CLEAN.md."""
    path = CORPUS_DIR / "LAST-WEEK-CLEAN.md"
    assert path.exists(), f"LAST-WEEK-CLEAN.md not found at {path}"
    return _parse_clean_md(path)


@pytest.fixture(scope="session")
def known_organs():
    return KNOWN_ORGANS


@pytest.fixture(scope="session")
def all_prompts(parsed_corpus):
    """Flat list of all prompts across all sequences."""
    prompts = []
    for seq in parsed_corpus["sequences"]:
        for p in seq["prompts"]:
            prompts.append({**p, "seq_num": seq["seq_num"], "organ": seq["organ"], "date": seq["date"]})
    return prompts


@pytest.fixture(scope="session")
def sample_jsonl_entry():
    """A well-formed JSONL entry matching the sequenced-prompts schema."""
    return {
        "id": "abc123def456",
        "source": {
            "session_id": "sess_001",
            "agent": "claude",
            "project_dir": "/Users/4jp/Workspace/meta-organvm",
            "project_slug": "meta-organvm",
            "timestamp": "2026-03-28T00:07:38Z",
            "prompt_index": 0,
            "prompt_count": 5,
        },
        "content": {
            "text": "build the client pillar process",
            "char_count": 31,
            "word_count": 5,
            "line_count": 1,
        },
        "classification": {
            "prompt_type": "unclassified",
            "size_class": "short",
            "session_position": "opener",
            "is_continuation": False,
            "is_interrupted": False,
        },
        "signals": {
            "opening_phrase": "build",
            "imperative_verb": "build",
            "mentions_files": [],
            "mentions_tools": [],
            "tags": [],
        },
        "threading": {
            "thread_id": "t001",
            "thread_label": "client-pillar",
            "arc_position": "opener",
        },
        "organ": "META",
        "domain_fingerprint": "",
        "raw_text_truncated": False,
    }


def _load_script(name: str):
    """Import a hyphenated Python script as a module."""
    script_path = CORPUS_DIR / f"{name}.py"
    if not script_path.exists():
        pytest.skip(f"Script {name}.py not found at {script_path}")
    module_name = name.replace("-", "_")
    spec = importlib.util.spec_from_file_location(module_name, script_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="session")
def extract_seeds_mod():
    return _load_script("extract-seeds")


@pytest.fixture(scope="session")
def sequence_and_merge_mod():
    return _load_script("sequence-and-merge")


@pytest.fixture(scope="session")
def sequence_corpus_mod():
    return _load_script("sequence-corpus")


@pytest.fixture(scope="session")
def ingest_supplementary_mod():
    return _load_script("ingest-supplementary")


@pytest.fixture(scope="session")
def track_a_pairs_mod():
    return _load_script("track-a-pairs")


@pytest.fixture(scope="session")
def track_b_reverse_chain_mod():
    return _load_script("track-b-reverse-chain")


@pytest.fixture(scope="session")
def extract_dialogue_mod():
    return _load_script("extract-dialogue")
