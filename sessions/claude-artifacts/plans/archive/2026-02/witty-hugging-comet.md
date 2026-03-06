# Plan: Build "The Actual News" from Design Document

## Context

The repo `/Users/4jp/Workspace/the-actual-news/` contains one file: `News-as-Public-Service.md` (4,433 lines). It's a comprehensive AI-chat transcript that progressively designs a verifiable news ledger platform — from philosophy through OpenAPI contracts, database schemas, a working gateway service, a 10-phase roadmap, an RFC-style protocol spec, and a conformance test suite with 8 fixtures.

**Goal:** Extract this design into a fully-functioning, professionally-structured monorepo using three skills in order:
1. **Speckit** — Formalize the design into SDD artifacts (spec, plan, tasks)
2. **github-repository-standards** — Minimal Root structure, World-Class README
3. **github-repo-curator** — Community health, documentation standards, CI

**Decisions:** AGPL-3.0 license, pnpm workspaces.

---

## Execution Order (7 phases, ~34 files to extract/create)

### Phase 0: Repository Foundation
*Skill: github-repository-standards + github-repo-curator*

Create the skeleton before any code lands.

| File | Purpose |
|------|---------|
| `.gitignore` | Node, macOS, IDE, .env patterns |
| `LICENSE` | AGPL-3.0 |
| `.editorconfig` | Consistent formatting |
| `pnpm-workspace.yaml` | Workspace: `services/*`, `apps/*`, `tools/conformance` |
| `package.json` | Root package (private, scripts) |
| `.github/CONTRIBUTING.md` | Contribution guide |
| `.github/CODE_OF_CONDUCT.md` | Contributor Covenant |
| `.github/SECURITY.md` | Security policy |
| `.github/PULL_REQUEST_TEMPLATE.md` | PR template |
| `.github/ISSUE_TEMPLATE/bug_report.yml` | Bug report form |
| `.github/ISSUE_TEMPLATE/feature_request.yml` | Feature request form |
| `CHANGELOG.md` | Keep a Changelog format |
| `README.md` | World-Class README (hero, Mermaid architecture, quick start, badges) |

**Commit:** `feat: initialize repo with standards, community health, and license`

---

### Phase 1: Speckit SDD Formalization
*Skill: speckit (specify → plan → tasks)*

Preserve the source document, then formalize it into SDD format.

| File | Purpose |
|------|---------|
| `docs/design/News-as-Public-Service.md` | Source document moved here as design provenance |
| `memory/constitution.md` | Project constitution (10 invariants from protocol spec) |
| `specs/verifiable-news-platform/spec.md` | Feature spec: 8 user stories, 10+ FRs, acceptance criteria from CT-01..CT-07 |
| `specs/verifiable-news-platform/plan.md` | Technical plan: data model, service architecture, policy packs |
| `specs/verifiable-news-platform/tasks.md` | Executable task list organized by user story |

**Key user stories to formalize:**
- US-01 (P1): Reader views story with verification spine
- US-02 (P1): Reader browses quality-ranked feed
- US-03 (P1): Verifier reviews claims and submits verdicts
- US-04 (P2): Publisher drafts with evidence-first editor, system extracts claims
- US-05 (P2): Publisher publishes; system enforces quality gates
- US-06 (P2): Third party queries public API
- US-07 (P3): System detects claim contradictions
- US-08 (P3): Corrections append to ledger

**Commit:** `feat: add SDD specification, plan, and task artifacts`

---

### Phase 2: Contracts, Schemas, and Protocol Spec
*Extract from source document code blocks*

| File | Source Lines | Content |
|------|-------------|---------|
| `contracts/openapi/common.openapi.yaml` | 418-457 | Shared types (Ulid, IsoTime, Error, ActorRef, EvidenceRef) |
| `contracts/openapi/story.openapi.yaml` | 463-640 | Story CRUD, versions, publish |
| `contracts/openapi/claim.openapi.yaml` | 646-739 | Claim extraction, listing |
| `contracts/openapi/evidence.openapi.yaml` | 745-849 | Evidence presign, register, get |
| `contracts/openapi/verify.openapi.yaml` | 855-947 | Verification tasks, reviews |
| `contracts/openapi/gateway.openapi.yaml` | 955-1036 | Public BFF: feed, story bundle |
| `contracts/events/envelope.v1.schema.json` | 1190-1208 | CloudEvents-style envelope |
| `contracts/events/story.published.v1.schema.json` | 1212-1235 | Story published event |
| `contracts/policy-packs/v1.0.0.json` | 2675-2697 | Default policy pack thresholds |
| `db/migrations/001_init.sql` | 1044-1149 | 10 tables (actors through corrections) |
| `db/migrations/002_outbox.sql` | 1154-1167 | Event outbox table |
| `db/migrations/003_indexes.sql` | 1172-1182 | Performance indexes |
| `specs/protocol/core-protocol-spec-v1.md` | 2567-2994 | RFC: terminology, invariants I1-I10, algorithms 4.1-4.6 |

**Commit:** `feat: extract contracts, migrations, and protocol specification`

---

### Phase 3: Infrastructure and Tooling
*Extract from source document + create new*

| File | Source Lines | Notes |
|------|-------------|-------|
| `.env.example` | 322-350 | All env vars with defaults |
| `Makefile` | 1293-1307 | Extended: up, down, migrate, reset, lint, test, dev |
| `tools/migrate.sh` | 1311-1321 | Make executable (chmod +x) |
| `tools/gen-ulid.ts` | — | New: simple ULID generator using `ulid` package |
| `infra/docker-compose.yml` | 358-412 | Postgres + Prism mocks (add resource limits) |
| `infra/postgres/init.sql` | — | Symlink or copy of migrations |
| `tools/conformance/package.json` | — | New: `pg` dependency |
| `tools/conformance/sql/schema.sql` | 3028-3094 + 4107-4117 | All tables including event_outbox |
| `tools/conformance/sql/publish_gate.sql` | 3117-3218 | Policy-parameterized gate query |
| `tools/conformance/sql/publish_txn.sql` | 4134-4271 | Transactional publish + assertions |
| `tools/conformance/fixtures/CT-01.json` | 3226-3378 | Minimal publish passes |
| `tools/conformance/fixtures/CT-02.json` | 3382-3497 | Fails unsupported claim share |
| `tools/conformance/fixtures/CT-03A.json` | 3501-3561 | Ratio edge passes at 0.50 |
| `tools/conformance/fixtures/CT-03B.json` | 3567-3627 | Ratio fails at 0.60 |
| `tools/conformance/fixtures/CT-04.json` | 3631-3690 | High-impact corroboration passes |
| `tools/conformance/fixtures/CT-05.json` | 3694-3753 | Same independence key fails |
| `tools/conformance/fixtures/CT-06.json` | 3757-3810 | Contradicted claims hard fail |
| `tools/conformance/fixtures/CT-07.json` | 3816-3875 | Missing provenance conservative |
| `tools/conformance/run.mjs` | 3893-4087 + 4280-4415 | Final version with publish txn |

**Commit:** `feat: add infrastructure, conformance harness, and build tooling`

---

### Phase 4: Gateway Service
*Extract from source document — most complex merge*

| File | Source Lines | Notes |
|------|-------------|-------|
| `services/gateway/package.json` | 1371-1393 | Dependencies: express, pg |
| `services/gateway/tsconfig.json` | 1399-1413 | ES2022, strict |
| `services/gateway/src/env.ts` | 1421-1438 | PLATFORM_ID + POSTGRES_URI |
| `services/gateway/src/db.ts` | 1444-1451 | pg Pool factory |
| `services/gateway/src/server.ts` | **Composite** | Merge 3 code blocks into one coherent file |

**server.ts assembly order:**
1. Imports + types (lines 1460-1508)
2. Env + pool + app setup (lines 1510-1514)
3. `GET /v1/health` (lines 1516-1518)
4. `GET /v1/feed` (lines 1679-1721) — insert here
5. `GET /v1/story/:story_id` (lines 1520-1639)
6. `POST /v1/story/:story_id/publish` (lines 2144-2370)
7. `ulidLike()` helper (lines 2373-2377)
8. Server listen + shutdown (lines 1624-1639)

**Service stubs** (health-only placeholder for future implementation):
| File | Notes |
|------|-------|
| `services/story/package.json` | Stub |
| `services/story/src/server.ts` | `/v1/health` only |
| `services/claim/package.json` | Stub |
| `services/claim/src/server.ts` | `/v1/health` only |
| `services/evidence/package.json` | Stub |
| `services/evidence/src/server.ts` | `/v1/health` only |
| `services/verify/package.json` | Stub |
| `services/verify/src/server.ts` | `/v1/health` only |

**Commit:** `feat: extract gateway service with feed, story, and publish endpoints`

---

### Phase 5: UI Skeleton
*Partially extracted, partially new*

| File | Source Lines | Notes |
|------|-------------|-------|
| `apps/public-web/package.json` | — | New: next, react, react-dom |
| `apps/public-web/next.config.js` | — | New: minimal config |
| `apps/public-web/tsconfig.json` | — | New: extends base |
| `apps/public-web/src/lib/env.ts` | 1265-1272 | Extracted |
| `apps/public-web/src/lib/api.ts` | 1276-1284 | Extracted |
| `apps/public-web/src/pages/index.tsx` | — | New: feed page (GET /v1/feed) |
| `apps/public-web/src/pages/story/[story_id].tsx` | — | New: story + verification spine |
| `apps/public-web/src/pages/verify/index.tsx` | — | New: task queue |
| `apps/public-web/src/pages/verify/task/[task_id].tsx` | — | New: task review form |

**Commit:** `feat: add Next.js reader and verifier UI skeleton`

---

### Phase 6: Workspace Wiring and CI
*Ties everything together*

| File | Notes |
|------|-------|
| `pnpm-workspace.yaml` | Finalize workspace members |
| `.github/workflows/ci.yml` | Lint OpenAPI, typecheck TS, run conformance against Postgres |
| `.config/typescript/tsconfig.base.json` | Shared compiler options |
| `Makefile` | Add: `lint`, `test`, `dev`, `dev-minimal` targets |

**Commit:** `feat: configure monorepo workspaces and CI pipeline`

---

### Phase 7: Documentation Polish
*Skill: github-repository-standards + github-repo-curator*

| File | Notes |
|------|-------|
| `README.md` | Finalize: architecture Mermaid, working quick start, all badges |
| `docs/architecture.md` | Platform design + service architecture (extracted from source lines 1-228) |
| `docs/roadmap.md` | 10-phase plan (extracted from source lines 1727-1951) |
| `docs/glossary.md` | Terminology from protocol spec section 1 |

**Commit:** `docs: add architecture, roadmap, and glossary documentation`

---

## Final Repository Layout

```
the-actual-news/
├── .config/typescript/tsconfig.base.json
├── .editorconfig
├── .env.example
├── .gitignore
├── .github/
│   ├── CONTRIBUTING.md
│   ├── CODE_OF_CONDUCT.md
│   ├── SECURITY.md
│   ├── PULL_REQUEST_TEMPLATE.md
│   ├── ISSUE_TEMPLATE/{bug_report,feature_request}.yml
│   └── workflows/ci.yml
├── CHANGELOG.md
├── LICENSE (AGPL-3.0)
├── Makefile
├── README.md
├── package.json
├── pnpm-workspace.yaml
├── contracts/
│   ├── openapi/{common,gateway,story,claim,evidence,verify}.openapi.yaml
│   ├── events/{envelope,story.published}.v1.schema.json
│   └── policy-packs/v1.0.0.json
├── db/migrations/{001_init,002_outbox,003_indexes}.sql
├── docs/
│   ├── architecture.md
│   ├── roadmap.md
│   ├── glossary.md
│   └── design/News-as-Public-Service.md
├── specs/
│   ├── protocol/core-protocol-spec-v1.md
│   └── verifiable-news-platform/{spec,plan,tasks}.md
├── memory/constitution.md
├── services/
│   ├── gateway/  (full implementation: 4 routes)
│   ├── story/    (health stub)
│   ├── claim/    (health stub)
│   ├── evidence/ (health stub)
│   └── verify/   (health stub)
├── apps/public-web/  (Next.js: 4 pages)
├── infra/
│   ├── docker-compose.yml
│   └── postgres/init.sql
└── tools/
    ├── migrate.sh
    ├── gen-ulid.ts
    └── conformance/
        ├── run.mjs
        ├── sql/{schema,publish_gate,publish_txn}.sql
        └── fixtures/CT-{01..07}.json
```

**Total: ~60 files** (34 extracted from source doc + ~26 new)

---

## Verification

After all phases complete:

1. **Structure check:** Root directory has <15 items (Minimal Root philosophy)
2. **Contracts valid:** `npx @redocly/cli lint contracts/openapi/*.yaml`
3. **Migrations idempotent:** `make up && make migrate` runs clean
4. **Gateway starts:** `cd services/gateway && pnpm dev` → health endpoint responds
5. **Conformance passes:** `make test` → all CT-01..CT-07 pass (requires Postgres running)
6. **UI renders:** `cd apps/public-web && pnpm dev` → feed page loads against Prism mocks or real gateway
7. **CI green:** Push to GitHub → workflow validates lint + typecheck + conformance

---

## Tricky Merges

1. **`services/gateway/src/server.ts`** — Three separate code blocks from the source must be merged into one file with correct route ordering. The feed route goes between health and story; the publish endpoint goes after story; the `ulidLike` helper goes near the bottom before `app.listen`.

2. **`tools/conformance/run.mjs`** — Two versions exist in the source (initial + final with publish txn assertions). Use only the final version from lines 4286-4414 plus the `PUBLISH_TXN_SQL` import from line 4280.

3. **`tools/conformance/sql/schema.sql`** — Initial version (lines 3028-3094) lacks `event_outbox`. Must insert the table from lines 4107-4117 before the `COMMIT;`.
