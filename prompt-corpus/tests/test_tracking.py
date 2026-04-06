"""Unit tests for track-a-pairs.py and track-b-reverse-chain.py."""

import pytest


class TestClassifyDelta:
    """Tests for classify_delta() from track-a-pairs.py."""

    def test_no_response(self, track_a_pairs_mod):
        assert track_a_pairs_mod.classify_delta("do this", "") == "no_response"

    def test_minimal_response(self, track_a_pairs_mod):
        assert track_a_pairs_mod.classify_delta("build it", "ok") == "minimal_response"

    def test_executed(self, track_a_pairs_mod):
        long_response = "I'll start building the pipeline. " + "x" * 300
        result = track_a_pairs_mod.classify_delta("build the pipeline", long_response)
        assert result == "executed"

    def test_clarification_requested(self, track_a_pairs_mod):
        response = "Would you like me to use React or Vue for this? Which framework do you prefer?"
        result = track_a_pairs_mod.classify_delta("build the frontend", response)
        assert result == "clarification_requested"

    def test_planned(self, track_a_pairs_mod):
        response = "Here's my plan: Step 1 - Set up the database. Phase 2 - Build the API. " + "x" * 400
        result = track_a_pairs_mod.classify_delta("how should we approach this", response)
        assert result in ("planned", "executed", "substantive_response")

    def test_substantive_response(self, track_a_pairs_mod):
        response = "The results show that " + "x" * 600
        result = track_a_pairs_mod.classify_delta("analyze this", response)
        assert result in ("substantive_response", "executed", "planned")

    def test_brief_response(self, track_a_pairs_mod):
        result = track_a_pairs_mod.classify_delta("what is this", "This is a test file.")
        assert result == "brief_response"


class TestIsToolResult:
    """Tests for is_tool_result() from track-a-pairs.py."""

    def test_tool_result_in_content(self, track_a_pairs_mod):
        entry = {"message": {"content": [{"type": "tool_result", "content": "..."}]}}
        assert track_a_pairs_mod.is_tool_result(entry) is True

    def test_tool_use_result_field(self, track_a_pairs_mod):
        entry = {"toolUseResult": {"tool": "read", "result": "..."}}
        assert track_a_pairs_mod.is_tool_result(entry) is True

    def test_normal_text_not_tool_result(self, track_a_pairs_mod):
        entry = {"message": {"content": "hello world"}}
        assert track_a_pairs_mod.is_tool_result(entry) is False

    def test_text_block_not_tool_result(self, track_a_pairs_mod):
        entry = {"message": {"content": [{"type": "text", "text": "hello"}]}}
        assert track_a_pairs_mod.is_tool_result(entry) is False


class TestExtractUserText:
    """Tests for extract_user_text() from track-a-pairs.py."""

    def test_string_content(self, track_a_pairs_mod):
        entry = {"message": {"content": "hello world"}}
        assert track_a_pairs_mod.extract_user_text(entry) == "hello world"

    def test_list_content_text_blocks(self, track_a_pairs_mod):
        entry = {"message": {"content": [
            {"type": "text", "text": "first part"},
            {"type": "text", "text": "second part"},
        ]}}
        result = track_a_pairs_mod.extract_user_text(entry)
        assert "first part" in result
        assert "second part" in result

    def test_empty_content(self, track_a_pairs_mod):
        entry = {"message": {"content": ""}}
        assert track_a_pairs_mod.extract_user_text(entry) == ""


class TestExtractAssistantText:
    """Tests for extract_assistant_text() from track-a-pairs.py."""

    def test_text_blocks_extracted(self, track_a_pairs_mod):
        entry = {"message": {"content": [
            {"type": "text", "text": "Here is my analysis."},
        ]}}
        assert "analysis" in track_a_pairs_mod.extract_assistant_text(entry)

    def test_tool_use_blocks_skipped(self, track_a_pairs_mod):
        entry = {"message": {"content": [
            {"type": "tool_use", "name": "Read", "input": {"path": "/tmp"}},
            {"type": "text", "text": "The file contains..."},
        ]}}
        result = track_a_pairs_mod.extract_assistant_text(entry)
        assert "file contains" in result
        assert "Read" not in result


class TestParseTs:
    """Tests for parse_ts() from track-b-reverse-chain.py."""

    def test_iso_with_z(self, track_b_reverse_chain_mod):
        result = track_b_reverse_chain_mod.parse_ts("2026-03-28T00:07:38Z")
        assert result is not None

    def test_iso_with_offset(self, track_b_reverse_chain_mod):
        result = track_b_reverse_chain_mod.parse_ts("2026-03-28T00:07:38+00:00")
        assert result is not None

    def test_empty_string(self, track_b_reverse_chain_mod):
        assert track_b_reverse_chain_mod.parse_ts("") is None

    def test_none_input(self, track_b_reverse_chain_mod):
        assert track_b_reverse_chain_mod.parse_ts("") is None

    def test_ordering_preserved(self, track_b_reverse_chain_mod):
        t1 = track_b_reverse_chain_mod.parse_ts("2026-03-28T00:00:00Z")
        t2 = track_b_reverse_chain_mod.parse_ts("2026-03-29T00:00:00Z")
        assert t2 > t1
