# Prompt Archaeology Corpus — Foundation

**Date:** 2026-04-04
**Scope:** Scaffolding for 48-hour archaeology pass across all session surfaces.

---

## What Exists (Pre-Archaeology)

### Already Canonized Patterns

**Session Protocol (8 phases):**
- SEED → REDIRECT → SPECIFY → CONNECT → PORTAL → NEST → AUDIT → HANDOFF

**Design Grammar (9 phases):**
- DEFINE → DISCOVER → EXTRACT → ALIGN → STRUCTURE → SYNC → VALIDATE → DOCUMENT → TRANSFORM

**Close Protocol (12 steps):**
- Full checklist in `close-protocol.yaml`

**Operational Vocabulary (12 categories, 7 paired patterns):**
- Defined in `library/vocabulary/vocabulary.yaml`

**Frameworks & Principles (22 abstractions):**
- Including 11 uncategorized "natural kin" patterns

---

## What Remains to Extract

The memory file explicitly notes:
- **Gap:** Unknown number of unique prompts remain in raw history
- **Estimate:** 50-200 unique patterns likely exist in the 48-hour window
- **Source surfaces not yet catalogued:**
  - Raw session transcripts (JSONL)
  - Gemini project directories
  - Codex sessions
  - Unformalized plan files (agent sub-plans)

---

## Archaeology Framework

### Sources to Mine
1. `~/.claude/` — Claude transcript files
2. `~/.local/share/gemini/antigravity/` — Gemini sessions
3. `~/.codex/` — Codex sessions
4. `.claude/plans/` — Plan files in each workspace
5. `.gemini/plans/` — Gemini plan files

### Extraction Targets
- Unique prompts not in operational vocabulary
- Recurring sequences revealing workflow grammar
- Domain-specific variants of general patterns
- Raw prompts better than their formalized versions
- Prompts that failed (anti-patterns worth preserving)

---

## Status

This artifact establishes the scaffold. Full archaeology requires:
- Dedicated session (noted as "48-hour window")
- Digestion logic: parse all session files → extract → classify → produce corpus

**Memory file should be updated from "needed" to "scaffolded" until dedicated pass completes.**

---

*Artifact created: 2026-04-04*