"""Unit tests for sequence-and-merge.py and sequence-corpus.py — organ derivation, dedup, timestamps."""

import pytest


class TestDeriveOrgan:
    """Tests for derive_organ() from sequence-and-merge.py."""

    def test_organ_i(self, sequence_and_merge_mod):
        assert sequence_and_merge_mod.derive_organ("organvm-i-theoria/recursive-engine") == "ORGAN-I"

    def test_organ_ii(self, sequence_and_merge_mod):
        assert sequence_and_merge_mod.derive_organ("organvm-ii-poiesis/generative-art") == "ORGAN-II"

    def test_organ_iii(self, sequence_and_merge_mod):
        assert sequence_and_merge_mod.derive_organ("organvm-iii-ergon/sovereign-systems") == "ORGAN-III"

    def test_organ_iv(self, sequence_and_merge_mod):
        assert sequence_and_merge_mod.derive_organ("organvm-iv-taxis") == "ORGAN-IV"

    def test_organ_v(self, sequence_and_merge_mod):
        assert sequence_and_merge_mod.derive_organ("organvm-v-logos/public-process") == "ORGAN-V"

    def test_organ_vi(self, sequence_and_merge_mod):
        assert sequence_and_merge_mod.derive_organ("organvm-vi-koinonia/reading-group") == "ORGAN-VI"

    def test_organ_vii(self, sequence_and_merge_mod):
        assert sequence_and_merge_mod.derive_organ("organvm-vii-kerygma/distribution") == "ORGAN-VII"

    def test_meta(self, sequence_and_merge_mod):
        assert sequence_and_merge_mod.derive_organ("meta-organvm/organvm-engine") == "META"

    def test_liminal_4444j99(self, sequence_and_merge_mod):
        assert sequence_and_merge_mod.derive_organ("4444j99/application-pipeline") == "LIMINAL"

    def test_liminal_domus(self, sequence_and_merge_mod):
        assert sequence_and_merge_mod.derive_organ("domus-semper-palingenesis") == "LIMINAL"

    def test_axiom(self, sequence_and_merge_mod):
        assert sequence_and_merge_mod.derive_organ("system-system--system") == "AXIOM"

    def test_unclassified_fallback(self, sequence_and_merge_mod):
        assert sequence_and_merge_mod.derive_organ("some-random-project") == "UNCLASSIFIED"

    def test_empty_string(self, sequence_and_merge_mod):
        assert sequence_and_merge_mod.derive_organ("") == "UNCLASSIFIED"


class TestDedupKey:
    """Tests for dedup_key() from sequence-and-merge.py."""

    def test_deterministic(self, sequence_and_merge_mod):
        entry = {"content": {"text": "hello world"}}
        k1 = sequence_and_merge_mod.dedup_key(entry)
        k2 = sequence_and_merge_mod.dedup_key(entry)
        assert k1 == k2

    def test_different_for_different_text(self, sequence_and_merge_mod):
        e1 = {"content": {"text": "hello world"}}
        e2 = {"content": {"text": "goodbye world"}}
        assert sequence_and_merge_mod.dedup_key(e1) != sequence_and_merge_mod.dedup_key(e2)

    def test_returns_string(self, sequence_and_merge_mod):
        entry = {"content": {"text": "test"}}
        assert isinstance(sequence_and_merge_mod.dedup_key(entry), str)

    def test_fixed_length(self, sequence_and_merge_mod):
        entry = {"content": {"text": "test"}}
        assert len(sequence_and_merge_mod.dedup_key(entry)) == 16

    def test_empty_text(self, sequence_and_merge_mod):
        entry = {"content": {"text": ""}}
        key = sequence_and_merge_mod.dedup_key(entry)
        assert isinstance(key, str)
        assert len(key) == 16


class TestParseTimestamp:
    """Tests for parse_timestamp() from sequence-corpus.py."""

    def test_iso_with_z(self, sequence_corpus_mod):
        result = sequence_corpus_mod.parse_timestamp("2026-03-28T00:07:38Z")
        assert result > 0

    def test_iso_with_offset(self, sequence_corpus_mod):
        result = sequence_corpus_mod.parse_timestamp("2026-03-28T00:07:38+00:00")
        assert result > 0

    def test_empty_string(self, sequence_corpus_mod):
        assert sequence_corpus_mod.parse_timestamp("") == 0.0

    def test_invalid_string(self, sequence_corpus_mod):
        assert sequence_corpus_mod.parse_timestamp("not-a-date") == 0.0

    def test_consistency(self, sequence_corpus_mod):
        ts = "2026-03-28T12:00:00Z"
        r1 = sequence_corpus_mod.parse_timestamp(ts)
        r2 = sequence_corpus_mod.parse_timestamp(ts)
        assert r1 == r2

    def test_ordering_preserved(self, sequence_corpus_mod):
        t1 = sequence_corpus_mod.parse_timestamp("2026-03-28T00:00:00Z")
        t2 = sequence_corpus_mod.parse_timestamp("2026-03-29T00:00:00Z")
        assert t2 > t1


class TestDeduplicate:
    """Tests for deduplicate() from sequence-corpus.py."""

    def test_removes_exact_duplicates_in_window(self, sequence_corpus_mod):
        records = [
            {"source": {"timestamp": "2026-03-28T00:00:00Z"}, "raw_text": "hello", "content": {"text": "hello"}},
            {"source": {"timestamp": "2026-03-28T00:00:30Z"}, "raw_text": "hello", "content": {"text": "hello"}},
        ]
        result = sequence_corpus_mod.deduplicate(records)
        assert len(result) == 1

    def test_keeps_duplicates_outside_window(self, sequence_corpus_mod):
        records = [
            {"source": {"timestamp": "2026-03-28T00:00:00Z"}, "raw_text": "hello", "content": {"text": "hello"}},
            {"source": {"timestamp": "2026-03-28T00:05:00Z"}, "raw_text": "hello", "content": {"text": "hello"}},
        ]
        result = sequence_corpus_mod.deduplicate(records)
        assert len(result) == 2

    def test_keeps_different_texts(self, sequence_corpus_mod):
        records = [
            {"source": {"timestamp": "2026-03-28T00:00:00Z"}, "raw_text": "hello", "content": {"text": "hello"}},
            {"source": {"timestamp": "2026-03-28T00:00:30Z"}, "raw_text": "world", "content": {"text": "world"}},
        ]
        result = sequence_corpus_mod.deduplicate(records)
        assert len(result) == 2

    def test_empty_list(self, sequence_corpus_mod):
        assert sequence_corpus_mod.deduplicate([]) == []
