# PROCLAMATIO Sprint — Ghost Newsletter + Platform Stack Integration

## Context

Research into newsletter platforms identified **Ghost** as the ideal hub for a creative technologist/artist persona. Ghost offers:
- Full visual control (custom themes, CSS, responsive galleries)
- Headless CMS mode (Content API for custom frontends)
- Native **ActivityPub/Fediverse** integration (newsletter = followable Mastodon/Threads profile)
- 0% revenue fees (vs Substack's 10%)
- Open source, self-hostable

The user **already has a Ghost instance**. The ORGAN-VII kerygma pipeline currently supports Mastodon, Discord, and Bluesky as POSSE distribution targets. A Ghost "Publish to Ghost Newsletter" step exists in the ORGAN-IV `distribute-content.yml` workflow (using raw `curl` + JWT auth), but there is **no Ghost adapter** in the `kerygma_social` package and **no Ghost channel** in the template system.

**Goal:** Make Ghost a first-class platform in the kerygma pipeline, wire ActivityPub, and document the full platform stack architecture.

---

## Phase 1: GHOST ADAPTER — `kerygma_social/ghost.py`

### 1A: Create Ghost adapter module
Following the exact pattern of `bluesky.py` (config dataclass, post dataclass, client with live/mock modes):

- **File:** `social-automation/kerygma_social/ghost.py`
- `GhostConfig`: `admin_api_key`, `api_url`, `newsletter_slug` (optional)
- `GhostPost`: `title`, `html`, `status` (draft/published), `tags`, `excerpt`
- `GhostClient`:
  - `__init__(config, live=False)` — same live/mock pattern
  - `_build_jwt()` — split key into id:secret, build HS256 JWT (port the logic from distribute-content.yml lines 248–254)
  - `create_post(post: GhostPost)` → dict — POST to `/ghost/api/admin/posts/`
  - `format_for_ghost(title, body, canonical_url)` → GhostPost — convert pipeline content to Ghost HTML
- Mock mode: record posts in `_posted` list without API calls

### 1B: Create Ghost tests
- **File:** `social-automation/tests/test_ghost.py`
- Test JWT generation (known key → known token structure)
- Test mock post creation
- Test format_for_ghost output
- Test config loading

### 1C: Wire Ghost into config.py
- **File:** `social-automation/kerygma_social/config.py`
- Add `ghost_api_url`, `ghost_admin_api_key`, `ghost_newsletter_slug` to `SocialConfig`
- Add `KERYGMA_GHOST_API_URL`, `KERYGMA_GHOST_ADMIN_API_KEY` env var mappings

### 1D: Wire Ghost into POSSE distributor
- **File:** `social-automation/kerygma_social/posse.py`
- Add `Platform.GHOST = "ghost"` to enum
- Add `ghost_client: GhostClient | None = None` to `PosseDistributor.__init__`
- Add `_syndicate_ghost()` method following mastodon/discord/bluesky pattern
- Add Ghost branch to `syndicate()` method

### 1E: Update kerygma_config.example.yaml
- **File:** `kerygma_config.example.yaml` (root)
- Add `ghost:` section with `api_url`, `admin_api_key`, `newsletter_slug`

### 1F: Commit and push social-automation
- Commit: `feat: add Ghost newsletter adapter — GhostClient, JWT auth, POSSE integration`
- Push to origin main

---

## Phase 2: GHOST TEMPLATES — Channel blocks in all 15 templates

### 2A: Add Ghost to quality checker
- **File:** `announcement-templates/kerygma_templates/quality_checker.py`
- Add `"ghost": 0` to `CHANNEL_LIMITS` (Ghost has no char limit — it's HTML email)
- The checker already handles `limit == 0` as "no limit defined" (returns info, not error)

### 2B: Add `{{#channel ghost}}` blocks to all 15 templates
Ghost blocks should be longer-form HTML-friendly content (unlike 300-char Bluesky). Pattern:
```
{{#channel ghost}}
# {{ event.title }}

{{ event.summary }}

[Read more]({{ event.url }})
{{/channel}}
```
- **Files:** All 15 files in `announcement-templates/templates/`
- Update frontmatter `channels:` lists to include `ghost`

### 2C: Unarchive, commit, push, re-archive announcement-templates
- `gh api` unarchive → push → re-archive

---

## Phase 3: PIPELINE — Wire Ghost end-to-end

### 3A: Update kerygma_pipeline.py
- **File:** `.github/kerygma_pipeline.py`
- Import `GhostClient`, `GhostConfig` from `kerygma_social.ghost`
- Add Ghost client construction in `_build_distributor()`
- Add `"ghost"` to default channels in `run_full_pipeline()` and `status()`
- Sync local copy at workspace root

### 3B: Update dispatch-receiver.yml
- **File:** `.github/.github/workflows/dispatch-receiver.yml`
- Add `KERYGMA_GHOST_API_URL` and `KERYGMA_GHOST_ADMIN_API_KEY` secrets to env

### 3C: Commit and push .github
- Commit: `feat: wire Ghost into pipeline, dispatch-receiver, and default channels`

---

## Phase 4: ACTIVITYPUB — Fediverse native presence

### 4A: Document Ghost ActivityPub setup
Ghost's ActivityPub integration makes the newsletter a followable Fediverse profile. This is a Ghost admin setting, not code:
- Enable ActivityPub in Ghost Admin → Settings → Labs
- The Ghost instance becomes `@index@yourdomain.com` on Mastodon/Threads/Flipboard

### 4B: Add ActivityPub awareness to seed.yaml
- **File:** `.github/seed.yaml`
- Add `fediverse` section documenting the Ghost↔ActivityPub bridge
- Note that Ghost publishing automatically federates to Mastodon followers

### 4C: Create ADR documenting platform strategy
- **File:** `.github/docs/adr/001-ghost-as-canonical-hub.md`
- Decision: Ghost is the canonical publishing hub
- POSSE flow: Ghost (canonical) → Mastodon, Discord, Bluesky (syndication)
- ActivityPub: Ghost native federation replaces manual Mastodon cross-posting for newsletter content
- Rationale from research (headless CMS, visual control, 0% fees, open source)

---

## Phase 5: PLATFORM STACK — Document the full creative technologist stack

### 5A: Create platform architecture document
- **File:** `.github/docs/platform-stack.md`
- Document the "Full Stack Architecture" from the research:

| Layer | Platform | Purpose |
|-------|----------|---------|
| **Hub** | Ghost | Canonical publishing, newsletter, membership |
| **Fediverse** | Mastodon (via Ghost ActivityPub) | Open social web presence |
| **Social** | Bluesky | "Town square" — writers/artists community |
| **Social** | Discord | Community server, real-time discussion |
| **Visual** | Instagram (manual) | Visual portfolio / gallery |
| **Professional** | Read.cv | Creative technologist identity |
| **Inspiration** | Are.na | Research/mood boarding |
| **Code** | GitHub | Source, process, building in public |
| **Landing** | Bento.me (or Ghost homepage) | Link-in-bio / landing page |

### 5B: Update seed.yaml with platform stack
- **File:** `.github/seed.yaml`
- Add `platform_stack` section listing all platforms and their role
- Add Ghost as a `produces` target (newsletter content)

### 5C: Commit and push all remaining changes

---

## Phase 6: REGISTRY — Contract reconciliation

### 6A: Update registry-v2.json
- **File:** `~/Workspace/meta-organvm/organvm-corpvs-testamentvm/registry-v2.json`
- Update ORGAN-VII descriptions to mention Ghost newsletter integration
- Note PROCLAMATIO sprint in repo notes

### 6B: Run validation
- Run existing validation scripts to confirm no regressions

---

## Execution Order

Sequential (each depends on previous):

1. **Phase 1** (GHOST ADAPTER) — Ghost client + tests + config + POSSE wire
2. **Phase 2** (GHOST TEMPLATES) — Channel blocks in all 15 templates
3. **Phase 3** (PIPELINE) — Wire Ghost into orchestrator and dispatch workflow
4. **Phase 4** (ACTIVITYPUB) — Document Ghost↔Fediverse bridge + ADR
5. **Phase 5** (PLATFORM STACK) — Full stack architecture documentation
6. **Phase 6** (REGISTRY) — Contract update

## Critical Files

| File | Phase | Action |
|------|-------|--------|
| `social-automation/kerygma_social/ghost.py` | 1A | **CREATE** — Ghost adapter |
| `social-automation/tests/test_ghost.py` | 1B | **CREATE** — Ghost tests |
| `social-automation/kerygma_social/config.py` | 1C | EDIT — add Ghost config fields |
| `social-automation/kerygma_social/posse.py` | 1D | EDIT — add Platform.GHOST + syndicate method |
| `kerygma_config.example.yaml` | 1E | EDIT — add ghost section |
| `announcement-templates/kerygma_templates/quality_checker.py` | 2A | EDIT — add ghost limit |
| `announcement-templates/templates/**/*.md` (15 files) | 2B | EDIT — add ghost channel blocks |
| `.github/kerygma_pipeline.py` | 3A | EDIT — import and wire Ghost |
| `.github/.github/workflows/dispatch-receiver.yml` | 3B | EDIT — add Ghost secrets |
| `.github/docs/adr/001-ghost-as-canonical-hub.md` | 4C | **CREATE** — ADR |
| `.github/docs/platform-stack.md` | 5A | **CREATE** — Platform architecture |
| `.github/seed.yaml` | 4B, 5B | EDIT — ActivityPub + platform stack |
| `registry-v2.json` | 6A | EDIT — update descriptions |

## Verification

1. `cd social-automation && pytest tests/test_ghost.py -v` — Ghost adapter tests pass
2. `cd social-automation && pytest tests/ -v` — All 66+ tests still pass
3. `cd announcement-templates && pytest tests/ -v` — All 83+ tests still pass
4. `python kerygma_pipeline.py status` — Shows Ghost as a configured channel
5. `python kerygma_pipeline.py preview --template essay-announce --repo public-process --channel ghost` — Renders Ghost HTML
6. `grep -r "channel ghost" announcement-templates/templates/ | wc -l` — Returns 15
7. YAML lint on seed.yaml — valid
8. Registry validation script passes
