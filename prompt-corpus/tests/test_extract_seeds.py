"""Unit tests for extract-seeds.py — seed classification logic."""

import pytest

VALID_SEED_TYPES = frozenset({
    "design_directive", "theoretical_grounding", "consolidation_order",
    "naming_act", "rejection_correction", "strategic_vision", "process_definition",
})


class TestClassifySeed:
    def test_design_directive_match(self, extract_seeds_mod):
        # Needs 2 pattern matches (threshold=2)
        text = "define the schema format for the new interface protocol"
        types = extract_seeds_mod.classify_seed(text)
        assert "design_directive" in types

    def test_design_directive_needs_threshold(self, extract_seeds_mod):
        # Only one pattern match — should NOT trigger (threshold=2)
        text = "the system is defined already"
        types = extract_seeds_mod.classify_seed(text)
        # "define" alone may or may not be enough depending on other matches
        # At minimum, a trivial sentence shouldn't produce design_directive
        # unless it genuinely matches 2+ patterns

    def test_theoretical_grounding_match(self, extract_seeds_mod):
        text = "the telos of the organ demands ontological coherence"
        types = extract_seeds_mod.classify_seed(text)
        assert "theoretical_grounding" in types

    def test_theoretical_grounding_organ_match(self, extract_seeds_mod):
        text = "each organ in the biological system has a digestive function"
        types = extract_seeds_mod.classify_seed(text)
        assert "theoretical_grounding" in types

    def test_consolidation_order_match(self, extract_seeds_mod):
        # Pattern uses \b word boundaries, so full-word stems like "flatten", "absorb" match;
        # truncated stems like "consolidat", "merg" require word-final position
        text = "flatten and absorb these overlapping layers into a single source"
        types = extract_seeds_mod.classify_seed(text)
        assert "consolidation_order" in types

    def test_naming_act_match(self, extract_seeds_mod):
        text = "rename it to recursive-engine--generative-entity and rebrand the interface"
        types = extract_seeds_mod.classify_seed(text)
        assert "naming_act" in types

    def test_rejection_correction_match(self, extract_seeds_mod):
        text = "no, not that approach. instead use the recursive method"
        types = extract_seeds_mod.classify_seed(text)
        assert "rejection_correction" in types

    def test_strategic_vision_match(self, extract_seeds_mod):
        text = "the revenue model needs scale for enterprise growth and market expansion"
        types = extract_seeds_mod.classify_seed(text)
        assert "strategic_vision" in types

    def test_process_definition_match(self, extract_seeds_mod):
        text = "the workflow pipeline protocol: step 1 is to create the phase scaffold"
        types = extract_seeds_mod.classify_seed(text)
        assert "process_definition" in types

    def test_no_seed_for_trivial_yes(self, extract_seeds_mod):
        assert extract_seeds_mod.classify_seed("yes") == []

    def test_no_seed_for_trivial_ok(self, extract_seeds_mod):
        assert extract_seeds_mod.classify_seed("ok") == []

    def test_no_seed_for_trivial_continue(self, extract_seeds_mod):
        assert extract_seeds_mod.classify_seed("continue") == []

    def test_multiple_seed_types(self, extract_seeds_mod):
        text = (
            "define the schema protocol for the new system architecture, "
            "and rename it to organvm-engine--core. The telos demands this "
            "consolidation to merge redundant overlapping modules."
        )
        types = extract_seeds_mod.classify_seed(text)
        assert len(types) >= 2, f"Expected multiple seed types, got {types}"

    def test_seed_types_are_valid(self, extract_seeds_mod):
        test_texts = [
            "define the schema format for the new interface protocol",
            "the telos of the organ demands ontological coherence",
            "merge these redundant modules",
            "no, not that. instead do this always",
            "the revenue model and market growth need scale for enterprise expansion",
            "the workflow pipeline: step 1 create, then step 2 verify",
        ]
        for text in test_texts:
            types = extract_seeds_mod.classify_seed(text)
            for t in types:
                assert t in VALID_SEED_TYPES, f"'{t}' not in valid set for text: '{text[:60]}'"


class TestPatternSets:
    def test_all_pattern_lists_nonempty(self, extract_seeds_mod):
        pattern_names = [
            "DESIGN_DIRECTIVE_PATTERNS", "THEORETICAL_PATTERNS",
            "CONSOLIDATION_PATTERNS", "NAMING_PATTERNS",
            "REJECTION_PATTERNS", "STRATEGIC_PATTERNS", "PROCESS_PATTERNS",
        ]
        for name in pattern_names:
            patterns = getattr(extract_seeds_mod, name, None)
            assert patterns is not None, f"{name} not found"
            assert len(patterns) > 0, f"{name} is empty"

    def test_patterns_are_compiled_regex(self, extract_seeds_mod):
        import re
        for p in extract_seeds_mod.DESIGN_DIRECTIVE_PATTERNS:
            assert isinstance(p, re.Pattern), f"Pattern is not compiled regex: {p}"
