# Plan: AQUA COMMUNIS — The Living Waters

## Context

IGNIS KOINOS (completed 2026-02-17) built the infrastructure: dark theme, full-text search, DB-backed syllabus, Docker deployment config, structured logging. All 5 repos at v0.3.0, 149 tests passing. But the system is **not yet live** — Render deployment never provisioned, migrations 002+003 not run against Neon, CORS blocks POST requests, zero HTTP integration tests, and no real-time features exist.

AQUA COMMUNIS ("common water" — the alchemical prima materia of flow) transforms ORGAN-VI from a validated codebase into a **live, hardened, interactive, well-tested community platform**.

**Outcome:** Live Render deployment, 225+ tests, paginated APIs, contributor profiles, Atom feeds, rate limiting, WebSocket live salons, deduplicated codebase.

---

## Batch 1: IGNITION — Make It Live

### 1.1 — Run Alembic migrations against Neon
From `koinonia-db/`: `DATABASE_URL=... alembic upgrade head` (002 fulltext + 003 syllabus). Verify with `alembic current` showing `003 (head)`.

### 1.2 — Fix CORS to allow POST
**File:** `community-hub/src/community_hub/app.py`
Change `allow_methods=["GET"]` → `allow_methods=["GET", "POST"]`

### 1.3 — Deploy to Render
Push community-hub to GitHub. Create Render service, set `DATABASE_URL` secret. Verify `/health`, `/api/health/deep`, `/api/stats`.

**Verify:** `curl <render-url>/health` → 200. `/api/health/deep` → `"database": "connected"`. POST `/syllabus/generate` works cross-origin.

---

## Batch 2: AQUA — Integration Tests + Pagination + Contributors
*Parallelizable with Batch 3*

### 2.1 — HTTP integration tests with TestClient
**NEW:** `community-hub/tests/test_integration.py` (~20 test functions)
Use `fastapi.testclient.TestClient` with mocked async DB session. Test all routes: `GET /health`, `/`, `/salons`, `/salons/999` (404), `/curricula`, `/search?q=`, `/api/salons`, `/api/curricula`, `/api/taxonomy`, `/api/stats`, `/api/health/deep`, `/api/manifest`, `/api/search?q=test`, `/community/events`, `/community/stats`.

Pattern:
```python
@pytest.fixture
def client():
    app = create_app()
    # mock app.state.db to yield mock async session
    with TestClient(app, raise_server_exceptions=False) as c:
        yield c
```

### 2.2 — Pagination on list endpoints
**Files:** `community-hub/src/community_hub/routes/api.py`, `salons.py`, `curricula.py`
Add `limit: int = 50, offset: int = 0` query params. Return pagination envelope:
```python
class PaginatedResponse(BaseModel):
    items: list[...]
    total: int
    limit: int
    offset: int
```
**Templates:** Add prev/next links to `salons/list.html`, `curricula/list.html`

### 2.3 — Contributor profiles
**Files:**
- `community-hub/src/community_hub/routes/community.py` — add `GET /community/contributors`, `GET /community/contributors/{handle}`
- `community-hub/src/community_hub/routes/api.py` — add `GET /api/contributors`, `GET /api/contributors/{handle}`, `ContributorOut` model
- **NEW:** `community-hub/src/community_hub/templates/community/contributors.html`
- **NEW:** `community-hub/src/community_hub/templates/community/contributor_detail.html`
- `base.html` — add Contributors nav link
- `/api/manifest` — add `"contributor_profiles"` to capabilities

**Verify:** 21 tests → ~45 tests. `GET /api/salons?limit=5` returns 5 items + `total`. `/community/contributors/4444J99` renders.

---

## Batch 3: TERRA — Test Coverage for Untested Modules
*Parallelizable with Batch 2*

### 3.1 — koinonia-db syllabus model tests
**File:** `koinonia-db/tests/test_models.py`
Add `ATTACH DATABASE ':memory:' AS syllabus` to fixture. Test LearnerProfileRow, LearningPathRow, LearningModuleRow CRUD. Update `test_base_metadata_has_tables` assertions. (+4 tests)

### 3.2 — adaptive-personal-syllabus: db_generator tests
**NEW:** `adaptive-personal-syllabus/tests/test_db_generator.py`
Test `DatabaseSyllabusGenerator` instantiation, URL normalization, `_build_modules()` with empty taxonomy, `_build_modules()` with data. (~5 tests)

### 3.3 — adaptive-personal-syllabus: CLI tests
**NEW:** `adaptive-personal-syllabus/tests/test_cli.py`
Use `click.testing.CliRunner`. Test `version`, `generate --organs I --format text/json/md`, missing `--organs` error. (~5 tests)

### 3.4 — reading-group-curriculum: repository tests
**NEW:** `reading-group-curriculum/tests/test_repository.py`
Structure tests (method existence) + live DB tests gated behind `DATABASE_URL`. (~10 tests)

### 3.5 — CI normalization
**File:** `reading-group-curriculum/.github/workflows/ci.yml` — change `python-version: "3.12"` → `"3.11"` for consistency with all other repos.

**Verify:** koinonia-db 10→14, adaptive-personal-syllabus 9→19, reading-group-curriculum 33→43. All CI green on Python 3.11.

---

## Batch 4: AER — API Hardening
*Depends on Batches 2+3*

### 4.1 — Eliminate syllabus route duplication
`community-hub/routes/syllabus.py` duplicates ~100 lines of generation logic from `adaptive-personal-syllabus/generator.py`.

Extract to: **NEW** `koinonia-db/src/koinonia_db/syllabus_service.py` — `async def generate_learning_path(session, organs, level, name)`.
Modify `community-hub/routes/syllabus.py` — replace `_generate_path()` with import from `koinonia_db.syllabus_service`.

### 4.2 — Atom feeds
**NEW:** `community-hub/src/community_hub/routes/feeds.py`
- `GET /feeds/salons.xml` — Atom 1.0 feed of salon sessions
- `GET /feeds/events.xml` — Atom feed of community events
- `GET /feeds/curricula.xml` — Atom feed of curricula

Use `xml.etree.ElementTree` (stdlib). Register router in `app.py`. Add `<link rel="alternate" type="application/atom+xml">` autodiscovery to `base.html`.

### 4.3 — Rate limiting
Add `slowapi>=0.1.9` to `community-hub/pyproject.toml`.
**Files:** `app.py` (limiter setup), `routes/syllabus.py` (`@limiter.limit("10/minute")` on POST, `"20/minute"` on GET API).

**Verify:** `from koinonia_db.syllabus_service import generate_learning_path` works. `/feeds/salons.xml` returns valid Atom XML. 21st rapid-fire generation request returns 429.

---

## Batch 5: IGNIS — WebSocket Live Salons
*Depends on Batch 4*

### 5.1 — WebSocket live salon room
**NEW:** `community-hub/src/community_hub/routes/live.py`
- `RoomManager` class (in-process, dict of room→connections)
- `GET /salons/{id}/live` — renders live room page
- `WS /ws/salons/{id}` — WebSocket join/message/leave with broadcast

**NEW:** `community-hub/src/community_hub/templates/salons/live.html`
Vanilla JS WebSocket client with chat UI, participant count, 30s keepalive ping (Render 55s idle timeout).

Register in `app.py`. Add "Join Live" link to `salons/detail.html`.

### 5.2 — WebSocket tests
Add to `test_integration.py`:
```python
with client.websocket_connect("/ws/salons/1") as ws:
    ws.send_text("Hello")
    data = ws.receive_json()
    assert data["type"] == "message"
```

**Verify:** Two browser tabs see each other's messages. WebSocket tests pass in CI.

---

## Batch 6: QUINTESSENTIA — Polish
*Can overlap with Batches 4+5*

### 6.1 — CHANGELOGs
All 5 repos: v0.4.0 entries documenting AQUA COMMUNIS additions.

### 6.2 — ADRs
- **NEW:** `community-hub/docs/adr/003-websocket-room-manager.md`
- **NEW:** `community-hub/docs/adr/004-rate-limiting-slowapi.md`
- **NEW:** `koinonia-db/docs/adr/003-syllabus-service-extraction.md`

### 6.3 — Version bump
`community-hub`: bump to `0.4.0` in `pyproject.toml` and `app.py`. Update manifest `capabilities` list with all new items.

**Verify:** CHANGELOGs updated. ADRs exist. Version consistent. `/api/manifest` lists 10 capabilities.

---

## Dependency Graph

```
        Batch 1 (IGNITION)
        ├── migrations
        ├── CORS fix
        └── Render deploy
              │
     ┌────────┴────────┐
  Batch 2 (AQUA)    Batch 3 (TERRA)
  integration tests  syllabus model tests
  pagination         db_generator tests
  contributors       CLI tests, repo tests
     └────────┬────────┘
              │
        Batch 4 (AER)
        ├── deduplication
        ├── Atom feeds
        └── rate limiting
              │
        Batch 5 (IGNIS)
        ├── WebSocket rooms
        └── WS tests
              │
        Batch 6 (QUINTESSENTIA)
        ← overlaps 4+5 →
```

## Test Count Projection

| Repo | Before | After | Delta |
|---|---|---|---|
| community-hub | 21 | ~70 | +49 |
| koinonia-db | 10 | ~14 | +4 |
| salon-archive | 76 | 76 | 0 |
| reading-group-curriculum | 33 | ~43 | +10 |
| adaptive-personal-syllabus | 9 | ~19 | +10 |
| **Total** | **149** | **~222** | **+73** |

## End-to-End Verification

1. `curl <render-url>/health` → 200 (Batch 1)
2. `POST /syllabus/generate` works cross-origin (Batch 1)
3. `GET /api/salons?limit=5&offset=0` → paginated response (Batch 2)
4. `GET /community/contributors/4444J99` → contributor detail (Batch 2)
5. 222+ tests passing across 5 repos (Batches 2+3)
6. `GET /feeds/salons.xml` → valid Atom (Batch 4)
7. 21st rapid-fire generation → 429 (Batch 4)
8. Two browser tabs share live salon messages (Batch 5)
9. `/api/manifest` → 10 capabilities (Batch 6)
