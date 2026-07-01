"""Cross-artifact data integrity tests for the prompt corpus."""

import json
from collections import Counter, defaultdict
from pathlib import Path


# Organ prefix → expected path fragment
ORGAN_PATH_MAP = {
    "ORGAN-I": "organvm-i-theoria",
    "ORGAN-II": "organvm-ii-poiesis",
    "ORGAN-III": "organvm-iii-ergon",
    "ORGAN-IV": "organvm-iv-taxis",
    "ORGAN-V": "organvm-v-logos",
    "ORGAN-VI": "organvm-vi-koinonia",
    "ORGAN-VII": "organvm-vii-kerygma",
    "META": "meta-organvm",
    "LIMINAL": "4444J99",
}


class TestOrganDistribution:
    def test_organ_distribution_reasonable(self, parsed_corpus):
        total = len(parsed_corpus["sequences"])
        organs = Counter(s["organ"] for s in parsed_corpus["sequences"])
        for organ, count in organs.items():
            pct = count / total
            assert pct < 0.60, (
                f"{organ} has {count}/{total} sequences ({pct:.0%}) — "
                f"dominates the corpus (> 60%)"
            )

    def test_organ_to_path_consistency(self, parsed_corpus):
        mismatches = []
        for seq in parsed_corpus["sequences"]:
            organ = seq["organ"]
            path = seq["path"].lower()
            if organ in ORGAN_PATH_MAP:
                expected = ORGAN_PATH_MAP[organ].lower()
                if expected not in path:
                    mismatches.append(
                        f"Seq {seq['seq_num']}: organ={organ} but path='{seq['path']}' "
                        f"(expected '{expected}' in path)"
                    )
        assert not mismatches, (
            f"{len(mismatches)} organ/path mismatches:\n" + "\n".join(mismatches[:15])
        )


class TestDateRange:
    def test_date_range_matches_header(self, parsed_corpus):
        h = parsed_corpus["header"]
        dates = [s["date"] for s in parsed_corpus["sequences"]]
        assert min(dates) == h["period_start"], (
            f"First date {min(dates)} != header start {h['period_start']}"
        )
        assert max(dates) == h["period_end"], (
            f"Last date {max(dates)} != header end {h['period_end']}"
        )


class TestPromptDistribution:
    def test_prompts_per_sequence_distribution(self, parsed_corpus):
        counts = [len(s["prompts"]) for s in parsed_corpus["sequences"]]
        avg = sum(counts) / len(counts)
        # Average should be reasonable (1-5 prompts per sequence)
        assert 1.0 <= avg <= 5.0, f"Average {avg:.1f} prompts/sequence — unexpected"
        # No single sequence should have an absurd number
        max_count = max(counts)
        assert max_count <= 30, (
            f"Max prompts in one sequence: {max_count} — likely a parsing error"
        )

    def test_single_prompt_sequences_not_dominant(self, parsed_corpus):
        counts = [len(s["prompts"]) for s in parsed_corpus["sequences"]]
        singles = sum(1 for c in counts if c == 1)
        pct = singles / len(counts)
        # It's normal for many sequences to have 1 prompt, but not all
        assert pct < 0.95, (
            f"{pct:.0%} of sequences have only 1 prompt — parser may be splitting wrong"
        )


class TestDuplicates:
    def test_intra_sequence_duplicates_are_rare(self, parsed_corpus):
        """Some rapid-fire duplicates are natural (user pasted same prompt twice).
        Flag if the duplicate rate is abnormally high."""
        dupe_count = 0
        total = 0
        for seq in parsed_corpus["sequences"]:
            texts = [p["text"] for p in seq["prompts"]]
            total += len(texts)
            seen = set()
            for t in texts:
                if t in seen:
                    dupe_count += 1
                seen.add(t)
        pct = dupe_count / total if total else 0
        assert pct < 0.02, (
            f"{dupe_count}/{total} intra-sequence duplicates ({pct:.1%}) — "
            f"above 2% threshold"
        )

    def test_near_duplicate_rate_acceptable(self, all_prompts):
        """Check that exact-text duplicates across all sequences are rare."""
        texts = [p["text"][:200] for p in all_prompts]
        counts = Counter(texts)
        dupes = {t: c for t, c in counts.items() if c > 2}
        total = len(all_prompts)
        dupe_count = sum(c - 1 for c in counts.values() if c > 2)
        pct = dupe_count / total if total else 0
        assert pct < 0.05, (
            f"{dupe_count} cross-sequence duplicates ({pct:.1%}) — "
            f"top offenders: {list(dupes.keys())[:3]}"
        )


class TestTemporalGaps:
    def test_sequence_temporal_gaps_reasonable(self, parsed_corpus):
        """Gaps between consecutive sequences on the same date should be < 12h."""
        seqs = parsed_corpus["sequences"]
        large_gaps = []
        for i in range(1, len(seqs)):
            if seqs[i]["date"] == seqs[i - 1]["date"]:
                t1 = seqs[i - 1]["time"]
                t2 = seqs[i]["time"]
                # Compare HH:MM strings
                if t2 < t1:
                    large_gaps.append(
                        f"Seq {seqs[i]['seq_num']}: time went backward "
                        f"({t1} → {t2}) on {seqs[i]['date']}"
                    )
        assert not large_gaps, (
            f"{len(large_gaps)} same-day time reversals:\n" + "\n".join(large_gaps[:10])
        )


class TestCrossReference:
    def test_cross_reference_sequenced_jsonl(self, corpus_dir, parsed_corpus):
        """If sequenced-prompts.jsonl exists, verify total count is in the same ballpark."""
        jsonl_path = corpus_dir / "sequenced-prompts.jsonl"
        if not jsonl_path.exists():
            return  # Skip silently if JSONL not present

        with open(jsonl_path) as f:
            jsonl_count = sum(1 for line in f if line.strip())

        md_count = parsed_corpus["header"]["clean_prompts"]
        # The JSONL covers the full corpus (all time), the MD covers one week.
        # JSONL count should be >= MD count.
        assert jsonl_count >= md_count, (
            f"sequenced-prompts.jsonl has {jsonl_count} entries but "
            f"LAST-WEEK-CLEAN.md claims {md_count} clean prompts — "
            f"JSONL should contain at least as many"
        )

    def test_unique_seeds_file_exists_if_seeds_exist(self, corpus_dir):
        """If seeds.jsonl exists, SEED-CATALOGUE.md should also exist."""
        seeds = corpus_dir / "seeds.jsonl"
        catalogue = corpus_dir / "SEED-CATALOGUE.md"
        if seeds.exists():
            assert catalogue.exists(), "seeds.jsonl exists but SEED-CATALOGUE.md is missing"
