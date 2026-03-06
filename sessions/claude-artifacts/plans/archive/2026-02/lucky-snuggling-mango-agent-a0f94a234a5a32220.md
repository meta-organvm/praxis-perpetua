# ORGAN-VII Operational Readiness Investigation Plan

**Date**: 2026-02-24  
**Task**: Investigate the gap between "code works in tests" and "system actually distributes an announcement"  
**Status**: ~40% complete (plan mode - read-only investigation)

---

## Investigation Objectives

Thorough exploration of 7 components determining ORGAN-VII's ability to send its first real announcement:

1. **Config completeness** ✅ COMPLETED
2. **Ghost deployment state** ⏳ PARTIALLY COMPLETED
3. **Platform registration docs** ⏳ PENDING
4. **RSS feed state** ⏳ PENDING
5. **GitHub Actions secrets** ⏳ PENDING
6. **Dry-run capability** ⏳ PENDING
7. **Landing page / public presence** ⏳ PENDING

---

## Completed Findings

### 1. Config Completeness ✅

**File Analyzed**: `/Users/4jp/Workspace/organvm-vii-kerygma/kerygma-pipeline/kerygma_config.example.yaml`

**Key Findings**:
- Complete reference configuration exists with all 4 platforms (Mastodon, Discord, Bluesky, Ghost)
- All credential fields are **empty by default** requiring environment variable override (`KERYGMA_*` prefix pattern)
- **RSS feed URL pre-configured**: `https://organvm-v-logos.github.io/public-process/feed.xml`
- **Default mode**: `live_mode: false` (dry-run by default - **no accidental real posts**)
- 4 platform channels defined:
  - `mastodon-primary`: max_length 500
  - `discord-announcements`: max_length 4096
  - `bluesky-primary`: max_length 300, currently disabled
  - `ghost-newsletter`: max_length 0 (no limit), currently disabled
- Calendar events configured with posting_modifier for seasonal adjustments

**Critical Finding**: **No actual config file exists** (kerygma_config.yaml not present, no .env files)
- System cannot run in production without creating `kerygma_config.yaml` and setting environment variables

### 2. Ghost Deployment State ⏳ PARTIALLY COMPLETED

**File Analyzed**: `/Users/4jp/Workspace/organvm-vii-kerygma/.github/scripts/deploy-ghost-theme.py`

**Key Findings**:
- Deployment script exists (104 lines) and implements Ghost Admin API JWT authentication
- Uses HMAC-SHA256 signed JWT tokens from api_key in `{id}:{secret}` format
- Theme ZIP packaging logic properly handles directory traversal
- Multipart form-data upload to Ghost Admin API `/ghost/api/admin/themes/upload/`
- Requires two environment variables:
  - `KERYGMA_GHOST_API_URL` (e.g., `https://your-ghost.com`)
  - `KERYGMA_GHOST_ADMIN_API_KEY` (JWT signing key)
- Script exits with clear error messages if credentials missing
- **No evidence found yet of actual theme deployment or Ghost instance setup**

**Questions Remaining**:
- Has Ghost instance ever been provisioned?
- Has `deploy-ghost-theme.py` ever been executed?
- Is `organvm-theme/` populated with actual theme files?

### 3. Infrastructure Architecture ✅ (from .github/CLAUDE.md)

**Key Findings**:
- `.github/` is infrastructure submodule containing CI/CD backbone
- 8 GitHub Actions workflows defined:
  - `ci-pipeline.yml`: push to main → install + test
  - `dispatch-receiver.yml`: cross-organ events → full pipeline
  - `rss-auto-dispatch.yml`: cron every 6h → poll RSS + dispatch
  - `weekly-analytics.yml`: Monday 09:00 UTC → weekly report
  - `dispatch-log.yml`, `notify-kerygma.yml`, `quarterly-feedback.yml`, `quarterly-synthesis-dispatch.yml`
- 4 operational scripts in `.github/scripts/`:
  - `deploy-ghost-theme.py` (analyzed above)
  - `deploy-landing-page.py`
  - `sync-platform-profiles.py`
  - `update-status-badge.py`
  - `validate-live-config.py`
- seed.yaml is authoritative organ contract with 13 inbound event subscriptions from 6 organs

---

## Pending Investigations

### 3. Platform Registration Docs ⏳ PENDING

**What to investigate**:
- Search `.github/docs/` for platform setup documentation (8 docs files found but not yet read)
- Look for: Mastodon account registration, Bluesky handle setup, Discord webhook configuration, Ghost instance provisioning
- Check if any of these platforms have been actually set up for ORGANVM

**Files to read**:
- `.github/docs/platform-stack.md`
- `.github/docs/` ADR files
- `.github/docs/cross-organ-workflows/` specs

### 4. RSS Feed State ⏳ PENDING

**What to investigate**:
- Verify configured RSS feed URL (`https://organvm-v-logos.github.io/public-process/feed.xml`)
- Check if ORGAN-V (`public-process`) actually has Atom feed published
- Verify feed is accessible and contains recent essays
- Check if rss-auto-dispatch workflow would actually find new content

**Locations to check**:
- Navigate to `/Users/4jp/Workspace/organvm-v-logos/public-process/` (ORGAN-V)
- Look for `_config.yml`, `feed.xml`, or Jekyll feed configuration
- Verify feed generator is active and recently updated

### 5. GitHub Actions Secrets ⏳ PENDING

**What to investigate**:
- Examine all 8 workflow files in `.github/.github/workflows/` for `${{ secrets.* }}` references
- Catalog which secrets must be configured in GitHub repository settings
- Determine if any secrets are currently set up
- Map secrets to actual platform credentials needed

**Expected secrets** (based on config analysis):
- `KERYGMA_MASTODON_INSTANCE_URL`
- `KERYGMA_MASTODON_ACCESS_TOKEN`
- `KERYGMA_DISCORD_WEBHOOK_URL`
- `KERYGMA_BLUESKY_HANDLE`
- `KERYGMA_BLUESKY_APP_PASSWORD`
- `KERYGMA_GHOST_API_URL`
- `KERYGMA_GHOST_ADMIN_API_KEY`

### 6. Dry-Run Capability ⏳ PENDING

**What to investigate**:
- Test pipeline orchestrator CLI commands (requires venv activation and package installation)
- Execute:
  ```bash
  python kerygma-pipeline/kerygma_pipeline.py status          # Health check
  python kerygma-pipeline/kerygma_pipeline.py templates       # List templates
  python kerygma-pipeline/kerygma_pipeline.py preview --template essay-announce --repo public-process --channel mastodon
  ```
- Verify dry-run mode works and produces accurate previews without posting
- Check error handling and logging

### 7. Landing Page / Public Presence ⏳ PENDING

**What to investigate**:
- Search for evidence of live public-facing platforms:
  - Mastodon account (check fediverse social graph for @organvm or related account)
  - Ghost newsletter (check if newsletter exists and subscribers present)
  - Bluesky profile (check if account active)
  - Discord server (check if webhook has posted messages)
  - Landing page (check deploy-landing-page.py output)
- Search repository for any deployed/public URLs or API endpoints
- Check analytics for any existing audience engagement

**Files to examine**:
- `.github/scripts/deploy-landing-page.py`
- Any documented public URLs in `.github/docs/`
- Analytics records in root directory

---

## Architectural Context

### ORGAN-VII Structure
- **Superproject**: 4 submodules + orchestrator
  - `announcement-templates/`: Template engine for content generation
  - `social-automation/`: 4 platform clients (Mastodon, Discord, Bluesky, Ghost) + POSSE orchestrator
  - `distribution-strategy/`: Analytics, scheduling, calendar integration
  - `.github/`: Infrastructure, CI/CD, deployment scripts
- **Orchestrator**: `kerygma_pipeline.py` - coordinates template rendering → quality checking → POSSE dispatch → analytics recording

### Key Design Principles
- **Dry-run by default** (`live_mode: false`) - prevents accidental real posts
- **Environment variable cascade** - config file + env overrides enable flexible credential management
- **POSSE model** - publish to Ghost, syndicate to social platforms
- **Event-driven** - responds to RSS polls (ORGAN-V essays), GitHub dispatch (ORGAN-IV events), cron schedules
- **Cross-organ integration** - 13 inbound event subscriptions from 6 organs

### The Gap Analysis

**Current State**: Code works in tests, but system has never sent a real announcement

**Root Causes Hypothesis** (to be validated):
1. **No production config file**: kerygma_config.yaml missing
2. **No platform credentials**: GitHub Actions secrets not configured
3. **No platform instances**: Ghost, Mastodon, Discord, Bluesky not actually provisioned
4. **No ORGAN-V feed**: public-process Atom feed may not be accessible
5. **No orchestration trigger**: dispatch-receiver workflow may not have been called
6. **Dry-run default prevents actual delivery**: Code would need `live_mode: true` to post

---

## Next Steps (After Plan Mode)

1. **Read platform documentation** (.github/docs/)
2. **Examine workflow files** for secrets references
3. **Test pipeline CLI** (requires venv setup)
4. **Check ORGAN-V feed** availability
5. **Search for platform evidence** (deployed instances, profiles, webhook logs)
6. **Document operational checklist** for going from 0 to first dispatch:
   - Create kerygma_config.yaml with credentials
   - Provision platforms (Ghost instance, Mastodon account, Discord webhook, Bluesky handle)
   - Set GitHub Actions secrets
   - Enable live_mode in config or environment
   - Trigger test dispatch via `dispatch-receiver` workflow
   - Monitor delivery logs and analytics

---

## Files Analyzed So Far
- ✅ `/Users/4jp/Workspace/organvm-vii-kerygma/kerygma-pipeline/kerygma_config.example.yaml`
- ✅ `/Users/4jp/Workspace/organvm-vii-kerygma/.github/scripts/deploy-ghost-theme.py`
- ✅ `/Users/4jp/Workspace/organvm-vii-kerygma/.github/CLAUDE.md`

## Files Queued for Analysis
- ⏳ `.github/docs/platform-stack.md`
- ⏳ `.github/docs/` ADRs
- ⏳ `.github/.github/workflows/` (all 8 workflows)
- ⏳ `.github/scripts/deploy-landing-page.py`
- ⏳ `organvm-v-logos/public-process/` (ORGAN-V feed)
