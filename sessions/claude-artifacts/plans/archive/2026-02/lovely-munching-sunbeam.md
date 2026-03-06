# Evaluation-to-Growth: ORGAN-VI (Koinonia) Project-Wide Review

## Context

ORGAN-VI is the Community organ of the ORGANVM system — a git superproject with 6 submodules (`koinonia-db`, `salon-archive`, `reading-group-curriculum`, `adaptive-personal-syllabus`, `community-hub`, `.github`). All repos are at LOCAL promotion status with no flagships graduated. This review applies the Evaluation-to-Growth lens-protocol across the entire organ to identify structural weaknesses, reinforce strengths, assess risks, and chart a concrete growth path toward CANDIDATE promotion.

---

## Phase 1: Evaluation (Critique)

### Dimension 1: Architecture & Design

**Strengths assessed in Phase 2. Issues:**

- **search_vector column mismatch** — `community-hub/routes/search.py` queries `search_vector` tsvector columns on `salons.sessions`, `reading.curricula`, and `community.events` tables. These columns are **not defined** in `koinonia-db/alembic/versions/001_initial_schema.py`. Search will crash at runtime.
  - Files: `community-hub/src/community_hub/routes/search.py`, `koinonia-db/alembic/versions/001_initial_schema.py`

- **Singleton engine divergence** — `koinonia-db/engine.py` exposes async `get_engine()`/`get_session_factory()` with a module-global `_engine`. CLI repos (`salon-archive`, `reading-group-curriculum`) create their own sync engines in `repository.py`. No shared sync engine factory exists, so each CLI reinvents connection management.
  - Files: `koinonia-db/src/koinonia_db/engine.py`, `salon-archive/src/repository.py`, `reading-group-curriculum/src/repository.py`

- **ORGAN_MAP duplication** — The organ-to-description mapping dict is defined identically in both `koinonia-db/src/koinonia_db/syllabus_service.py` and `adaptive-personal-syllabus/src/adaptive_personal_syllabus/generator.py`. Drift risk.
  - Files: `koinonia-db/src/koinonia_db/syllabus_service.py:~L15`, `adaptive-personal-syllabus/src/adaptive_personal_syllabus/generator.py:~L20`

- **Settings.require_db() triplicate** — Identical `postgresql://` → `postgresql+psycopg://` URL rewriting logic in 3 repos' config modules. Should live in `koinonia-db` as the shared DB package.
  - Files: `salon-archive/src/config.py`, `reading-group-curriculum/src/config.py`, `community-hub/src/community_hub/config.py`

### Dimension 2: Code Quality & Consistency

- **Deprecated code retained** — `sessions.py`, `taxonomy.py` (salon-archive), `curriculum.py`, `reading_list.py`, `guides.py` (reading-group-curriculum) are all marked DEPRECATED with proper docstrings but still importable. No `__all__` gating or deprecation warnings at import time.

- **CI action pinning inconsistency** — `salon-archive` pins GitHub Actions by SHA hash (e.g., `actions/checkout@<sha>`), while `community-hub` uses tag versions (`actions/checkout@v4`). Should standardize on SHA pinning for supply-chain security.
  - Files: `salon-archive/.github/workflows/ci.yml`, `community-hub/.github/workflows/ci.yml`

- **Ruff line-length divergence** — `adaptive-personal-syllabus` uses line-length `100`, all other repos use `99`. Minor but should unify.

- **contributor_count hardcoded to 0** — `community-hub/routes/api.py` returns `contributor_count: 0` in `/api/stats` instead of querying the database.
  - File: `community-hub/src/community_hub/routes/api.py`

### Dimension 3: Test Coverage

- **community-hub: 3 tests only** — `test_app.py` tests Settings defaults and `require_db()`. Zero tests for any of the 8 route modules (salons, curricula, community, api, search, feeds, live, syllabus). This is the flagship repo.
  - File: `community-hub/tests/test_app.py`

- **koinonia-db: fixture-only tests** — `test_seed.py` validates JSON fixture file structure (keys exist, types correct). No tests for ORM models, engine factory, migrations, or syllabus_service.
  - File: `koinonia-db/tests/test_seed.py`

- **reading-group-curriculum: no repository tests** — Only deprecated in-memory classes are tested. `CurriculumRepository` (the actual production code) has zero test coverage.
  - File: `reading-group-curriculum/tests/` (missing `test_repository.py`)

- **salon-archive: repository smoke tests only** — `test_repository.py` checks method existence but all DB-hitting tests are skipped without `DATABASE_URL`. No SQLite fallback or test fixtures.

- **adaptive-personal-syllabus: best coverage** — Tests models, generator initialization, and path generation. Still no integration tests for the full CLI flow or SQLite storage.

### Dimension 4: Data Integrity & Safety

- **Seed loader partial idempotency** — `load_seed.py` checks `SELECT count(*) FROM salons.taxonomy_nodes` to decide whether to run. If taxonomy loaded but sessions failed mid-run, re-running skips everything including the failed sessions. Sessions are always inserted fresh with no duplicate checking.
  - File: `koinonia-db/seed/load_seed.py`

- **No input validation on WebSocket** — `community-hub/routes/live.py` `RoomManager` accepts arbitrary JSON from WebSocket clients with no authentication, no rate limiting, no message size limit, and no sanitization before broadcasting.
  - File: `community-hub/src/community_hub/routes/live.py`

- **No CSRF protection** — community-hub serves HTML forms (syllabus generation) but has no CSRF token middleware.

### Dimension 5: Documentation & Contracts

- **seed.yaml coverage: complete** — All 6 repos have well-structured seed.yaml files declaring tier, produces/consumes edges, and event subscriptions.

- **CLAUDE.md: now accurate** — Updated in this session to reflect superproject structure, all 4 schemas, CLI entry points, and corrected gotchas.

- **AGENTS.md/GEMINI.md: now complete** — Created for community-hub and koinonia-db in this session. All submodules now have auto-synced context files.

- **No API documentation** — community-hub exposes a full REST API + WebSocket endpoint but has no OpenAPI customization, no API docs route, no endpoint documentation beyond code comments.

---

## Phase 2: Reinforcement (What's Working Well)

1. **Clean dependency graph** — `koinonia-db` as single shared foundation, consumed by all other repos. No circular dependencies. Matches ORGANVM unidirectional flow principle.

2. **Repository pattern** — `SalonRepository` and `CurriculumRepository` provide clean separation between business logic and data access. Consistent interface pattern across both CLI repos.

3. **Dual-mode architecture in adaptive-personal-syllabus** — Standalone SQLite operation (`~/.adaptive-syllabus/`) plus shared PostgreSQL via `koinonia-db/syllabus_service.py` is well-designed for both offline personal use and community integration.

4. **Comprehensive seed data** — `koinonia-db/seed/` has rich, realistic fixtures (taxonomy trees, sample sessions with segments, multi-week curricula with discussion questions). Good foundation for development and testing.

5. **Well-structured FastAPI app** — `community-hub/app.py` uses proper lifespan management, modular route registration, rate limiting via slowapi, Jinja2 templating, and exception handlers. Good production patterns.

6. **Deprecated code clearly marked** — All in-memory implementations have explicit DEPRECATED docstrings pointing to the repository-backed replacements. Clean migration path.

7. **SQLAlchemy 2.0 throughout** — Modern `Mapped[]`/`mapped_column()` ORM style, proper relationship declarations, schema isolation via `__table_args__`.

8. **Shared syllabus service** — `koinonia-db/syllabus_service.py` provides a single async `generate_learning_path()` function consumed by both community-hub and adaptive-personal-syllabus, avoiding logic duplication for the core algorithm.

---

## Phase 3: Risk Analysis

| Risk | Severity | Likelihood | Impact |
|------|----------|------------|--------|
| Search crashes in production (missing tsvector columns) | **Critical** | Certain | Broken core feature |
| WebSocket abuse (no auth/rate limit) | **High** | Likely | DoS, spam, resource exhaustion |
| Seed loader double-inserts sessions on partial failure | **Medium** | Moderate | Duplicate data |
| community-hub has no test coverage for routes | **High** | Certain | Regressions undetected |
| CI supply-chain (unpinned action tags) | **Medium** | Low | Compromised builds |
| Settings.require_db() drift across 3 copies | **Low** | Moderate | Subtle connection failures |

---

## Phase 4: Growth (Implementation Plan)

### Priority 1: Fix Critical Bugs (immediate)

#### 1a. Add search_vector columns via Alembic migration
- Create `koinonia-db/alembic/versions/002_add_search_vectors.py`
- Add `search_vector` tsvector columns to `salons.sessions`, `reading.curricula`, `community.events`
- Add GIN indexes for each
- Add trigger functions to auto-populate vectors on INSERT/UPDATE
- **Verify:** `alembic upgrade head` succeeds; `community-hub` search route returns results

#### 1b. Fix seed loader idempotency
- Modify `koinonia-db/seed/load_seed.py` to check existence per-table (not just taxonomy_nodes)
- Use `INSERT ... ON CONFLICT DO NOTHING` for sessions and other tables
- **Verify:** Running `load_seed.py` twice produces no duplicates

### Priority 2: Security Hardening (before any deployment)

#### 2a. WebSocket authentication & rate limiting
- Add token/session validation to `community-hub/routes/live.py` WebSocket connect handler
- Add per-connection message rate limit (e.g., 10 msg/sec)
- Add max message size (e.g., 4KB)
- Sanitize message content before broadcast
- **File:** `community-hub/src/community_hub/routes/live.py`

#### 2b. CSRF middleware for community-hub
- Add `starlette-csrf` or equivalent middleware to `app.py`
- Update syllabus form template to include CSRF token
- **Files:** `community-hub/src/community_hub/app.py`, templates

### Priority 3: Test Coverage (before CANDIDATE promotion)

#### 3a. community-hub route tests
- Create `community-hub/tests/test_routes.py` with `httpx.AsyncClient` + `TestClient`
- Test all API endpoints (`/api/salons`, `/api/curricula`, `/api/stats`, `/api/health/deep`, `/api/manifest`)
- Test HTML routes return 200 with expected templates
- Test search, feeds (Atom XML validation), syllabus generation
- Mock database sessions for unit tests
- **Target:** >80% route coverage

#### 3b. koinonia-db model and engine tests
- Create `koinonia-db/tests/test_models.py` — test ORM model instantiation, relationships, constraints
- Create `koinonia-db/tests/test_engine.py` — test engine factory, session factory, dispose
- Create `koinonia-db/tests/test_syllabus_service.py` — test `generate_learning_path()` with mock DB
- **Target:** Cover all 4 model modules + engine + syllabus service

#### 3c. reading-group-curriculum repository tests
- Create `reading-group-curriculum/tests/test_repository.py`
- Test `CurriculumRepository` CRUD methods with SQLite in-memory or mock sessions
- **Target:** All repository methods covered

### Priority 4: Code Deduplication (cleanup)

#### 4a. Extract Settings.require_db() to koinonia-db
- Add `koinonia_db.config.require_database_url()` utility function
- Update `salon-archive/src/config.py`, `reading-group-curriculum/src/config.py`, `community-hub/src/community_hub/config.py` to import from `koinonia_db`
- **Verify:** All CLI commands and community-hub still resolve DATABASE_URL correctly

#### 4b. Deduplicate ORGAN_MAP
- Move canonical `ORGAN_MAP` to `koinonia_db.constants` or similar
- Update `koinonia_db/syllabus_service.py` and `adaptive-personal-syllabus/generator.py` to import it
- **Verify:** Syllabus generation works from both community-hub and APS CLI

#### 4c. Remove or gate deprecated modules
- Add `warnings.warn("deprecated", DeprecationWarning)` at import time to all deprecated modules
- Or remove them entirely if no code paths reference them (check imports across all repos)
- **Files:** `salon-archive/src/sessions.py`, `salon-archive/src/taxonomy.py`, `reading-group-curriculum/src/curriculum.py`, `reading-group-curriculum/src/reading_list.py`, `reading-group-curriculum/src/guides.py`

### Priority 5: Polish & Consistency

#### 5a. Standardize CI action pinning
- Update `community-hub/.github/workflows/ci.yml` to use SHA-pinned actions (match salon-archive pattern)
- **Verify:** CI runs pass on GitHub

#### 5b. Unify ruff line-length
- Change `adaptive-personal-syllabus/pyproject.toml` ruff config from `100` to `99`
- Run `ruff format` to fix any resulting issues
- **Verify:** `ruff check` passes

#### 5c. Fix contributor_count in API
- Replace hardcoded `0` with actual `SELECT count(*) FROM community.contributors` query
- **File:** `community-hub/src/community_hub/routes/api.py`

#### 5d. Add OpenAPI metadata to community-hub
- Configure FastAPI app metadata (title, description, version, tags)
- Add response models to API endpoints for auto-generated docs
- **Verify:** `/docs` endpoint shows complete API documentation

---

## Verification Plan

1. **Database:** `alembic upgrade head` on a test database — confirm search_vector columns and GIN indexes exist
2. **Seed:** Run `load_seed.py` twice — confirm no duplicate rows
3. **Tests:** `pytest tests/ -v` in each repo — all pass, new tests included
4. **Lint:** `ruff check src/` in each repo — clean
5. **Search:** Start community-hub, perform a search query — results returned without error
6. **WebSocket:** Connect to `/ws/{room}` — confirm auth required, rate limits enforced
7. **API:** Hit `/api/stats` — confirm `contributor_count` reflects actual data
8. **CI:** Push to each repo — GitHub Actions pass with SHA-pinned actions
