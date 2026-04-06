# Plan: Full QA & Test Suite for Prompt Corpus

## Context

The prompt corpus at `meta-organvm/praxis-perpetua/prompt-corpus/` is the archaeological record of all human prompts across the ORGANVM system. `LAST-WEEK-CLEAN.md` (909 prompts, 535 sequences, 210KB) is the canonical weekly extraction — the base file for this work.

Currently: **zero tests exist.** The CLAUDE.md says "CI validates markdown structure only" but there is no actual test infrastructure in the prompt-corpus directory. Six Python scripts process the corpus with no automated verification. This plan establishes a complete test suite covering both the markdown artifact and the processing scripts.

## What We're Testing

1. **LAST-WEEK-CLEAN.md structural integrity** — the markdown format contract
2. **Python script unit tests** — the 6 extraction/classification/sequencing scripts
3. **Cross-artifact consistency** — JSONL ↔ markdown ↔ header claims

## Files to Create

| File | Purpose |
|------|---------|
| `prompt-corpus/tests/__init__.py` | Test package |
| `prompt-corpus/tests/conftest.py` | Shared fixtures (parsed corpus, sample entries) |
| `prompt-corpus/tests/test_clean_structure.py` | LAST-WEEK-CLEAN.md structural QA |
| `prompt-corpus/tests/test_data_integrity.py` | Cross-artifact data consistency |
| `prompt-corpus/tests/test_extract_seeds.py` | `extract-seeds.py` unit tests |
| `prompt-corpus/tests/test_sequence_corpus.py` | `sequence-and-merge.py` + `sequence-corpus.py` unit tests |
| `prompt-corpus/tests/test_ingest_supplementary.py` | `ingest-supplementary.py` unit tests |
| `prompt-corpus/tests/test_tracking.py` | `track-a-pairs.py` + `track-b-reverse-chain.py` unit tests |
| `prompt-corpus/tests/test_extract_dialogue.py` | `extract-dialogue.py` unit tests |

## Implementation Steps

### Step 1: conftest.py — Shared Fixtures

Parse LAST-WEEK-CLEAN.md into a structured representation for all tests:

```python
@pytest.fixture(scope="session")
def parsed_corpus():
    """Parse LAST-WEEK-CLEAN.md into list of sequences."""
    # Returns: { header: {period, clean_prompts, sequences}, sequences: [{seq_num, date, time, organ, path, prompts: [{timestamp, text}]}] }
```

Key fixtures:
- `parsed_corpus` — full parsed markdown → structured data
- `corpus_dir` — path to prompt-corpus/
- `sample_jsonl_entry` — one well-formed JSONL record for schema tests
- `known_organs` — frozenset of valid organ classifications

### Step 2: test_clean_structure.py — Markdown Structural QA (15+ tests)

Tests against LAST-WEEK-CLEAN.md format contract:

- `test_header_present` — file starts with `# Last Week — Clean Prompt Sequences`
- `test_header_period_format` — `**Period:** YYYY-MM-DD → YYYY-MM-DD`
- `test_header_prompt_count_matches` — claimed 909 matches actual parsed count
- `test_header_sequence_count_matches` — claimed 535 matches actual parsed count
- `test_sequence_numbering_continuous` — 1, 2, 3, ..., 535 with no gaps or duplicates
- `test_sequence_dates_non_decreasing` — date of seq N <= date of seq N+1
- `test_timestamps_valid_format` — all backtick timestamps match `HH:MM:SS`
- `test_timestamps_within_sequence_non_decreasing` — timestamps within each sequence don't go backward
- `test_organ_classifications_valid` — all organs in known set: {ORGAN-I..VII, META, LIMINAL, UNCLASSIFIED, AXIOM, SEED}
- `test_workspace_paths_present` — every sequence has a workspace path after the organ
- `test_workspace_path_format` — paths follow `org/repo` or `user/repo` pattern
- `test_no_empty_sequences` — every sequence has at least one timestamped prompt
- `test_sequence_separator_present` — `---` separates every sequence
- `test_no_consecutive_blank_sequences` — no back-to-back empty entries
- `test_prompt_text_not_empty` — no timestamp with zero-length text after it

### Step 3: test_data_integrity.py — Cross-Artifact Consistency (8+ tests)

- `test_organ_distribution_reasonable` — no single organ > 60% of prompts
- `test_date_range_matches_header` — first/last dates match the Period line
- `test_prompts_per_sequence_distribution` — most sequences have 1-5 prompts, flagging outliers
- `test_no_exact_duplicate_prompts` — no two identical prompt texts (within 60s window, matching dedup logic)
- `test_organ_to_path_consistency` — ORGAN-III paths contain `organvm-iii-ergon`, etc.
- `test_unique_timestamps_per_second` — no collision (same HH:MM:SS in same sequence with different text)
- `test_sequence_temporal_gaps_reasonable` — gap between consecutive sequences < 24h (within a day's work)
- `test_cross_reference_sequenced_jsonl` — if sequenced-prompts.jsonl exists, verify prompt count alignment

### Step 4: test_extract_seeds.py — Seed Classification Unit Tests (12+ tests)

Test the `classify_seed()` function from extract-seeds.py:

- `test_design_directive_match` — "define the schema for..." → design_directive
- `test_design_directive_needs_threshold` — single pattern match insufficient (threshold=2)
- `test_theoretical_grounding_match` — "the telos demands..." → theoretical_grounding
- `test_consolidation_order_match` — "merge these three modules" → consolidation_order
- `test_naming_act_match` — "call it recursive-engine--generative-entity" → naming_act
- `test_rejection_correction_match` — "no, not that approach" → rejection_correction
- `test_strategic_vision_match` — "the revenue model and growth strategy" → strategic_vision
- `test_process_definition_match` — "the workflow should be: step 1..." → process_definition
- `test_no_seed_for_trivial` — "yes" / "ok" / "continue" → empty list
- `test_multiple_seed_types` — a rich prompt can match multiple types
- `test_short_prompts_skipped` — text < 15 chars skipped by main()
- `test_seed_types_are_valid` — all returned types are from the known 7-type set

### Step 5: test_sequence_corpus.py — Sequencing & Dedup Tests (8+ tests)

Test from both `sequence-and-merge.py` and `sequence-corpus.py`:

- `test_derive_organ_known_prefixes` — all 9 organ prefixes map correctly
- `test_derive_organ_unclassified_fallback` — unknown slugs → "UNCLASSIFIED"
- `test_derive_organ_liminal` — "4444j99" and "domus" → "LIMINAL"
- `test_dedup_key_deterministic` — same text always produces same key
- `test_dedup_key_different_for_different_text` — different texts produce different keys
- `test_parse_timestamp_iso` — standard ISO timestamps parse correctly
- `test_parse_timestamp_empty` — empty string → 0.0
- `test_parse_timestamp_invalid` — garbage string → 0.0

### Step 6: test_ingest_supplementary.py — Supplementary Ingestion Tests (10+ tests)

Test `make_entry()` and per-source ingestors:

- `test_make_entry_schema` — output has all required keys (id, source, content, classification, signals, threading)
- `test_make_entry_empty_text_returns_empty` — blank text → empty dict
- `test_make_entry_size_class_terse` — < 20 chars → "terse"
- `test_make_entry_size_class_long` — > 500 chars → "long"
- `test_make_entry_text_truncation` — text > 10000 chars truncated, `raw_text_truncated=True`
- `test_compute_id_deterministic` — same input always same hash
- `test_claude_export_prompt_extraction` — mock ❯-prefixed text parsed correctly
- `test_chatgpt_markdown_extraction` — mock `## User` blocks parsed
- `test_specstory_extraction` — mock `_**User (ts)**_` blocks parsed
- `test_clipboard_json_extraction` — mock Paste.app JSON parsed

### Step 7: test_tracking.py — Tracking Script Tests (6+ tests)

- `test_classify_delta_no_response` — empty response → "no_response"
- `test_classify_delta_executed` — acknowledgment + long response → "executed"
- `test_classify_delta_clarification` — question words → "clarification_requested"
- `test_is_tool_result_detection` — tool_result blocks detected
- `test_extract_user_text_string_content` — simple string → extracted
- `test_extract_user_text_list_content` — list of text blocks → joined

### Step 8: test_extract_dialogue.py — Dialogue Extraction Tests (6+ tests)

- `test_extract_human_text_filters_noise` — system-reminder, tool results → empty
- `test_extract_human_text_preserves_real` — actual human text preserved
- `test_extract_assistant_text_strips_thinking` — thinking blocks removed
- `test_extract_assistant_text_strips_tool_use` — tool_use blocks skipped
- `test_derive_slug_from_cwd` — path extraction works
- `test_session_to_markdown_format` — output contains expected headers

## Existing Functions to Reuse

All functions under test already exist — no new production code needed. Import paths:

| Script | Key Functions |
|--------|--------------|
| `extract-seeds.py:81` | `classify_seed(text)` |
| `sequence-and-merge.py:18-45` | `dedup_key(entry)`, `derive_organ(slug)` |
| `sequence-corpus.py:23-37` | `parse_timestamp(ts)`, `deduplicate(records)` |
| `ingest-supplementary.py:22-81` | `compute_id(text)`, `make_entry(...)` |
| `track-a-pairs.py:65-92` | `classify_delta(prompt, response)`, `is_tool_result(entry)`, `extract_user_text(entry)` |
| `track-b-reverse-chain.py:20-30` | `parse_ts(ts_str)` |
| `extract-dialogue.py:39-99` | `extract_human_text(entry)`, `extract_assistant_text(entry)`, `derive_slug(entry)` |

**Import note:** Script filenames use hyphens (e.g., `extract-seeds.py`), which are invalid Python identifiers. Tests will use `importlib` to import them:

```python
import importlib.util
spec = importlib.util.spec_from_file_location("extract_seeds", corpus_dir / "extract-seeds.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
```

## Verification

```bash
cd /Users/4jp/Workspace/meta-organvm/praxis-perpetua/prompt-corpus
python3 -m pytest tests/ -v --tb=short
```

Expected: 70+ tests, all green. The test suite validates:
1. LAST-WEEK-CLEAN.md structural contract holds
2. All 6 Python scripts' core functions work correctly
3. Cross-artifact data is consistent

No production code changes needed — this is pure QA instrumentation.
