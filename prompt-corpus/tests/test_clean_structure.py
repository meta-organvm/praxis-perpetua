"""Structural QA for LAST-WEEK-CLEAN.md — validates the markdown format contract."""

import re
from collections import Counter


class TestHeader:
    def test_header_present(self, parsed_corpus):
        assert parsed_corpus["header"]["title"] == "Last Week — Clean Prompt Sequences"

    def test_header_period_format(self, parsed_corpus):
        h = parsed_corpus["header"]
        assert re.match(r"\d{4}-\d{2}-\d{2}", h["period_start"])
        assert re.match(r"\d{4}-\d{2}-\d{2}", h["period_end"])
        assert h["period_start"] <= h["period_end"]

    def test_header_prompt_count_declared(self, parsed_corpus):
        assert parsed_corpus["header"]["clean_prompts"] > 0

    def test_header_sequence_count_declared(self, parsed_corpus):
        assert parsed_corpus["header"]["sequences"] > 0

    def test_header_prompt_count_matches(self, parsed_corpus, all_prompts):
        claimed = parsed_corpus["header"]["clean_prompts"]
        actual = len(all_prompts)
        assert actual == claimed, (
            f"Header claims {claimed} prompts but parsed {actual}"
        )

    def test_header_sequence_count_matches(self, parsed_corpus):
        claimed = parsed_corpus["header"]["sequences"]
        actual = len(parsed_corpus["sequences"])
        assert actual == claimed, (
            f"Header claims {claimed} sequences but parsed {actual}"
        )


class TestSequenceNumbering:
    def test_sequence_numbering_starts_at_one(self, parsed_corpus):
        first = parsed_corpus["sequences"][0]
        assert first["seq_num"] == 1

    def test_sequence_numbering_continuous(self, parsed_corpus):
        nums = [s["seq_num"] for s in parsed_corpus["sequences"]]
        expected = list(range(1, len(nums) + 1))
        gaps = set(expected) - set(nums)
        assert not gaps, f"Missing sequence numbers: {sorted(gaps)}"

    def test_no_duplicate_sequence_numbers(self, parsed_corpus):
        nums = [s["seq_num"] for s in parsed_corpus["sequences"]]
        counts = Counter(nums)
        dupes = {n: c for n, c in counts.items() if c > 1}
        assert not dupes, f"Duplicate sequence numbers: {dupes}"


class TestDateOrdering:
    def test_sequence_dates_non_decreasing(self, parsed_corpus):
        violations = []
        seqs = parsed_corpus["sequences"]
        for i in range(1, len(seqs)):
            if seqs[i]["date"] < seqs[i - 1]["date"]:
                violations.append(
                    f"Seq {seqs[i]['seq_num']} ({seqs[i]['date']}) < "
                    f"Seq {seqs[i - 1]['seq_num']} ({seqs[i - 1]['date']})"
                )
        assert not violations, f"Date ordering violations:\n" + "\n".join(violations[:10])

    def test_dates_within_declared_period(self, parsed_corpus):
        h = parsed_corpus["header"]
        for seq in parsed_corpus["sequences"]:
            assert h["period_start"] <= seq["date"] <= h["period_end"], (
                f"Seq {seq['seq_num']} date {seq['date']} outside period "
                f"{h['period_start']}→{h['period_end']}"
            )


class TestTimestamps:
    def test_timestamps_valid_format(self, all_prompts):
        invalid = []
        for p in all_prompts:
            if not re.match(r"\d{2}:\d{2}:\d{2}$", p["timestamp"]):
                invalid.append(f"Seq {p['seq_num']}: '{p['timestamp']}'")
        assert not invalid, (
            f"{len(invalid)} invalid timestamps:\n" + "\n".join(invalid[:10])
        )

    def test_timestamps_valid_ranges(self, all_prompts):
        invalid = []
        for p in all_prompts:
            parts = p["timestamp"].split(":")
            if len(parts) == 3:
                h, m, s = int(parts[0]), int(parts[1]), int(parts[2])
                if not (0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59):
                    invalid.append(f"Seq {p['seq_num']}: {p['timestamp']} out of range")
        assert not invalid, "\n".join(invalid[:10])

    def test_timestamps_within_sequence_non_decreasing(self, parsed_corpus):
        """Timestamps within a sequence should be non-decreasing, allowing for
        midnight crossings (23:xx → 00:xx) which are valid continuations."""
        violations = []
        for seq in parsed_corpus["sequences"]:
            prompts = seq["prompts"]
            for i in range(1, len(prompts)):
                prev_ts = prompts[i - 1]["timestamp"]
                curr_ts = prompts[i]["timestamp"]
                if curr_ts < prev_ts:
                    # Allow midnight crossing: prev is 23:xx, curr is 00:xx
                    prev_h = int(prev_ts.split(":")[0])
                    curr_h = int(curr_ts.split(":")[0])
                    if prev_h == 23 and curr_h == 0:
                        continue  # Valid midnight crossing
                    violations.append(
                        f"Seq {seq['seq_num']}: {prev_ts} > {curr_ts}"
                    )
        assert not violations, (
            f"{len(violations)} intra-sequence timestamp violations:\n"
            + "\n".join(violations[:10])
        )


class TestOrganClassifications:
    def test_organ_classifications_valid(self, parsed_corpus, known_organs):
        invalid = []
        for seq in parsed_corpus["sequences"]:
            if seq["organ"] not in known_organs:
                invalid.append(f"Seq {seq['seq_num']}: '{seq['organ']}'")
        assert not invalid, (
            f"Unknown organ classifications:\n" + "\n".join(invalid[:10])
        )

    def test_organ_distribution_nonzero(self, parsed_corpus):
        organs = Counter(s["organ"] for s in parsed_corpus["sequences"])
        assert len(organs) >= 3, f"Only {len(organs)} distinct organs — suspiciously low"


class TestWorkspacePaths:
    def test_workspace_paths_present(self, parsed_corpus):
        missing = [
            seq["seq_num"] for seq in parsed_corpus["sequences"]
            if not seq["path"]
        ]
        assert not missing, f"Sequences missing workspace path: {missing[:10]}"

    def test_workspace_path_format(self, parsed_corpus):
        invalid = []
        for seq in parsed_corpus["sequences"]:
            path = seq["path"]
            if "/" not in path and not path.strip():
                invalid.append(f"Seq {seq['seq_num']}: '{path}'")
        assert not invalid, f"Invalid paths:\n" + "\n".join(invalid[:10])


class TestSequenceContent:
    def test_no_empty_sequences(self, parsed_corpus):
        empty = [
            seq["seq_num"] for seq in parsed_corpus["sequences"]
            if not seq["prompts"]
        ]
        assert not empty, f"Empty sequences (no prompts): {empty[:10]}"

    def test_prompt_text_not_empty(self, all_prompts):
        empty = [
            f"Seq {p['seq_num']} @ {p['timestamp']}"
            for p in all_prompts
            if not p["text"].strip()
        ]
        assert not empty, f"Prompts with empty text:\n" + "\n".join(empty[:10])

    def test_total_prompts_reasonable(self, all_prompts):
        assert len(all_prompts) >= 100, f"Only {len(all_prompts)} prompts — file may be truncated"
        assert len(all_prompts) <= 5000, f"{len(all_prompts)} prompts — suspiciously large for one week"
