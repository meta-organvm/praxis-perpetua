"""Unit tests for extract-dialogue.py — noise filtering, text extraction, slug derivation."""

import pytest


class TestExtractHumanText:
    """Tests for extract_human_text() from extract-dialogue.py."""

    def test_preserves_real_text(self, extract_dialogue_mod):
        entry = {"message": {"content": "build the new pipeline"}}
        assert extract_dialogue_mod.extract_human_text(entry) == "build the new pipeline"

    def test_preserves_text_blocks(self, extract_dialogue_mod):
        entry = {"message": {"content": [
            {"type": "text", "text": "first instruction"},
            {"type": "text", "text": "second instruction"},
        ]}}
        result = extract_dialogue_mod.extract_human_text(entry)
        assert "first instruction" in result
        assert "second instruction" in result

    def test_filters_system_reminder(self, extract_dialogue_mod):
        entry = {"message": {"content": "<system-reminder>some system context</system-reminder>"}}
        assert extract_dialogue_mod.extract_human_text(entry) == ""

    def test_filters_command_name(self, extract_dialogue_mod):
        entry = {"message": {"content": "<command-name>read</command-name>"}}
        assert extract_dialogue_mod.extract_human_text(entry) == ""

    def test_filters_task_notification(self, extract_dialogue_mod):
        entry = {"message": {"content": "<task-notification>task completed</task-notification>"}}
        assert extract_dialogue_mod.extract_human_text(entry) == ""

    def test_filters_tool_result_blocks(self, extract_dialogue_mod):
        entry = {"message": {"content": [
            {"type": "tool_result", "content": "file contents here"},
        ]}}
        assert extract_dialogue_mod.extract_human_text(entry) == ""

    def test_filters_request_interrupted(self, extract_dialogue_mod):
        entry = {"message": {"content": "[Request interrupted by user]"}}
        assert extract_dialogue_mod.extract_human_text(entry) == ""

    def test_filters_very_short(self, extract_dialogue_mod):
        entry = {"message": {"content": "ok"}}
        assert extract_dialogue_mod.extract_human_text(entry) == ""

    def test_empty_message(self, extract_dialogue_mod):
        entry = {"message": {}}
        assert extract_dialogue_mod.extract_human_text(entry) == ""

    def test_non_dict_message(self, extract_dialogue_mod):
        entry = {"message": "not a dict"}
        result = extract_dialogue_mod.extract_human_text(entry)
        # Should handle gracefully — either empty or the string itself
        assert isinstance(result, str)


class TestExtractAssistantText:
    """Tests for extract_assistant_text() from extract-dialogue.py."""

    def test_extracts_text_blocks(self, extract_dialogue_mod):
        entry = {"message": {"content": [
            {"type": "text", "text": "Here is my response."},
        ]}}
        assert "response" in extract_dialogue_mod.extract_assistant_text(entry)

    def test_strips_tool_use_blocks(self, extract_dialogue_mod):
        entry = {"message": {"content": [
            {"type": "tool_use", "name": "Read", "input": {"path": "/tmp/test"}},
            {"type": "text", "text": "The file shows..."},
        ]}}
        result = extract_dialogue_mod.extract_assistant_text(entry)
        assert "file shows" in result
        assert "tool_use" not in result.lower()

    def test_strips_thinking_blocks(self, extract_dialogue_mod):
        entry = {"message": {"content": [
            {"type": "text", "text": "<thinking>internal reasoning</thinking>The answer is 42."},
        ]}}
        result = extract_dialogue_mod.extract_assistant_text(entry)
        assert "42" in result
        # Thinking should be stripped
        assert "internal reasoning" not in result

    def test_empty_content(self, extract_dialogue_mod):
        entry = {"message": {"content": []}}
        assert extract_dialogue_mod.extract_assistant_text(entry) == ""

    def test_non_list_content(self, extract_dialogue_mod):
        entry = {"message": {"content": "just a string"}}
        assert extract_dialogue_mod.extract_assistant_text(entry) == ""


class TestDeriveSlug:
    """Tests for derive_slug() from extract-dialogue.py."""

    def test_from_slug_field(self, extract_dialogue_mod):
        entry = {"slug": "my-project"}
        assert extract_dialogue_mod.derive_slug(entry) == "my-project"

    def test_from_cwd(self, extract_dialogue_mod):
        entry = {"cwd": "/Users/4jp/Workspace/meta-organvm/organvm-engine"}
        assert extract_dialogue_mod.derive_slug(entry) == "organvm-engine"

    def test_slug_takes_precedence(self, extract_dialogue_mod):
        entry = {"slug": "preferred", "cwd": "/Users/4jp/Workspace/other"}
        assert extract_dialogue_mod.derive_slug(entry) == "preferred"

    def test_empty_entry(self, extract_dialogue_mod):
        entry = {}
        assert extract_dialogue_mod.derive_slug(entry) == ""

    def test_trailing_slash(self, extract_dialogue_mod):
        entry = {"cwd": "/Users/4jp/Workspace/meta-organvm/"}
        result = extract_dialogue_mod.derive_slug(entry)
        assert result == "meta-organvm"


class TestSessionToMarkdown:
    """Tests for session_to_markdown() from extract-dialogue.py."""

    def test_contains_title(self, extract_dialogue_mod):
        session = {
            "session_id": "abc123def456",
            "project_slug": "test-project",
            "first_timestamp": "2026-03-28T10:00:00Z",
            "last_timestamp": "2026-03-28T11:00:00Z",
            "human_turns": 2,
            "total_turns": 4,
            "turns": [
                {"role": "human", "text": "build this", "timestamp": "2026-03-28T10:00:00Z"},
                {"role": "assistant", "text": "Building...", "timestamp": ""},
                {"role": "human", "text": "test it", "timestamp": "2026-03-28T10:30:00Z"},
                {"role": "assistant", "text": "Tests pass.", "timestamp": ""},
            ],
        }
        md = extract_dialogue_mod.session_to_markdown(session)
        assert "test-project" in md
        assert "2026-03-28" in md
        assert "## Human" in md
        assert "## Assistant" in md

    def test_truncates_long_responses(self, extract_dialogue_mod):
        session = {
            "session_id": "abc123def456",
            "project_slug": "test",
            "first_timestamp": "2026-03-28T10:00:00Z",
            "last_timestamp": "2026-03-28T10:00:00Z",
            "human_turns": 1,
            "total_turns": 2,
            "turns": [
                {"role": "human", "text": "generate a lot", "timestamp": "2026-03-28T10:00:00Z"},
                {"role": "assistant", "text": "x" * 5000, "timestamp": ""},
            ],
        }
        md = extract_dialogue_mod.session_to_markdown(session)
        assert "truncated" in md
