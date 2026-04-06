"""Unit tests for ingest-supplementary.py — entry schema, size classes, source parsers."""

import json
import pytest
from pathlib import Path


class TestComputeId:
    def test_deterministic(self, ingest_supplementary_mod):
        assert ingest_supplementary_mod.compute_id("test") == ingest_supplementary_mod.compute_id("test")

    def test_different_inputs(self, ingest_supplementary_mod):
        assert ingest_supplementary_mod.compute_id("a") != ingest_supplementary_mod.compute_id("b")

    def test_returns_12_char_hex(self, ingest_supplementary_mod):
        result = ingest_supplementary_mod.compute_id("test")
        assert len(result) == 12
        assert all(c in "0123456789abcdef" for c in result)


class TestMakeEntry:
    def test_schema_has_required_keys(self, ingest_supplementary_mod):
        entry = ingest_supplementary_mod.make_entry(
            text="test prompt content",
            agent="claude",
            source_file="/tmp/test.jsonl",
            timestamp="2026-03-28T00:00:00Z",
            prompt_index=0,
            prompt_count=5,
        )
        required = {"id", "source", "content", "classification", "signals", "threading"}
        assert required.issubset(entry.keys()), f"Missing keys: {required - entry.keys()}"

    def test_content_fields(self, ingest_supplementary_mod):
        entry = ingest_supplementary_mod.make_entry(
            text="hello world test",
            agent="claude",
            source_file="/tmp/test.jsonl",
            timestamp="",
            prompt_index=0,
            prompt_count=1,
        )
        content = entry["content"]
        assert content["text"] == "hello world test"
        assert content["char_count"] == len("hello world test")
        assert content["word_count"] == 3
        assert content["line_count"] == 1

    def test_empty_text_returns_empty(self, ingest_supplementary_mod):
        entry = ingest_supplementary_mod.make_entry(
            text="",
            agent="claude",
            source_file="/tmp/test.jsonl",
            timestamp="",
            prompt_index=0,
            prompt_count=1,
        )
        assert entry == {}

    def test_whitespace_only_returns_empty(self, ingest_supplementary_mod):
        entry = ingest_supplementary_mod.make_entry(
            text="   \n\t  ",
            agent="claude",
            source_file="/tmp/test.jsonl",
            timestamp="",
            prompt_index=0,
            prompt_count=1,
        )
        assert entry == {}

    def test_size_class_terse(self, ingest_supplementary_mod):
        entry = ingest_supplementary_mod.make_entry(
            text="yes ok",
            agent="claude",
            source_file="/tmp/test.jsonl",
            timestamp="",
            prompt_index=0,
            prompt_count=1,
        )
        assert entry["classification"]["size_class"] == "terse"

    def test_size_class_short(self, ingest_supplementary_mod):
        entry = ingest_supplementary_mod.make_entry(
            text="build the pipeline for this project now please",
            agent="claude",
            source_file="/tmp/test.jsonl",
            timestamp="",
            prompt_index=0,
            prompt_count=1,
        )
        assert entry["classification"]["size_class"] == "short"

    def test_size_class_medium(self, ingest_supplementary_mod):
        entry = ingest_supplementary_mod.make_entry(
            text="x" * 200,
            agent="claude",
            source_file="/tmp/test.jsonl",
            timestamp="",
            prompt_index=0,
            prompt_count=1,
        )
        assert entry["classification"]["size_class"] == "medium"

    def test_size_class_long(self, ingest_supplementary_mod):
        entry = ingest_supplementary_mod.make_entry(
            text="x" * 600,
            agent="claude",
            source_file="/tmp/test.jsonl",
            timestamp="",
            prompt_index=0,
            prompt_count=1,
        )
        assert entry["classification"]["size_class"] == "long"

    def test_text_truncation(self, ingest_supplementary_mod):
        long_text = "a" * 15000
        entry = ingest_supplementary_mod.make_entry(
            text=long_text,
            agent="claude",
            source_file="/tmp/test.jsonl",
            timestamp="",
            prompt_index=0,
            prompt_count=1,
        )
        assert len(entry["content"]["text"]) == 10000
        assert entry["raw_text_truncated"] is True

    def test_no_truncation_for_short(self, ingest_supplementary_mod):
        entry = ingest_supplementary_mod.make_entry(
            text="short text",
            agent="claude",
            source_file="/tmp/test.jsonl",
            timestamp="",
            prompt_index=0,
            prompt_count=1,
        )
        assert entry["raw_text_truncated"] is False

    def test_supplementary_tag_present(self, ingest_supplementary_mod):
        entry = ingest_supplementary_mod.make_entry(
            text="test prompt",
            agent="chatgpt",
            source_file="/tmp/test.jsonl",
            timestamp="",
            prompt_index=0,
            prompt_count=1,
        )
        assert f"supplementary:chatgpt" in entry["signals"]["tags"]


class TestClaudeExportIngestion:
    def test_prompt_extraction(self, ingest_supplementary_mod, tmp_path):
        content = (
            "❯ build the new pipeline\n\n"
            "⏺ I'll start building the pipeline...\n\n"
            "❯ now test it\n\n"
            "⏺ Running tests..."
        )
        test_file = tmp_path / "2026-04-04-152030-test-session.txt"
        test_file.write_text(content)
        entries = ingest_supplementary_mod.ingest_claude_export(test_file)
        assert len(entries) >= 1
        texts = [e["content"]["text"] for e in entries]
        assert any("build the new pipeline" in t for t in texts)


class TestChatGPTMarkdownIngestion:
    def test_user_block_extraction(self, ingest_supplementary_mod, tmp_path):
        content = (
            "---\nconversation_id: abc123\n---\n\n"
            "## User\n\n"
            "define the architecture for the engine\n\n"
            "## Assistant\n\n"
            "I'll help design the architecture...\n\n"
            "## User\n\n"
            "now implement step one\n\n"
            "## Assistant\n\n"
            "Starting implementation..."
        )
        test_file = tmp_path / "test-convo.md"
        test_file.write_text(content)
        entries = ingest_supplementary_mod.ingest_chatgpt_markdown(test_file)
        assert len(entries) == 2
        assert "architecture" in entries[0]["content"]["text"]
        assert "implement" in entries[1]["content"]["text"]


class TestSpecStoryIngestion:
    def test_user_block_extraction(self, ingest_supplementary_mod, tmp_path):
        content = (
            "# Session\n\n---\n\n"
            "_**User (2026-03-28T10:00:00Z)**_\n\n"
            "build the dashboard\n\n"
            "---\n\n"
            "_**Assistant (2026-03-28T10:01:00Z)**_\n\n"
            "Building dashboard...\n\n"
            "---\n\n"
            "_**User (2026-03-28T10:05:00Z)**_\n\n"
            "add the graph view\n\n"
            "---\n"
        )
        test_file = tmp_path / "2026-03-28_10-00Z-test.md"
        test_file.write_text(content)
        entries = ingest_supplementary_mod.ingest_specstory(test_file)
        assert len(entries) == 2
        assert "dashboard" in entries[0]["content"]["text"]
        assert "graph" in entries[1]["content"]["text"]


class TestClipboardIngestion:
    def test_paste_app_json(self, ingest_supplementary_mod, tmp_path):
        data = {
            "prompts": [
                {
                    "id": 1,
                    "text": "test clipboard prompt",
                    "source_app": "Terminal",
                    "session_id": "clip-001",
                    "timestamp": "2026-03-28T10:00:00Z",
                    "position_in_session": 0,
                    "session_size": 1,
                },
                {
                    "id": 2,
                    "text": "",
                    "source_app": "Safari",
                    "session_id": "clip-002",
                    "timestamp": "",
                    "position_in_session": 0,
                    "session_size": 1,
                },
            ]
        }
        test_file = tmp_path / "ai-prompts-clipboard-export.json"
        test_file.write_text(json.dumps(data))
        entries = ingest_supplementary_mod.ingest_clipboard(test_file)
        assert len(entries) == 1  # Empty text skipped
        assert "clipboard prompt" in entries[0]["content"]["text"]
        assert entries[0]["source"]["agent"] == "clipboard/terminal"
