# Evaluation-to-Growth Review: ORGAN-VII Data Artifact Generation

## Context

Post-implementation review of the ORGAN-VII data artifact generation that made Kerygma the third complete organ (5/5 produce edges). Applies the Evaluation-to-Growth framework across all 3 repos: announcement-templates, distribution-strategy, social-automation.

**Mode**: Autonomous | **Format**: Markdown Report + Structured Checklist

---

## Phase 1: Evaluation

### 1.1 Critique

**Strengths**
- S1: Consistent architecture — all 3 repos follow identical `build_*()` + `export_all()` + `main()` pattern matching ORGAN-VI reference
- S2: Strong code reuse — imports TemplateEngine, QualityChecker, ChannelRegistry, Platform enum etc. rather than reimplementing
- S3: All 253 tests pass (231 existing + 22 new), zero regressions
- S4: validate.sh works end-to-end: 3 passed, 1 skipped
- S5: JSON artifacts include metadata headers (organ, generated_at, repo) enabling machine consumption
- S6: No new dependencies added — stdlib + existing package deps only
- S7: social-automation's POSSE manifest is excellent introspective documentation (resilience stack, env vars, config fields, deduplication strategy)

**Weaknesses**
- W1: **Private function coupling** — `data_export.py` imports `_sample_context()` from `cli.py` (underscore-prefixed = private API)
  - File: `announcement-templates/kerygma_templates/data_export.py:5`
- W2: **Redundant I/O** — `distribution-strategy/data_export.py` reads YAML files twice: once via `yaml.safe_load()`, again via `ChannelRegistry.from_yaml()` / `DistributionCalendar.from_yaml()`
  - File: `distribution-strategy/kerygma_strategy/data_export.py:35-50`
- W3: **6 quality failures + 4 warnings unexplained** — `template-registry.json` reports `"failed": 6, "warnings": 4` out of 432 checks; no breakdown of which templates/channels fail or why
  - File: `announcement-templates/data/template-registry.json:316-319`
- W4: **Test fixtures as production data source** — distribution-strategy exports from `tests/fixtures/sample_channels.yaml` / `sample_calendar.yaml`. If fixtures change for test purposes, production artifacts silently change
  - File: `distribution-strategy/kerygma_strategy/data_export.py:23`
- W5: **`__init__.py` not updated** — none of the 3 `__init__.py` files export `data_export`, so `from kerygma_templates import data_export` doesn't work. Deliberate or oversight?
- W6: **CLAUDE.md not updated** — ORGAN-VII superproject CLAUDE.md doesn't mention `data/` artifacts, export CLIs (`announce-export`, `distrib-export`, `social-export`), or `validate.sh`
- W7: **Empty string vs null** — `distribution-plan.json` has `"end_date": ""` for events without end dates; should be `null` for proper JSON semantics
- W8: **Exception swallowing** — `build_quality_summary()` catches all exceptions with bare `except Exception` and silently counts them as failures with no logging
  - File: `announcement-templates/kerygma_templates/data_export.py:78-80`
- W9: **CHANGELOG gap** — distribution-strategy jumps from `[0.1.0]` to `[0.3.0]` with no `[0.2.0]` entry (the 0.2.0 release predated this work but was never documented in CHANGELOG)

### 1.2 Logic Check

| Issue | Severity | Location |
|-------|----------|----------|
| **Cross-repo channel inconsistency**: announcement-templates knows 6 channels (incl. twitter with limit 280), distribution-strategy knows 3 (from fixtures), social-automation knows 6 (from Platform enum). No single source of truth | Medium | All 3 data artifacts |
| **Dual status terminology**: `SyndicationStatus` uses published/failed, `delivery_statuses` uses success/failure for the same concept. Both appear in delivery-log.json | Low | `social-automation/data/delivery-log.json:49-59` |
| **`end_date` type inconsistency**: YAML fixture stores dates as strings, `DistributionCalendar` parses them to `datetime.date`, but `str()` in data_export converts back to string. Works but fragile chain | Low | `distribution-strategy/kerygma_strategy/data_export.py:60` |

### 1.3 Logos Review (Rational Appeal)

- **Argument clarity**: HIGH — each artifact clearly documents what its repo produces, in machine-readable format
- **Evidence quality**: HIGH — template-registry.json enumerates all 16 templates with exact variables and channels; POSSE manifest lists every env var and module path
- **Persuasive strength**: MEDIUM — the quality_summary showing 6 failures weakens the claim of a "complete" organ. A passing organ should have 0 failures in its own quality checks

### 1.4 Pathos Review

N/A — machine-readable JSON artifacts, not audience-facing content.

### 1.5 Ethos Review (Credibility)

- **Expertise signals**: Proper semver, Keep-a-Changelog format, seed.yaml contracts, consistent CLI entry points
- **Trust gaps**: (a) unexplained quality failures, (b) CLAUDE.md doesn't reflect current capabilities, (c) no CI enforcement of artifact freshness
- **Authority markers**: validate.sh proves all repos work together; test counts are transparent and verified

---

## Phase 2: Reinforcement

### Synthesis — Fixes Required

| # | Fix | Files | Priority |
|---|-----|-------|----------|
| F1 | Extract `_sample_context()` to a shared location or make it a public function `sample_context()` | `announcement-templates/kerygma_templates/cli.py`, `data_export.py` | HIGH |
| F2 | Investigate the 6 quality check failures and either fix templates or document them as known limitations in the artifact | `announcement-templates/kerygma_templates/data_export.py` | HIGH |
| F3 | Use `None` instead of `""` for missing `end_date` in distribution-plan.json | `distribution-strategy/kerygma_strategy/data_export.py:60` | MEDIUM |
| F4 | Update ORGAN-VII CLAUDE.md to document data artifacts, export CLIs, and validate.sh | `organvm-vii-kerygma/CLAUDE.md` | MEDIUM |
| F5 | Eliminate redundant YAML reads — use `ChannelRegistry.from_yaml()` and access data through the registry, or load raw YAML once and pass to both | `distribution-strategy/kerygma_strategy/data_export.py` | LOW |
| F6 | Add per-failure detail to quality_summary (which template/channel/check failed) | `announcement-templates/kerygma_templates/data_export.py` | LOW |

---

## Phase 3: Risk Analysis

### 3.1 Blind Spots

| Blind Spot | Impact | Mitigation |
|------------|--------|------------|
| **Artifact staleness** — committed JSON artifacts drift when source data changes (templates added, fixtures modified). No CI enforces regeneration | Consumers read outdated data | Add CI step: regenerate → diff → fail if changed (pattern: essay-pipeline CI for public-process/data/) |
| **Fixture = production** — `tests/fixtures/sample_channels.yaml` serves double duty as test fixture AND production data source. Changing test data silently changes the artifact | Unexpected production artifact changes | Move production config to a dedicated `config/` directory separate from test fixtures |
| **No downstream consumers yet** — artifacts fulfill produce edges on paper but nothing actually reads them. Completeness metric may be hollow | False confidence in system integration | Track actual consumption in ORGAN-IV orchestration |

### 3.2 Shatter Points

| Vulnerability | Severity | Prevention |
|---------------|----------|------------|
| `_sample_context()` rename/removal breaks data_export at import time | HIGH | F1: make it public or extract to shared module |
| `ChannelRegistry` has no public iteration API — data_export works around this by reading raw YAML. If YAML format changes but registry code adapts, data_export breaks | MEDIUM | Add `list_all()` method to ChannelRegistry or always use raw YAML consistently |
| validate.sh succeeds even with 6 quality failures because `build_quality_summary` doesn't raise on failures | MEDIUM | Decide: should quality failures be blocking? If yes, add a threshold check |
| `str(ev_data.get("end_date", ""))` produces `"None"` string if someone changes fixture to use Python None | LOW | Use explicit null check: `str(v) if v else None` |

---

## Phase 4: Growth

### 4.1 Bloom — Emergent Insights

1. **Cross-organ artifact index** — the superproject could maintain a `data/artifact-manifest.json` listing all data files, their types, and which produce edges they fulfill. ORGAN-IV could consume this instead of parsing individual seed.yaml files.

2. **Artifact drift CI** — a single CI job in the superproject's `.github/` that runs `validate.sh` and additionally regenerates all artifacts, diffing against committed versions. Pattern already exists in essay-pipeline.

3. **Unified platform registry** — a single YAML file defining all supported platforms (mastodon, discord, bluesky, ghost, linkedin, twitter) with their limits, env vars, and status (active/deprecated). Consumed by all 3 repos. Eliminates the cross-repo inconsistency.

4. **Quality dashboard** — the template-registry.json quality_summary could feed into a system health dashboard, tracking quality trends across template versions.

### 4.2 Evolve — Implementation Plan

**Immediate fixes (this session):**

1. **F1: Fix private function coupling**
   - Rename `_sample_context()` → `sample_context()` in `cli.py`
   - Update import in `data_export.py`

2. **F2: Investigate quality failures**
   - Run quality checks with verbose output to identify which 6 template/channel combos fail
   - Add `failure_details` list to quality_summary in the artifact

3. **F3: Fix null handling**
   - Change `str(ev_data.get("end_date", ""))` → `str(ev_data["end_date"]) if ev_data.get("end_date") else None`

4. **F4: Update CLAUDE.md**
   - Add "Data Artifacts" section to ORGAN-VII CLAUDE.md documenting:
     - The 5 artifacts and their paths
     - The 3 export CLI commands
     - validate.sh usage
     - How to regenerate artifacts

**Deferred (separate PR):**
- F5: Eliminate redundant YAML reads (low priority, no behavioral impact)
- F6: Per-failure quality detail (nice-to-have)
- Artifact drift CI (needs .github submodule changes)
- Unified platform registry (cross-repo architectural change)

---

## Verification

After implementing fixes F1-F4:
1. `cd organvm-vii-kerygma && ./validate.sh` — 3 passed, 1 skipped
2. All 253 tests still pass
3. `template-registry.json` quality_summary includes `failure_details` array
4. `distribution-plan.json` shows `null` (not `""`) for events without end_date
5. CLAUDE.md includes data artifact documentation
6. `grep -r "_sample_context" announcement-templates/` returns 0 results (no private imports)

## Critical Files

| File | Action |
|------|--------|
| `announcement-templates/kerygma_templates/cli.py` | Rename `_sample_context` → `sample_context` |
| `announcement-templates/kerygma_templates/data_export.py` | Update import, add failure_details to quality_summary |
| `distribution-strategy/kerygma_strategy/data_export.py` | Fix null handling for end_date |
| `organvm-vii-kerygma/CLAUDE.md` | Add Data Artifacts section |
| All 3 `data/*.json` | Regenerate after fixes |
