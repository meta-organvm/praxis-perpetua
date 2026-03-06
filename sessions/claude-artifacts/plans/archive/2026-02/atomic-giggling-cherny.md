# Evaluation-to-Growth Review: meta-organvm

## Context

The meta-organvm superproject has grown to ~7,700 LOC across 5 Python packages with 216+ passing tests, governing 103 repos across 8 organs. The codebase is architecturally sound — clean separation of concerns, strong type hints, good docstrings — but has accumulated technical debt in three areas: **untested critical paths** (CLI), **duplicated truth sources** (organ mappings, schema enums), and **silent error handling** that masks data corruption. This review identifies 12 concrete issues and proposes a phased implementation plan.

---

## Phase 1: Evaluation

### 1.1 Critique — Strengths

| Strength | Evidence |
|----------|----------|
| Clean module boundaries | 7 engine packages, each single-responsibility |
| Strong type hints | Python 3.11+ `\|` union syntax throughout |
| Elegant state machine | `state_machine.py` — 46 lines, no hidden state, clear transition matrix |
| Robust dependency validation | DFS cycle detection + back-edge enforcement in `dependency_graph.py` |
| Good test design | Shared conftest fixtures, 192 engine + 24 MCP tests |
| Dry-run everywhere | All mutating CLI commands support `--dry-run` |
| Professional MCP server | 16 tools, clean dispatch table, proper error boundaries |

### 1.2 Critique — Weaknesses

| ID | Severity | Issue | Location |
|----|----------|-------|----------|
| W1 | P0 | No CLI tests — 1017 lines, zero coverage | `organvm-engine/tests/` (missing `test_cli.py`) |
| W2 | P0 | Silent exception swallowing | `audit.py:142-143`, `superproject.py:56-57` |
| W3 | P0 | Circular import workarounds | `contextmd/generator.py:21-24,87-88,166,208` |
| W4 | P1 | Organ mapping fragmentation (3 dicts) | `query.py:6-16`, `superproject.py:17-39` |
| W5 | P1 | Enum duplication (code vs schema) | `validator.py:9-14` vs `schema-definitions/schemas/` |
| W6 | P1 | Fragile substring matching in seed graph | `seed/graph.py:82` |
| W7 | P1 | CLAUDE.md tool count stale (says 13, actually 16) | `CLAUDE.md` (superproject-level) |
| W8 | P2 | Unused imports | `governance/impact.py:9`, `contextmd/generator.py:11` |
| W9 | P2 | Auto-generated CLAUDE.md shows "unknown" for org/edges | Multiple repo CLAUDE.md files |
| W10 | P2 | No integration tests | `organvm-engine/tests/` |
| W11 | P2 | Stub command in alchemia | `alchemia/cli.py:231-234` (`cmd_review`) |
| W12 | P2 | Hardcoded relative path for provenance | `alchemia/cli.py:211` |

### 1.3 Logic Check

- **Contradiction**: `CLAUDE.md` documents 13 MCP tools in 5 groups, but `server.py` defines 16 tools (added `organvm_ci_health`, `organvm_upcoming_deadlines`, `organvm_pitch_status`). Consumers of the docs get wrong expectations.
- **Reasoning gap**: Governance rules loaded from YAML (`superproject.py:42-57`) but never validated against `governance-rules.schema.json`. If YAML is malformed, system silently uses hardcoded defaults.
- **Unsupported assumption**: `validator.py:9` comment "kept in sync with schema-definitions" — no automation enforces this, pure honor system.

### 1.4 Logos (Rational/Structural Appeal)

- **Argument clarity**: The architecture is well-reasoned — registry as SSOT, seeds as contracts, promotion state machine as governance. The logical structure is sound.
- **Evidence quality**: 192 tests provide good evidence of correctness for engine internals. But the CLI (the only user-facing surface) has zero test evidence.
- **Persuasive gap**: The system claims robust governance but silently swallows errors in audit and config loading — undermining the "trustworthy governance" narrative.

### 1.5 Pathos (Emotional/User Experience)

- **Current tone**: Developer-facing, pragmatic, well-documented. CLAUDE.md files give AI assistants solid context.
- **Connection gap**: Auto-generated CLAUDE.md files showing `unknown` for org/edges feel broken rather than informative. Users encountering these lose trust in the generation system.
- **Engagement**: The MCP server is the most engaging surface — real-time system querying. But error messages are generic (`"Error: {type(e).__name__}: {e}"`) rather than actionable.

### 1.6 Ethos (Credibility)

- **Expertise signals**: Type hints, dataclass results, schema definitions, proper CLI argparse — all signal professional engineering.
- **Trust gaps**: Silent `except: pass` patterns (audit.py, superproject.py) and duplicated enums undermine confidence in data integrity.
- **Missing authority markers**: No CLI tests means no CI gate on the primary user interface. No integration tests means cross-module contracts are untested.

---

## Phase 2: Reinforcement

Resolve contradictions and strengthen coherence.

### R1. Fix silent exception handling (P0, Size: S)

**Files:**
- `organvm-engine/src/organvm_engine/governance/audit.py:142-143`
- `organvm-engine/src/organvm_engine/git/superproject.py:56-57`

**Action:**
```python
# audit.py:142-143 — replace silent pass with warning
except ValueError:
    result.warnings.append(f"{organ_key}/{name}: malformed last_validated date")

# superproject.py:56-57 — replace silent pass with logging
except Exception as e:
    import warnings
    warnings.warn(f"Failed to load governance-config.yaml: {e}")
```

### R2. Resolve circular imports in contextmd (P0, Size: M)

**Files:**
- `organvm-engine/src/organvm_engine/contextmd/generator.py`

**Action:** The local imports at lines 21-24, 87-88, 166, 208 are all importing from `registry.query` and `contextmd.templates`. These aren't true circular dependencies — `templates.py` has no imports from `generator.py`, and `query.py` doesn't import from `contextmd`. Move all imports to module level.

### R3. Update stale documentation (P1, Size: S)

**Files:**
- `CLAUDE.md` (superproject root) — update MCP tool count from 13 to 16, add the 3 new tools to the table

### R4. Clean up unused imports (P2, Size: S)

**Files:**
- `organvm-engine/src/organvm_engine/governance/impact.py:9` — remove `from typing import Any`
- `organvm-engine/src/organvm_engine/contextmd/generator.py:11` — remove `from typing import Any`

---

## Phase 3: Risk Analysis

### 3.1 Blind Spots

| Blind Spot | Impact | Mitigation |
|------------|--------|------------|
| No error recovery for partial git sync | Interrupted `sync-organ` leaves submodule pointers inconsistent | Add pre-sync state snapshot and rollback |
| No schema migration strategy | registry-v2.json schema changes break all consumers silently | Document migration protocol; add schema_version check on load |
| Governance YAML not validated against schema | Malformed governance config → silent fallback to defaults | Validate on load or at least warn |
| Dashboard has no auth | Localhost info exposure | Document as known limitation; low risk for dev tool |
| registry-v2.json is SPOF | Corruption = full system failure | Add registry backup before mutations; validate before write |

### 3.2 Shatter Points

| Vulnerability | Severity | Preventive Measure |
|---------------|----------|-------------------|
| Organ mapping drift across 3 dicts | High | Consolidate to single source (see G1) |
| Enum drift between code and schemas | High | Load from schemas at runtime (see G2) |
| MCP server swallows all errors generically | Medium | Add structured error responses with tool name + context |
| Seed graph substring matching | Medium | Fix matching logic (see G3) |
| CLI has zero test coverage | Critical | Add CLI tests (see G4) |

---

## Phase 4: Growth

### G1. Consolidate organ mappings (P1, Size: M)

**New file:** `organvm-engine/src/organvm_engine/organ_config.py`

**Action:** Create single source of truth for all organ key/directory/registry mappings:
```python
# organ_config.py — canonical organ definitions
ORGANS = {
    "I":    {"dir": "organvm-i-theoria",    "registry_key": "ORGAN-I",       "org": "ivviiviivvi"},
    "II":   {"dir": "organvm-ii-poiesis",   "registry_key": "ORGAN-II",      "org": "omni-dromenon-machina"},
    "III":  {"dir": "organvm-iii-ergon",     "registry_key": "ORGAN-III",     "org": "labores-profani-crux"},
    ...
    "META": {"dir": "meta-organvm",         "registry_key": "META-ORGANVM",  "org": "meta-organvm"},
}

def organ_dir_map() -> dict[str, str]: ...
def registry_key_map() -> dict[str, str]: ...
def organ_aliases() -> dict[str, str]: ...
```

**Then update:**
- `registry/query.py` — import `organ_aliases` from `organ_config`
- `git/superproject.py` — import `organ_dir_map`, `registry_key_map` from `organ_config`
- `seed/discover.py` — import from `organ_config` if it has its own mapping

### G2. Load enums from schema definitions (P1, Size: M)

**Files:**
- `organvm-engine/src/organvm_engine/registry/validator.py:9-14`
- `schema-definitions/schemas/registry-v2.schema.json`

**Action:** Replace hardcoded sets with a loader function:
```python
def _load_schema_enums() -> dict[str, set[str]]:
    """Load enum values from registry-v2 JSON schema."""
    schema_path = Path(__file__).parents[3] / "schema-definitions/schemas/registry-v2.schema.json"
    # Fallback to env var or known paths
    ...
```

**Fallback:** If schema file unavailable (e.g., schema-definitions not installed), fall back to current hardcoded values with a warning. This keeps the package functional standalone.

### G3. Fix seed graph substring matching (P1, Size: S)

**File:** `organvm-engine/src/organvm_engine/seed/graph.py:82`

**Action:** Replace `source not in producer` with proper matching:
```python
# Before:
if source and source not in producer:
    continue

# After:
if source:
    # Match on org prefix or full identity
    producer_prefix = producer.split("/")[0] if "/" in producer else ""
    if source != producer_prefix and source not in producer.split("/"):
        continue
```

### G4. Add CLI test suite (P0, Size: L)

**New file:** `organvm-engine/tests/test_cli.py`

**Approach:** Use `subprocess.run` or `argparse` direct invocation to test:
- All 12 command groups dispatch correctly
- `--help` works for every subcommand
- `--dry-run` flags are respected
- Error cases (missing args, bad organ names) produce clean error messages
- Registry commands with mock registry fixture

**Target:** 30-40 tests covering all command groups. Use `tmp_path` fixtures and mock registry data (reuse patterns from `conftest.py`).

### G5. Fix auto-generated CLAUDE.md "unknown" values (P2, Size: M)

**Files:**
- `organvm-engine/src/organvm_engine/contextmd/generator.py` — `generate_repo_section()`
- `organvm-engine/src/organvm_engine/contextmd/sync.py`

**Action:** The `unknown` values appear because seed.yaml edges don't always have `target`/`artifact` fields populated, or the `org` field isn't being resolved from registry. Trace the data flow:
1. Check how `sync.py` passes `org` to `generate_repo_section()`
2. If `org` is not in seed.yaml, fall back to registry lookup
3. For edges, use edge `type` when `artifact` is missing rather than "unknown"

---

## Implementation Order

| Step | Item | Size | Dependencies |
|------|------|------|-------------|
| 1 | R1: Fix silent exception handling | S | None |
| 2 | R2: Resolve circular imports | M | None |
| 3 | R4: Clean unused imports | S | None |
| 4 | R3: Update stale CLAUDE.md | S | None |
| 5 | G3: Fix seed graph matching | S | None |
| 6 | G1: Consolidate organ mappings | M | None (but R2 first is cleaner) |
| 7 | G2: Load enums from schemas | M | Needs schema-definitions accessible |
| 8 | G4: Add CLI tests | L | Steps 1-6 done first (test clean code) |
| 9 | G5: Fix CLAUDE.md unknown values | M | G1 helpful but not required |

Steps 1-5 can be done in a single session. Steps 6-7 form a natural second batch. Steps 8-9 are larger efforts.

## Verification

After implementation:

1. **Run existing tests** — `pytest organvm-engine/tests/ -v` (expect 192+ pass, 0 fail)
2. **Run MCP tests** — `pytest organvm-mcp-server/tests/ -v` (expect 24+ pass)
3. **Run linting** — `ruff check organvm-engine/src/` (expect clean)
4. **Validate registry** — `organvm registry validate` (expect pass)
5. **Run governance audit** — `organvm governance audit` (verify warnings now surface, not silently swallowed)
6. **Test CLI help** — `organvm --help`, `organvm registry --help`, etc. (verify all commands listed)
7. **Re-run context sync** — `organvm context sync --dry-run` (verify no more "unknown" in output)
8. **New CLI tests** — `pytest organvm-engine/tests/test_cli.py -v` (if G4 implemented)
