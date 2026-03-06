# Meta-Organvm Project Memory

## Key Facts
- **Workspace:** ~/Workspace/meta-organvm/ (git superproject with 8 submodules)
- **Registry:** organvm-corpvs-testamentvm/registry-v2.json (2217 lines, 103 repos)
- **Engine tests:** 590 passing (organvm-engine), 81 passing (organvm-mcp-server), 31 passing (system-dashboard), 15 passing (schema-definitions), 136 passing (alchemia-ingestvm) — total 853
- **organ_config.py:** Single source of truth for organ key/dir/registry mappings (added in evaluation-to-growth review)
- **Python venv:** .venv/ at project root; activate before running any CLI
- **CLI:** `organvm` with 13 subcommands (registry, governance, seed, metrics, dispatch, git, deadlines, ci, omega, pitch, status, context, session); session has 10 subcommands (list, projects, agents, show, export, transcript, prompts, plans, analyze, review)

## Registry Structure
- Top-level: version, schema_version, summary, organs (dict by key), local_repos_migration, etc.
- Each organ: name, description, repositories (array of repo objects)
- Repo fields: name, org, status, public, description, dependencies, promotion_status, tier, last_validated, note, implementation_status, ci_workflow, platinum_status, revenue_model, revenue_status

## Omega Scorecard
- `_KNOWN_MET` dict in scorecard.py: {5, 6, 8, 13} — manually-confirmed criteria
- Criteria #5, #6, #8, #13 are MET (hardcoded); #1/#3/#9/#17 are auto-assessed
- Tests in test_omega.py hardcode expected `met_count=4` — update when flipping criteria
- Snapshot written to corpus: data/omega/omega-status-{date}.json
- Soak test running since 2026-02-16, day 16/30 as of 2026-03-04; auto-flips #1, #3, #17 on ~Mar 18

## Pitch Deck System
- `organvm pitch sync --organ ORGAN-I` generates HTML pitch decks
- Writes to each repo's docs/pitch/index.html
- Skips infrastructure/archive tiers and bespoke decks (no PITCH_MARKER)

## Promotion Pipeline
- Valid transitions: LOCAL→CANDIDATE→PUBLIC_PROCESS→GRADUATED→ARCHIVED
- Promotable criteria: ci_workflow + platinum_status + implementation_status=ACTIVE

## Architecture Notes
- **organ_config.py** is the canonical source for all organ mappings; `query.py`, `superproject.py`, `discover.py` all derive from it
- **validator.py** loads enums from `schema-definitions/schemas/registry-v2.schema.json` at import time, falls back to hardcoded values
- **contextmd/generator.py** imports are module-level (no circular deps despite earlier local-import pattern)
- **seed/graph.py** source matching uses org-prefix comparison, not substring `in`
- **MCP server** has 17 tools (16 original + `organvm_organism`), dispatch table in `server.py`
- **seed/graph.py** handles both string and dict produces/consumes entries (fixed in E2G-2 review)
- **MCP server CI** at `organvm-mcp-server/.github/workflows/ci.yml` (added in E2G-2)
- **Ruff** configured in engine `pyproject.toml` (line-length=100, py311, E/F/W/I rules); pre-existing lint issues in contextmd/sync.py, omega/scorecard.py, organ_config.py not yet fixed
- **Pyright** configured in engine `pyproject.toml` (basic mode, py311); `py.typed` marker present; 0 errors
- **CLI** is now a `cli/` package (15 modules) — split from 1072-line monolith in E2G-3, `organism.py` added in LDO sprint, `session.py` added for praxis-perpetua
- **Standalone scripts** (calculate-metrics.py, propagate-metrics.py) are thin wrappers importing from engine; CI workflow installs engine via git
- **Living Data Organism** (2026-03-06): ALL PHASES COMPLETE. `metrics/gates.py` (gate evaluation), `metrics/organism.py` (SystemOrganism), `metrics/views.py` (consumer projections). Dashboard + MCP server both delegate to organism. CLI: `organvm organism [--organ X] [--repo X] [--json] [--omega]` + `organvm organism snapshot [--write]`. Schema: `system-organism.schema.json`. MCP: `organvm_organism` tool with organ/repo/view params.
- **Ruff** ignore list now includes PLR0911 (too many returns) for gate-dispatch functions

## ORGAN-III → VI/VII Wiring (2026-02-27)
All 23 active ORGAN-III products wired into community (ORGAN-VI) and distribution (ORGAN-VII):
- 23 kerygma profiles in `organvm-vii-kerygma/kerygma-profiles/profiles/`
- 23 community events + 23 taxonomy nodes in `organvm-vi-koinonia/koinonia-db/seed/product_communities.json`
- All 23 seed.yaml files now declare produces/subscriptions edges to ORGAN-VI and ORGAN-VII
- `product.release` / `product.milestone` event types mapped in kerygma pipeline
- Superproject pointers synced and pushed for all three organs (III, VI, VII)

## Sprint History (2026-02-24)
- PROPULSIO MAXIMA: 48 repos promoted LOCAL→CANDIDATE, 83 pitch decks generated, omega 1→2/17
- Counts after sprint: CANDIDATE=68, PUBLIC_PROCESS=12, LOCAL=10, GRADUATED=4, ARCHIVED=9
- E2G Review #1: 9 improvements (R1-R4, G1-G5), 45 new CLI tests, test count 192→237
- E2G Review #2: 7 improvements (G1-G7), test count 237→288; seed graph crash fixed, schema updated, metrics auto-computed (code_files/test_files/repos_with_tests migrated from manual), word count rounding, MCP CI added, ruff configured
- E2G Review #3: 3 tasks — cli.py split into cli/ package (13 modules), pyright added (0 errors in basic mode), standalone scripts deduplicated as thin wrappers
- E2G Review #4 (2026-03-06): 112 new tests across 13 new files + 2 modified. Covers: LDO organism code (MCP+CLI), system-organism schema example, paths.py, organ_config.py, timeseries.py, git/reproduce.py, alchemia transformer+provenance, MCP loader+types, dashboard loader. Total 592 tests.
- E2G Review #5 (2026-03-06): 121 new tests across 12 new files + 3 modified. Covers: alchemia channels (bookmarks, ai_chats, apple_notes), absorb (classifier, name_variants, registry_loader), intake (crawler, manifest_loader), alchemize (deployer, batch_deployer), synthesize, engine governance/audit+rules, MCP seeds/graph/paths. cmd_review stub replaced with working implementation. Total 713 tests, post-selfrev 719.
- Deep structural audit (2026-03-06): 7 bugs fixed across engine+alchemia. F1: compute_vitals reading emptied manual dict (data corruption in vitals.json). F2: provenance.py dict.get returning None not default. F3: classifier Rule 3 incomplete organ_map. F4: bookmarks dead conditional (no pruning). F5: classifier asymmetric MET4 check. F6: engine loader module-level path freeze (DEFAULT_REGISTRY_PATH removed, now calls _default_registry_path()). F7: never-validated repos not flagged stale. Total 722 tests.

## Deployment Status
- public-record-data-scrapper: NOT deployed. Vercel team exists (ivviiviivvi) but no projects.
  Needs: Vercel CLI install, project link, Neon DB, Upstash Redis, env vars.
- Portfolio: Astro site at 4444j99.github.io/portfolio/. Data files in src/data/.

## Application Pipeline
- 1 submitted (Doris Duke AMT, 2026-02-24), 27 staged, 9 drafting
- Pipeline at ~/Workspace/4444J99/application-pipeline/
- Next deadlines: F4 NEH (Mar 6, #58), F14 Bread Loaf (Mar 15, #60), E3 Google Creative (Mar 18, #9)

## GitHub Issue Tracking (2026-03-04)
- **corpus:** 66+ issues (58 omega+sprint + 8 new human-action/deployment issues)
- **engine:** 4 issues (#1 closed, #2-4 good-first-issues)
- Labels: omega, horizon-1..5, blocked:*, sprint, cat:*, urgent:48h, urgent:2wk, action:human-submit, action:human-config
- Human-blocked items tracked as issues: #58 (NEH), #59 (batch submissions), #60 (Bread Loaf), #61 (GitHub Sponsors), #62 (writing pitches), #63 (BETA-SCRAPPER deploy), #64 (Stripe)

## Cross-Agent Handoff (Gemini Session, 2026-03-06)
- **Gemini session produced ~21 files** across meta-organvm (3 governance docs) and Styx (10 deep dives, 1 bibliography, 1 matrix, 1 alchemy, 1 localized SOP, 2 specs)
- **Structural issue discovered:** superproject `.gitignore` allowlist silently ignored `METADOC--research-standards.md` and `SOP--research-to-implementation-pipeline.md`. Gemini believed they were committed — they were not. Fixed by adding to allowlist.
- **10 content gaps identified and fixed (B1-B10):** missing bibliography entries, no STEEP analysis, no scenario planning, no CLA, no backcasting, no 5 Cs synthesis, no genealogical inquiry, no pattern language, no transition design, no verification criteria in specs
- **Governance docs moved to praxis-perpetua/standards/:** `SOP--cross-agent-handoff.md`, `METADOC--research-standards.md`, `SOP--research-to-implementation-pipeline.md`, `SOP--market-gap-analysis.md`, `SOP--structural-integrity-audit.md`
- **Styx research files expanded:** bibliography (62→~200 lines), matrix (46→~200 lines), alchemy (48→~250 lines), both specs (+verification +backcasting), new genealogy doc (~150 lines)
- **Key Gemini behavioral risks:** destructive `open(path, "w")` rewrites (lost intermediate versions), assumes git tracking without verifying `.gitignore`, drops frameworks under long context
- **Lesson:** Always run `git status` after receiving external agent output; verify `.gitignore` allowlists in superprojects

## Praxis-Perpetua (2026-03-06)
- **Process governance corpus** at `meta-organvm/praxis-perpetua/` (8th submodule)
- Docs-only: no code, no build, no tests beyond CI markdown validation
- **standards/**: 6 files (METADOC + 5 SOPs, including new SOP--session-self-critique)
- **templates/**: 4 files (session-review, content-audit, decision-log, handoff-triage)
- **sessions/**: Dated session logs — only review scaffold + prompts extract committed
- **lessons/**: derived-principles.md, agent-behavioral-risks.md, structural-patterns.md
- **templates/**: 5 files (4 original + transcript-style-guide.md)
- SOPs moved from superproject root (anti-pattern: allowlist gitignore required manual entries)
- Registry: META-ORGANVM now has 8 repos (was 7), repository_count updated
- Cross-references in moved SOPs updated from `meta-organvm/METADOC--*` to relative `METADOC--*`

## Session Transcript Architecture (2026-03-06)
- **Committed per session:** review scaffold (`--slug.md`) + prompts extract (`--slug--prompts.md`)
- **On-demand (never committed):** transcripts rendered live from JSONL via CLI
- **Source JSONL:** `~/.claude/projects/<encoded-project-path>/<session-uuid>.jsonl`
- **Two render modes:** `organvm session transcript <id>` (summary) and `--unabridged` (full audit trail with thinking blocks, Write/Edit content, tool results)
- **Referential wires:** review scaffold contains render commands and source path — auditors access transcripts on-demand
- **Key functions:** `render_transcript()` (summary), `render_transcript_unabridged()` (audit), `render_prompts()` (drift/pattern), `_fence()`, `_render_tool_use_unabridged()`
- **Multi-agent dispatch:** `detect_agent()`, `parse_any_session()`, `render_any_transcript()`, `render_any_prompts()` — route by file path
- **Agent-specific:** `parse_gemini_session()`, `render_gemini_transcript()`, `render_gemini_prompts()`, `parse_codex_session()`, `render_codex_transcript()`
- **Discovery:** `agents.py` — `discover_all_sessions()`, `agent_summary()`, per-agent discover functions
- **CLI:** `organvm session agents` (inventory), `--agent` filter on list, 10 subcommands total (7 original + plans, analyze, review)
- **1,367 sessions / 3.5GB** across 3 agents (Claude 829, Gemini 355, Codex 183)
- **Prompts extraction:** filters tool_result-only messages, tracks elapsed time, heuristic categorization (directives/questions/fixes/reviews)
- **Style guide:** shared template at `praxis-perpetua/templates/transcript-style-guide.md`
- **Gemini format:** single JSON with messages array, thoughts as list of subject/description, toolCalls with inline results, tokens tracking
- **Codex format:** JSONL with session_meta + response_item entries, function_call/function_call_output types, reasoning blocks are encrypted (content=None)

## Session Intelligence System (2026-03-06)
- **Plans discovery:** `organvm session plans` — discovers 122 plans across 14 projects (workspace + global + ~/.claude/projects)
- **Plans audit:** `organvm session plans --audit` — markdown scaffold for plan-vs-reality review
- **Session review:** `organvm session review --latest` — session summary, prompt listing, related plans
- **Prompt analysis:** `organvm session analyze` — cross-session stats (opening phrases, repeated patterns, agent breakdown)
- **Shell hook:** `~/.claude/scripts/session-review.sh` — auto-review on clean claude exit (source in .zshrc)
- **Context integration:** `SESSION_REVIEW_SECTION` in `contextmd/templates.py` — injected before AUTO:END in repo-level CLAUDE.md
- **New modules:** `session/plans.py` (~160 lines), `session/analysis.py` (~200 lines)
- **Tests:** 48 new tests (30 plans, 11 analysis, 7 review)
- `discover_plans(include_global=False)` when explicit workspace given — prevents test pollution from real ~/.claude/

## Community Infrastructure (HOSPITIUM + FORUM, 2026-03-04)
- GitHub Discussions enabled on corpus + engine
- Welcome post at corpus discussions/67
- 5 good-first-issues: engine#2 (--format json), engine#3 (type hints), engine#4 (shell completion), corpus#65 (mermaid diagrams), corpus#66 (concordance quickref)
- Issue templates added to corpus: config.yml, documentation.md, sprint-proposal.md
- CONTRIBUTING.md verified present on all flagships + org .github
- Sprint issues closed: #31 (HOSPITIUM), #32 (FORUM)
