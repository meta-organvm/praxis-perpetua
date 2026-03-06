# Plan: Genesis Sweep + Session Intelligence System

## Context

The user has 1,367 AI sessions (3.5GB) across Claude/Gemini/Codex and 79 plan files across 13 projects. The multi-agent session parsing infrastructure is already built (`organvm-engine/src/organvm_engine/session/`). Now the user wants:

1. **Genesis sweep** — collect all plans across the workspace, compare plan vs reality (was it implemented? partially? abandoned?)
2. **Cross-session prompt analysis** — find redundancies, recurring mistakes, and improvable patterns across all prompts
3. **Automatic session review** — hook into session exit to trigger review/prompt-strip/plan-check
4. **Agent file integration** — embed review instructions into CLAUDE.md/GEMINI.md/AGENTS.md at project roots

This plan covers **all four** as a unified "session intelligence" system added to `organvm-engine`.

---

## Part 1: Genesis Sweep — Plan Discovery & Audit

### What exists
- 79 plan files across 13 projects in `~/.claude/plans/` or `<project>/.claude/plans/`
- Plans follow `YYYY-MM-DD-{slug}.md` naming convention
- No Gemini or Codex plan equivalents found (Claude-only feature)

### New module: `organvm_engine/session/plans.py`

```python
@dataclass
class PlanFile:
    path: Path
    project: str          # decoded project path
    slug: str             # from filename
    date: str             # YYYY-MM-DD
    title: str            # first H1 from content
    size_bytes: int
    has_verification: bool  # contains "## Verification" section
    status: str           # "unknown" initially, annotatable

def discover_plans(workspace: Path | None = None) -> list[PlanFile]
def render_plan_inventory(plans: list[PlanFile]) -> str
```

**Discovery logic:**
1. Walk `~/Workspace/**/.claude/plans/*.md` (project-level)
2. Walk `~/.claude/plans/*.md` (global plans)
3. Parse each: extract date from filename, title from first `# ` line, check for verification section
4. Sort by date descending
5. Return `list[PlanFile]`

### New CLI: `organvm session plans`

```
organvm session plans                    # list all plans across workspace
organvm session plans --project X        # filter by project substring
organvm session plans --since YYYY-MM-DD # filter by date
organvm session plans audit              # render plan-vs-reality report scaffold
```

The `audit` subcommand generates a markdown report with each plan listed and empty `Status:` / `Reality:` fields for the user to fill in (or for a future LLM pass to auto-assess by cross-referencing git log).

### Files to create/modify
- **Create:** `organvm_engine/session/plans.py` (~80 lines)
- **Modify:** `organvm_engine/cli/session.py` — add `cmd_session_plans()` handler
- **Modify:** `organvm_engine/cli/__init__.py` — add `plans` subparser under `session`
- **Create:** `organvm_engine/tests/test_session_plans.py` (~30 tests)

---

## Part 2: Cross-Session Prompt Analysis

### New module: `organvm_engine/session/analysis.py`

```python
@dataclass
class PromptStats:
    total_sessions: int
    total_prompts: int
    total_chars: int
    avg_prompt_length: int
    top_opening_words: dict[str, int]   # first 3 words → frequency
    repeated_phrases: list[tuple[str, int]]  # phrase → count (min 3 occurrences)
    agent_breakdown: dict[str, int]     # agent → prompt count

def analyze_prompts(
    sessions: list[AgentSession] | None = None,
    sample_limit: int = 200,
) -> PromptStats
```

**Analysis logic:**
1. Use `discover_all_sessions()` to get session list (or accept pre-filtered)
2. For each session, call `render_any_prompts()` to extract human messages
3. Tokenize into opening phrases (first 3 words normalized)
4. Count repeated multi-word phrases (sliding window, min length 4 words, min 3 occurrences)
5. Compute basic stats

This is intentionally lightweight — no NLP dependencies, just string counting. The output is a report the user reviews, not an automated action system.

### New CLI: `organvm session analyze`

```
organvm session analyze                  # full analysis (sampled, ~200 sessions)
organvm session analyze --agent claude   # filter by agent
organvm session analyze --full           # all sessions (slow, ~1367)
organvm session analyze --output report.md
```

### Files to create/modify
- **Create:** `organvm_engine/session/analysis.py` (~120 lines)
- **Modify:** `organvm_engine/cli/session.py` — add `cmd_session_analyze()`
- **Modify:** `organvm_engine/cli/__init__.py` — add `analyze` subparser
- **Create:** `organvm_engine/tests/test_session_analysis.py` (~20 tests)

---

## Part 3: Session Exit Hook

### How Claude Code hooks work
Claude Code supports hooks via `settings.json` under the `hooks` key. The existing `template-interceptor.sh` at `~/.claude/scripts/` demonstrates the pattern — a bash script that receives JSON on stdin and outputs a JSON decision.

However, Claude Code hooks fire on **tool calls** (pre/post), not on session lifecycle events (start/end). There is no native "session exit" hook.

### Practical alternative: Shell integration

Instead of a Claude-internal hook, use **shell integration** — a zsh function that wraps the `claude` command:

```bash
# In ~/.zshrc or ~/.claude/scripts/session-review.sh (sourced by .zshrc)
claude-review() {
    # Run claude normally, capture exit
    command claude "$@"
    local exit_code=$?

    # After session ends, trigger review of the most recent session
    if [[ $exit_code -eq 0 ]]; then
        # Quick prompt strip + summary (non-blocking, background)
        organvm session review --latest --project "$(pwd)" &
    fi
    return $exit_code
}
alias claude='claude-review'
```

### New CLI: `organvm session review`

```
organvm session review <session-id>      # review specific session
organvm session review --latest          # review most recent session
organvm session review --latest --project <path>  # most recent for project
```

**What `review` does:**
1. Find the session (latest or by ID)
2. Extract prompts → count, list opening lines
3. Check if any plans exist for this project → flag unimplemented ones
4. Print a concise summary:
   ```
   Session Review: abc12345 (2026-03-06, 47 min, 23 messages)
   Agent: claude | Project: meta-organvm

   Prompts (12 human):
     1. "did you implement this as a function..."
     2. "we need to arrive at the best method..."
     ...

   Plans in this project (3):
     2026-03-06-living-data-organism.md ← same day
     2026-03-06-e2g-review-5.md ← same day

   Export: organvm session export abc12345 --slug <your-slug>
   ```

### Files to create/modify
- **Create:** `~/.claude/scripts/session-review.sh` (~20 lines, shell wrapper)
- **Modify:** `organvm_engine/cli/session.py` — add `cmd_session_review()`
- **Modify:** `organvm_engine/cli/__init__.py` — add `review` subparser
- **Create:** `organvm_engine/tests/test_session_review.py` (~15 tests)

---

## Part 4: Agent File Integration

### Approach
Add a `SESSION_REVIEW_SECTION` to the contextmd templates that gets injected into CLAUDE.md / GEMINI.md / AGENTS.md during `organvm context sync`.

### New template in `contextmd/templates.py`

```python
SESSION_REVIEW_SECTION = """\
## Session Review Protocol

At the end of each session that produces or modifies files:
1. Run `organvm session review --latest` to get a session summary
2. Check for unimplemented plans: `organvm session plans --project .`
3. Export significant sessions: `organvm session export <id> --slug <slug>`

Transcripts are on-demand (never committed):
- `organvm session transcript <id>` — conversation summary
- `organvm session transcript <id> --unabridged` — full audit trail
- `organvm session prompts <id>` — human prompts only
"""
```

This gets appended inside the `<!-- ORGANVM:AUTO:START -->` block for repo-level context files.

### Files to modify
- **Modify:** `organvm_engine/contextmd/templates.py` — add `SESSION_REVIEW_SECTION`
- **Modify:** `organvm_engine/contextmd/generator.py` — include session review section in repo-level generation
- Next `organvm context sync` propagates to all ~100 repos

---

## Implementation Order

1. **`session/plans.py`** + CLI + tests (genesis sweep — highest user priority)
2. **`cli/session.py` review command** + shell wrapper (immediate daily utility)
3. **`session/analysis.py`** + CLI + tests (prompt analysis)
4. **`contextmd/templates.py`** integration (propagation to agent files)

## Files Summary

### Create (6 files)
| File | Lines (est) | Purpose |
|------|-------------|---------|
| `src/organvm_engine/session/plans.py` | ~80 | Plan discovery and inventory |
| `src/organvm_engine/session/analysis.py` | ~120 | Cross-session prompt analysis |
| `tests/test_session_plans.py` | ~100 | Plan discovery tests |
| `tests/test_session_analysis.py` | ~80 | Prompt analysis tests |
| `tests/test_session_review.py` | ~60 | Review command tests |
| `~/.claude/scripts/session-review.sh` | ~20 | Shell wrapper for auto-review |

### Modify (4 files)
| File | Change |
|------|--------|
| `src/organvm_engine/cli/__init__.py` | Add `plans`, `analyze`, `review` subparsers |
| `src/organvm_engine/cli/session.py` | Add `cmd_session_plans()`, `cmd_session_analyze()`, `cmd_session_review()` |
| `src/organvm_engine/contextmd/templates.py` | Add `SESSION_REVIEW_SECTION` |
| `src/organvm_engine/contextmd/generator.py` | Include session review section |

### Reuse (existing code)
| Function | File | Used by |
|----------|------|---------|
| `discover_all_sessions()` | `session/agents.py` | analysis, review |
| `render_any_prompts()` | `session/parser.py` | analysis, review |
| `parse_any_session()` | `session/parser.py` | review |
| `find_session()` | `session/parser.py` | review |
| `agent_summary()` | `session/agents.py` | analysis |
| `REPO_SECTION` template pattern | `contextmd/templates.py` | agent file integration |
| `sync_all()` injection pattern | `contextmd/sync.py` | agent file integration |

## Verification

1. **Plans discovery:** `organvm session plans` — should list 79 plans across 13 projects
2. **Plans audit:** `organvm session plans audit` — should render markdown scaffold
3. **Review:** `organvm session review --latest` — should summarize most recent session
4. **Analysis:** `organvm session analyze --agent claude` — should produce stats
5. **Tests:** `pytest organvm-engine/tests/test_session_plans.py test_session_analysis.py test_session_review.py -v`
6. **Context sync dry-run:** `organvm context sync --dry-run` — should show session review section in output
7. **Shell wrapper:** Source `~/.claude/scripts/session-review.sh` and verify alias works
