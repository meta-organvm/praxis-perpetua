# Plan: ORGAN-VII Evaluation-to-Growth Review + Implementation

## Context

A comprehensive project-wide review of ORGAN-VII (Kerygma) — the POSSE distribution pipeline — using the full Evaluation-to-Growth framework. After deep exploration of all 4 submodules (~30 source files, ~30 test files, 16 templates, 8 CI workflows), this plan delivers:

1. **A Markdown report** (`.github/docs/e2g-review-2026-02.md`) covering all 9 E2G phases
2. **A prioritized implementation plan** with concrete code changes for approved findings

The review examines `announcement-templates`, `social-automation`, `distribution-strategy`, and `kerygma-pipeline` as an integrated system.

---

## Phase 1: Report Delivery

Write `.github/docs/e2g-review-2026-02.md` containing the full 9-phase analysis. Key findings from exploration:

### 1.1 Critique — Strengths
- **Clean architecture**: Three-package separation (templates/social/strategy) + pipeline orchestrator is well-decomposed
- **Zero external dependencies** in announcement-templates (stdlib-only template engine)
- **Resilience stack** is textbook: rate limiter -> circuit breaker -> retry, each in its own module
- **Dry-run by default** across all platform clients — safe experimentation
- **Delivery deduplication** prevents double-posting via persistent DeliveryLog
- **Atomic writes** everywhere (JsonStore, DeliveryLog, RssPoller) using `os.replace`
- **Comprehensive test coverage**: 30 test files, per-module test suites, integration tests
- **Zero TODOs/FIXMEs** in the codebase — unusual maturity signal
- **Consistent patterns**: every client follows `live=False` mock pattern; every store uses atomic writes; every CLI uses argparse with subcommands
- **16 well-structured templates** across 5 categories with 5-channel coverage

### 1.1 Critique — Weaknesses
- **Duplicated Ghost JWT logic**: `ghost.py:_build_jwt()` and `ghost_metrics.py:_build_jwt()` are near-identical (~30 lines each)
- **Duplicated `_build_distributor` logic**: `social-automation/cli.py:_build_distributor()` and `kerygma_pipeline.py:_build_distributor()` are structurally identical
- **No `__init__.py` exports**: all three packages have empty `__init__.py` — no public API surface
- **`ContentPost.created_at` uses mutable default**: `default_factory=datetime.now` is evaluated at instantiation time, which is correct, but the pattern looks like a common pitfall
- **RSS poller doesn't persist `seen_path`** when constructed from pipeline: `poll_for_events()` creates a fresh `RssPoller()` without `seen_path`, losing dedup state between calls
- **seed.yaml missing for `announcement-templates`**: only 3 of 4 submodules have seed.yaml
- **seed.yaml `promotion_status` inconsistency**: seed.yaml says LOCAL but CLAUDE.md says GRADUATED
- **CI workflow path filter too narrow**: `ci-pipeline.yml` only triggers on `kerygma_pipeline.py` and `tests/**` changes, missing the 3 submodule packages

### 1.2 Logic Check
- **Template engine conditional nesting uses repeated regex**: sound but could be slow on deeply nested templates (no practical concern at current scale)
- **`_with_resilience()` retry+circuit breaker interaction**: when both are present, `cb.call(retry, _retryable, config)` passes the `retry` function as the callable to the circuit breaker — this means the circuit breaker wraps the retry function, not individual attempts. This is intentional (retry is innermost) but the indirection is non-obvious
- **Scheduler `publish_entry()` creates `-next` IDs**: only one level of recurrence is tracked. A weekly entry that fires twice would produce `id-next`, then `id-next` would collide on the second fire. The entry_id uniqueness check in `schedule()` would raise `ValueError`

### 1.3 Logos (Rational Appeal)
- Architecture follows the stated POSSE pattern faithfully
- Event-template mapping is complete (17 event types -> 13 unique templates)
- Platform coverage: 4 platforms automated (Mastodon, Discord, Bluesky, Ghost), 2 manual (Twitter, LinkedIn — wise given API volatility)
- Config cascade (YAML -> env) is clean and well-documented

### 1.4 Pathos (Emotional Resonance)
- Template tone is professional but somewhat generic — "Excited to announce" on LinkedIn, "New essay published" on Mastodon
- Templates don't leverage platform-native affordances (Discord embeds with fields are constructed but templates produce plain text; Bluesky facets/links not used)
- No personality or voice differentiation between channels

### 1.5 Ethos (Credibility)
- Zero-dependency template engine signals craftsmanship
- Comprehensive test suite builds trust
- Atomic writes show production awareness
- `live_mode: false` default is responsible engineering
- Missing: no `py.typed` marker for type checker consumers; no `LICENSE` in individual packages (only in .github)

### Phase 2: Reinforcement
- Resolve the duplicated Ghost JWT code
- Resolve the duplicated `_build_distributor` pattern
- Fix the RSS poller statefulness gap in pipeline

### Phase 3: Risk Analysis

#### 3.1 Blind Spots
- **No timeout on circuit breaker in HALF_OPEN state**: if the trial request hangs, the circuit breaker stays in HALF_OPEN indefinitely
- **No max log size**: `DeliveryLog` and `RssPoller` seen_ids grow unbounded. After months of operation, JSON files become large
- **No retry differentiation**: all exceptions trigger retry, including `ValueError` (invalid input) and `CircuitOpenError`. Only transient errors (HTTP 5xx, timeouts) should be retried
- **Ghost JWT has no session refresh**: Bluesky handles session creation, but Ghost JWT is rebuilt per-request (correct but undocumented as intentional)
- **No structured logging**: all output is `print()` — no log levels, no structured JSON, hard to parse in CI
- **`announcement-templates` is tier `archive`**: seed.yaml (in superproject CLAUDE.md) marks it as archive, yet it's actively used by the pipeline

#### 3.2 Shatter Points
- **Critical**: `kerygma_pipeline.py:44` hardcodes `TEMPLATES_DIR` relative to `__file__` as `Path(__file__).parent / "announcement-templates" / "templates"`. This path assumes `kerygma-pipeline/` and `announcement-templates/` are siblings, which is true in the superproject but **not** in CI (where packages are pip-installed from separate repos). CI works around this by only testing `kerygma_pipeline.py` from the superproject checkout.
- **Critical**: RSS poller dedup state is lost between pipeline invocations (see weakness above) — cron-triggered `rss-auto-dispatch.yml` could re-dispatch old essays
- **Medium**: `DiscordEmbed.add_field()` stores `inline` as `str("true"/"false")` instead of `bool` — Discord API expects boolean, so live mode embeds will have inline=false always
- **Medium**: `Toot.validate()` hardcodes 500 char limit, ignoring `MastodonConfig.max_chars` — instances with different limits would silently truncate or fail

### Phase 4: Growth

#### 4.1 Bloom
- **Thread support**: Mastodon `split_for_thread()` exists but is never used in the pipeline — could enable long-form essay distribution as threads
- **Engagement feedback loop**: metrics adapters exist (`ghost_metrics.py`, `mastodon_metrics.py`) but aren't wired into the pipeline — could inform scheduling priority
- **Template inheritance**: the engine could support base templates with channel-specific overrides, reducing template duplication
- **Webhook receivers**: the existing `dispatch-receiver.yml` could be extended to accept events from any organ via a standardized payload schema

#### 4.2 Evolve — Implementation Items
See Phase 2 below.

---

## Phase 2: Implementation Plan (Priority Order)

### P0 — Bugs / Correctness

#### 1. Fix RSS poller dedup state loss in pipeline
- **File**: `kerygma-pipeline/kerygma_pipeline.py:307-308`
- **Issue**: `RssPoller()` is created without `seen_path`, so dedup state is never persisted
- **Fix**: Pass `seen_path=Path(self._social_config.delivery_log_path).with_name("rss_seen.json")` or add a dedicated config field

#### 2. Fix `DiscordEmbed.add_field()` inline type
- **File**: `social-automation/kerygma_social/discord.py:25`
- **Issue**: `"inline": str(inline).lower()` produces a string; Discord API expects a boolean
- **Fix**: Change to `"inline": inline`

#### 3. Fix `Toot.validate()` hardcoded limit
- **File**: `social-automation/kerygma_social/mastodon.py:33`
- **Issue**: `return 0 < len(self.content) <= 500` ignores instance-specific `max_chars`
- **Fix**: Add `max_chars` param to `Toot` or validate in `MastodonClient.post_toot()` using `self.config.max_chars`

#### 4. Fix scheduler recurring entry ID collision
- **File**: `distribution-strategy/kerygma_strategy/scheduler.py:91`
- **Issue**: `f"{entry_id}-next"` will collide on second recurrence
- **Fix**: Append a counter or timestamp: `f"{entry_id}-{datetime.now().strftime('%Y%m%d%H%M%S')}"`

### P1 — DRY / Code Quality

#### 5. Extract shared Ghost JWT builder
- **Files**: `social-automation/kerygma_social/ghost.py:48-80`, `distribution-strategy/kerygma_strategy/ghost_metrics.py:32-47`
- **Fix**: Move JWT builder to a shared utility (either in `social-automation` since it's the dependency, or as a standalone helper) and import from both locations

#### 6. Extract shared `_build_distributor` factory
- **Files**: `social-automation/kerygma_social/cli.py:25-57`, `kerygma-pipeline/kerygma_pipeline.py:110-150`
- **Fix**: Move the factory into `kerygma_social.posse` or a new `kerygma_social.factory` module, parameterized by `SocialConfig`

### P2 — Resilience Hardening

#### 7. Add retry exception filtering
- **File**: `social-automation/kerygma_social/retry.py:64`
- **Fix**: Add `retryable_exceptions: tuple[type[Exception], ...] = (Exception,)` to `RetryConfig`, and only retry matching exceptions. Default to `(RuntimeError, OSError, ConnectionError)` or similar

#### 8. Add delivery log rotation / max size
- **File**: `social-automation/kerygma_social/delivery_log.py`
- **Fix**: Add `max_records` param to `DeliveryLog.__init__()`. On `_save()`, trim oldest records beyond the limit

### P3 — Polish

#### 9. Populate `__init__.py` with public API exports
- **Files**: all three `__init__.py` files
- **Fix**: Export key classes for cleaner imports (e.g., `from kerygma_social import PosseDistributor, Platform`)

#### 10. Fix seed.yaml inconsistencies
- **File**: `announcement-templates/seed.yaml` (create if missing), all seed.yaml `promotion_status` fields
- **Fix**: Add missing seed.yaml; update `promotion_status` from LOCAL to GRADUATED to match actual status

---

## Verification

After implementation:
1. `pytest announcement-templates/tests/ -v` — all pass
2. `pytest social-automation/tests/ -v` — all pass
3. `pytest distribution-strategy/tests/ -v` — all pass
4. `pytest kerygma-pipeline/tests/ -v` — all pass
5. `ruff check announcement-templates/ social-automation/ distribution-strategy/` — clean
6. Manual verification: `python kerygma-pipeline/kerygma_pipeline.py status` returns valid JSON
7. For P0 items: add new tests covering the fixed behaviors

## Files to Create
- `.github/docs/e2g-review-2026-02.md` — the full E2G report

## Files to Modify
- `kerygma-pipeline/kerygma_pipeline.py` (P0.1, P1.6)
- `social-automation/kerygma_social/discord.py` (P0.2)
- `social-automation/kerygma_social/mastodon.py` (P0.3)
- `distribution-strategy/kerygma_strategy/scheduler.py` (P0.4)
- `social-automation/kerygma_social/ghost.py` (P1.5)
- `distribution-strategy/kerygma_strategy/ghost_metrics.py` (P1.5)
- `social-automation/kerygma_social/cli.py` (P1.6)
- `social-automation/kerygma_social/retry.py` (P2.7)
- `social-automation/kerygma_social/delivery_log.py` (P2.8)
- `announcement-templates/kerygma_templates/__init__.py` (P3.9)
- `social-automation/kerygma_social/__init__.py` (P3.9)
- `distribution-strategy/kerygma_strategy/__init__.py` (P3.9)
