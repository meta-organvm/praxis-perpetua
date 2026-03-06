# IGNIS PERPETUUS Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Activate the full ORGAN-VII kerygma pipeline — live fire across 5 channels, cross-organ event wiring, autonomous distribution loop, and public-facing Ghost theme.

**Architecture:** Four sequential phases. Phase I validates live API connectivity and fires the first real dispatch. Phase II wires reusable workflows so other organs trigger distribution. Phase III adds cron-driven RSS polling, bidirectional analytics, and self-generating weekly reports. Phase IV deploys a custom Ghost theme and landing configuration.

**Tech Stack:** Python 3.12+, GitHub Actions (workflows + repository_dispatch), Ghost Admin API (JWT/HS256), Mastodon API, AT Protocol (Bluesky), Discord webhooks, Handlebars (Ghost theme), pytest.

---

## Phase I: IGNITION — First Live Fire

### Task 1: Live Config Validation Script

**Files:**
- Create: `.github/scripts/validate-live-config.py`
- Test: `.github/tests/test_validate_live_config.py`

**Step 1: Write the test**

```python
# .github/tests/test_validate_live_config.py
"""Tests for live config validator — mock all HTTP calls."""
import types
from unittest.mock import patch, MagicMock

import pytest


def _import_validator():
    """Import the script as a module."""
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "validate_live_config",
        "scripts/validate-live-config.py",
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class TestCheckEndpoint:
    def test_success_returns_true(self):
        mod = _import_validator()
        with patch("urllib.request.urlopen") as mock_open:
            mock_resp = MagicMock()
            mock_resp.__enter__ = MagicMock(return_value=mock_resp)
            mock_resp.__exit__ = MagicMock(return_value=False)
            mock_resp.status = 200
            mock_open.return_value = mock_resp
            assert mod.check_endpoint("Ghost", "https://example.com/ghost/api/admin/site/", {}) is True

    def test_failure_returns_false(self):
        mod = _import_validator()
        with patch("urllib.request.urlopen", side_effect=Exception("Connection refused")):
            assert mod.check_endpoint("Ghost", "https://bad.example.com", {}) is False


class TestBuildChecks:
    def test_ghost_check_skipped_without_env(self):
        mod = _import_validator()
        with patch.dict("os.environ", {}, clear=True):
            checks = mod.build_checks()
            ghost_checks = [c for c in checks if c[0] == "Ghost"]
            assert len(ghost_checks) == 0

    def test_ghost_check_present_with_env(self):
        mod = _import_validator()
        env = {
            "KERYGMA_GHOST_API_URL": "https://ghost.example.com",
            "KERYGMA_GHOST_ADMIN_API_KEY": "abc:def",
        }
        with patch.dict("os.environ", env, clear=True):
            checks = mod.build_checks()
            ghost_checks = [c for c in checks if c[0] == "Ghost"]
            assert len(ghost_checks) == 1
```

**Step 2:** Run: `cd /Users/4jp/Workspace/organvm-vii-kerygma/.github && python -m pytest tests/test_validate_live_config.py -v`
Expected: FAIL (script doesn't exist yet)

**Step 3: Write the script**

```python
#!/usr/bin/env python3
"""Validate live API connectivity for all configured kerygma platforms.

Checks each endpoint with a read-only request (no posting).
Exit 0 = all configured endpoints reachable.
Exit 1 = at least one endpoint unreachable.
"""
from __future__ import annotations

import hashlib
import hmac
import json
import os
import sys
import time
import urllib.error
import urllib.request
from base64 import urlsafe_b64encode


def check_endpoint(name: str, url: str, headers: dict[str, str]) -> bool:
    """Send a GET/HEAD request and return True if we get a 2xx response."""
    req = urllib.request.Request(url, headers=headers, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            print(f"  [{name}] OK — HTTP {resp.status}")
            return True
    except Exception as exc:
        print(f"  [{name}] FAIL — {exc}")
        return False


def _ghost_jwt(api_key: str) -> str: # allow-secret
    key_id, secret_hex = api_key.split(":")
    header = json.dumps({"alg": "HS256", "typ": "JWT", "kid": key_id}, separators=(",", ":"))
    now = int(time.time())
    payload = json.dumps({"iat": now, "exp": now + 300, "aud": "/admin/"}, separators=(",", ":"))

    def b64(data: bytes) -> str:
        return urlsafe_b64encode(data).rstrip(b"=").decode()

    signing_input = f"{b64(header.encode())}.{b64(payload.encode())}"
    sig = hmac.new(bytes.fromhex(secret_hex), signing_input.encode(), hashlib.sha256).digest()
    return f"{signing_input}.{b64(sig)}"  # allow-secret — runtime JWT


def build_checks() -> list[tuple[str, str, dict[str, str]]]:
    """Build list of (name, url, headers) checks from environment."""
    checks: list[tuple[str, str, dict[str, str]]] = []

    ghost_url = os.environ.get("KERYGMA_GHOST_API_URL", "")
    ghost_key = os.environ.get("KERYGMA_GHOST_ADMIN_API_KEY", "")
    if ghost_url and ghost_key:
        token = _ghost_jwt(ghost_key)  # allow-secret
        checks.append(("Ghost", f"{ghost_url}/ghost/api/admin/site/", {"Authorization": f"Ghost {token}"}))

    masto_url = os.environ.get("KERYGMA_MASTODON_INSTANCE_URL", "")
    masto_token = os.environ.get("KERYGMA_MASTODON_ACCESS_TOKEN", "")
    if masto_url and masto_token:
        checks.append(("Mastodon", f"{masto_url}/api/v1/apps/verify_credentials",
                        {"Authorization": f"Bearer {masto_token}"}))

    discord_url = os.environ.get("KERYGMA_DISCORD_WEBHOOK_URL", "")
    if discord_url:
        checks.append(("Discord", discord_url, {}))

    bsky_handle = os.environ.get("KERYGMA_BLUESKY_HANDLE", "")
    if bsky_handle:
        checks.append(("Bluesky", "https://bsky.social/xrpc/com.atproto.server.describeServer", {}))

    return checks


def main() -> int:
    print("Kerygma Live Config Validation")
    print("=" * 40)
    checks = build_checks()
    if not checks:
        print("No platforms configured (set KERYGMA_* env vars).")
        return 1

    results = []
    for name, url, headers in checks:
        results.append(check_endpoint(name, url, headers))

    passed = sum(results)
    total = len(results)
    print(f"\n{passed}/{total} endpoints reachable.")
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
```

**Step 4:** Run: `cd /Users/4jp/Workspace/organvm-vii-kerygma/.github && python -m pytest tests/test_validate_live_config.py -v`
Expected: 4 PASS

**Step 5: Commit**
```bash
cd /Users/4jp/Workspace/organvm-vii-kerygma/.github
git add scripts/validate-live-config.py tests/test_validate_live_config.py
git commit -m "feat: add live config validation script with tests"
```

### Task 2: Manual — Configure GitHub Secrets

> **MANUAL STEP:** The user must add these 6 secrets to the `organvm-vii-kerygma` GitHub org:
> - `KERYGMA_GHOST_API_URL`
> - `KERYGMA_GHOST_ADMIN_API_KEY`
> - `KERYGMA_MASTODON_ACCESS_TOKEN`
> - `KERYGMA_DISCORD_WEBHOOK_URL`
> - `KERYGMA_BLUESKY_HANDLE`
> - `KERYGMA_BLUESKY_APP_PASSWORD`
>
> Then run: `python scripts/validate-live-config.py` locally with the env vars to verify connectivity.
> Pause here and confirm all endpoints report OK before proceeding.

### Task 3: First Live Dispatch

> **LIVE STEP — requires secrets configured:**
> ```bash
> cd /Users/4jp/Workspace/organvm-vii-kerygma
> KERYGMA_LIVE_MODE=true python kerygma_pipeline.py dispatch \
>   --template essay-announce --repo public-process \
>   --channels mastodon,discord,bluesky,ghost
> ```
> Verify delivery log shows 4 PUBLISHED entries.
> Capture evidence (screenshot or copy dispatch output).

---

## Phase II: NEXUS — Cross-Organ Nervous System

### Task 4: Upgrade notify-kerygma.yml to Reusable Workflow

**Files:**
- Modify: `.github/.github/workflows/notify-kerygma.yml`

**Step 1: Read current file**

Read `notify-kerygma.yml` to understand current structure.

**Step 2: Rewrite as reusable `workflow_call`**

The workflow must accept inputs (`event_type`, `repo_name`, `channels`) and fire a `repository_dispatch` to `organvm-vii-kerygma/.github`. Requires a PAT secret (`CROSS_ORG_DISPATCH_TOKEN`) with `repo` scope.

```yaml
name: Notify Kerygma

on:
  workflow_call:
    inputs:
      event_type:
        required: true
        type: string
        description: "Event type (e.g. essay-published, feature-released)"
      repo_name:
        required: true
        type: string
        description: "Source repository name"
      channels:
        required: false
        type: string
        default: "mastodon,discord,bluesky,ghost"
        description: "Comma-separated distribution channels"
    secrets:
      CROSS_ORG_DISPATCH_TOKEN:
        required: true
        description: "PAT with repo scope for cross-org dispatch"

jobs:
  dispatch:
    runs-on: ubuntu-latest
    steps:
      - name: Fire dispatch to ORGAN-VII
        env:
          GH_TOKEN: ${{ secrets.CROSS_ORG_DISPATCH_TOKEN }}
          EVENT_TYPE: ${{ inputs.event_type }}
          REPO_NAME: ${{ inputs.repo_name }}
          CHANNELS: ${{ inputs.channels }}
        run: |
          gh api repos/organvm-vii-kerygma/.github/dispatches \
            -f "event_type=$EVENT_TYPE" \
            -f "client_payload[repo_name]=$REPO_NAME" \
            -f "client_payload[channels]=$CHANNELS"
          echo "Dispatched $EVENT_TYPE for $REPO_NAME to ORGAN-VII"
```

**Step 3: Commit**
```bash
git add .github/workflows/notify-kerygma.yml
git commit -m "feat: upgrade notify-kerygma to reusable workflow_call"
```

### Task 5: ORGAN-V Essay Trigger

**Files:**
- Create: workflow file to be pushed to `organvm-v-logos/public-process`

**Step 1: Write the workflow**

```yaml
# .github/workflows/notify-essay-published.yml
name: Notify Essay Published

on:
  push:
    branches: [main]
    paths:
      - '_posts/**'
      - 'essays/**'

jobs:
  notify:
    uses: organvm-vii-kerygma/.github/.github/workflows/notify-kerygma.yml@main
    with:
      event_type: essay-published
      repo_name: public-process
      channels: mastodon,discord,bluesky,ghost
    secrets:
      CROSS_ORG_DISPATCH_TOKEN: ${{ secrets.CROSS_ORG_DISPATCH_TOKEN }}
```

**Step 2: Deploy to ORGAN-V**

Use GitHub API to create the workflow file in `organvm-v-logos/public-process`.

**Step 3: Commit evidence locally**

### Task 6: ORGAN-III Release Trigger Template

**Files:**
- Create: reusable release trigger workflow

**Step 1: Write the workflow**

```yaml
# .github/workflows/notify-feature-released.yml
name: Notify Feature Released

on:
  release:
    types: [published]

jobs:
  notify:
    uses: organvm-vii-kerygma/.github/.github/workflows/notify-kerygma.yml@main
    with:
      event_type: feature-released
      repo_name: ${{ github.event.repository.name }}
      channels: mastodon,discord,bluesky,ghost
    secrets:
      CROSS_ORG_DISPATCH_TOKEN: ${{ secrets.CROSS_ORG_DISPATCH_TOKEN }}
```

**Step 2: Deploy to 3 ORGAN-III repos**

Push to: `public-record-data-scrapper`, `fetch-familiar-friends`, `tab-bookmark-manager`.

### Task 7: Dispatch Log Workflow

**Files:**
- Create: `.github/.github/workflows/dispatch-log.yml`
- Create: `.github/docs/dispatch-log.md` (initial empty table)

**Step 1: Create initial dispatch log**

```markdown
# Dispatch Log

| Timestamp | Event | Source Repo | Channels | Status |
|-----------|-------|-------------|----------|--------|
```

**Step 2: Write the workflow**

```yaml
name: Dispatch Log

on:
  repository_dispatch:

jobs:
  log:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Append to dispatch log
        env:
          EVENT_TYPE: ${{ github.event.action }}
          REPO_NAME: ${{ github.event.client_payload.repo_name }}
          CHANNELS: ${{ github.event.client_payload.channels }}
        run: |
          TIMESTAMP=$(date -u +"%Y-%m-%d %H:%M UTC")
          echo "| $TIMESTAMP | \`$EVENT_TYPE\` | \`${REPO_NAME:-unknown}\` | ${CHANNELS:-default} | received |" >> docs/dispatch-log.md

      - name: Commit log update
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add docs/dispatch-log.md
          git diff --cached --quiet || git commit -m "log: ${{ github.event.action }} dispatch received"
          git push
```

**Step 3: Commit**
```bash
git add .github/workflows/dispatch-log.yml docs/dispatch-log.md
git commit -m "feat: add dispatch log — auto-records all cross-organ events"
```

### Task 8: Push Phase II + Manual Secret Setup

> **MANUAL:** Add `CROSS_ORG_DISPATCH_TOKEN` (PAT with `repo` scope) as an org-level secret across all orgs that need to trigger ORGAN-VII.

```bash
cd /Users/4jp/Workspace/organvm-vii-kerygma/.github
git push origin main
```

---

## Phase III: AUTONOMIA — Self-Running Loop

### Task 9: Cron RSS Auto-Dispatch Workflow

**Files:**
- Create: `.github/.github/workflows/rss-auto-dispatch.yml`

**Step 1: Write the workflow**

```yaml
name: RSS Auto-Dispatch

on:
  schedule:
    - cron: '0 */6 * * *'  # Every 6 hours
  workflow_dispatch:  # Manual trigger for testing

jobs:
  poll-and-dispatch:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install packages
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          pip install "git+https://${GH_TOKEN}@github.com/organvm-vii-kerygma/announcement-templates.git"
          pip install "git+https://${GH_TOKEN}@github.com/organvm-vii-kerygma/social-automation.git"
          pip install "git+https://${GH_TOKEN}@github.com/organvm-vii-kerygma/distribution-strategy.git"
          pip install pyyaml feedparser

      - name: Poll and dispatch
        env:
          KERYGMA_MASTODON_ACCESS_TOKEN: ${{ secrets.KERYGMA_MASTODON_ACCESS_TOKEN }}
          KERYGMA_DISCORD_WEBHOOK_URL: ${{ secrets.KERYGMA_DISCORD_WEBHOOK_URL }}
          KERYGMA_BLUESKY_HANDLE: ${{ secrets.KERYGMA_BLUESKY_HANDLE }}
          KERYGMA_BLUESKY_APP_PASSWORD: ${{ secrets.KERYGMA_BLUESKY_APP_PASSWORD }}
          KERYGMA_GHOST_API_URL: ${{ secrets.KERYGMA_GHOST_API_URL }}
          KERYGMA_GHOST_ADMIN_API_KEY: ${{ secrets.KERYGMA_GHOST_ADMIN_API_KEY }}
          KERYGMA_LIVE_MODE: "true"
        run: |
          echo "Polling RSS feed for new entries..."
          python kerygma_pipeline.py poll 2>&1 | tee poll_output.txt

          NEW_COUNT=$(grep -c "^  -" poll_output.txt || true)
          echo "Found $NEW_COUNT new entries."

          if [ "$NEW_COUNT" -gt 0 ]; then
            python kerygma_pipeline.py dispatch \
              --template essay-announce \
              --repo public-process \
              --channels mastodon,discord,bluesky,ghost \
              2>&1 | tee dispatch_output.txt
          fi
```

**Step 2: Commit**
```bash
git add .github/workflows/rss-auto-dispatch.yml
git commit -m "feat: add cron RSS auto-dispatch — polls every 6 hours"
```

### Task 10: Mastodon Metrics Adapter

**Files:**
- Create: `distribution-strategy/kerygma_strategy/mastodon_metrics.py`
- Create: `distribution-strategy/tests/test_mastodon_metrics.py`

**Step 1: Write failing tests**

```python
# tests/test_mastodon_metrics.py
"""Tests for Mastodon engagement metrics pull-back."""
from kerygma_strategy.mastodon_metrics import MastodonMetricsClient, MastodonMetricsConfig


class TestMastodonMetrics:
    def _client(self):
        return MastodonMetricsClient(
            MastodonMetricsConfig(instance_url="https://mastodon.social", access_token="test")
        )

    def test_mock_get_status_metrics(self):
        client = self._client()
        metrics = client.get_status_metrics("12345")
        assert "reblogs_count" in metrics
        assert "favourites_count" in metrics
        assert "replies_count" in metrics

    def test_mock_get_account_stats(self):
        client = self._client()
        stats = client.get_account_stats()
        assert "followers_count" in stats
        assert "statuses_count" in stats

    def test_config_defaults(self):
        config = MastodonMetricsConfig(instance_url="https://x.com", access_token="t")
        assert config.instance_url == "https://x.com"
```

**Step 2:** Run tests, verify fail.

**Step 3: Write implementation**

```python
# kerygma_strategy/mastodon_metrics.py
"""Mastodon engagement metrics pull-back.

Reads boost, favorite, and reply counts for distributed statuses.
Follows live/mock pattern from kerygma_social adapters.
"""
from __future__ import annotations

import json
import urllib.request
import urllib.error
from dataclasses import dataclass
from typing import Any


@dataclass
class MastodonMetricsConfig:
    instance_url: str
    access_token: str


class MastodonMetricsClient:
    def __init__(self, config: MastodonMetricsConfig, live: bool = False) -> None:
        self.config = config
        self._live = live

    def _get(self, path: str) -> dict[str, Any]:
        url = f"{self.config.instance_url}{path}"
        req = urllib.request.Request(url, headers={
            "Authorization": f"Bearer {self.config.access_token}",
        })
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode())

    def get_status_metrics(self, status_id: str) -> dict[str, int]:
        if not self._live:
            return {"reblogs_count": 0, "favourites_count": 0, "replies_count": 0}
        data = self._get(f"/api/v1/statuses/{status_id}")
        return {
            "reblogs_count": data.get("reblogs_count", 0),
            "favourites_count": data.get("favourites_count", 0),
            "replies_count": data.get("replies_count", 0),
        }

    def get_account_stats(self) -> dict[str, int]:
        if not self._live:
            return {"followers_count": 0, "following_count": 0, "statuses_count": 0}
        data = self._get("/api/v1/accounts/verify_credentials")
        return {
            "followers_count": data.get("followers_count", 0),
            "following_count": data.get("following_count", 0),
            "statuses_count": data.get("statuses_count", 0),
        }
```

**Step 4:** Run tests, verify pass.

**Step 5: Commit**
```bash
cd /Users/4jp/Workspace/organvm-vii-kerygma/distribution-strategy
git add kerygma_strategy/mastodon_metrics.py tests/test_mastodon_metrics.py
git commit -m "feat: add Mastodon metrics pull-back adapter"
```

### Task 11: Ghost Metrics Adapter

**Files:**
- Create: `distribution-strategy/kerygma_strategy/ghost_metrics.py`
- Create: `distribution-strategy/tests/test_ghost_metrics.py`

Same pattern as Task 10. Ghost Content API provides:
- `GET /ghost/api/content/posts/?key={content_api_key}` — post list with meta
- Member count via Admin API `GET /ghost/api/admin/members/`
- Use same JWT auth from `kerygma_social.ghost`

Mock mode returns `{"total_posts": 0, "total_members": 0, "email_open_rate": 0.0}`.

**Step 1:** Write tests (3 tests: mock metrics, config defaults, post count).
**Step 2:** Run, verify fail.
**Step 3:** Write implementation.
**Step 4:** Run, verify pass.
**Step 5:** Commit: `feat: add Ghost metrics pull-back adapter`

### Task 12: Weekly Analytics Workflow

**Files:**
- Create: `.github/.github/workflows/weekly-analytics.yml`

```yaml
name: Weekly Analytics Report

on:
  schedule:
    - cron: '0 9 * * 1'  # Monday 09:00 UTC
  workflow_dispatch:

jobs:
  report:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install packages
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          pip install "git+https://${GH_TOKEN}@github.com/organvm-vii-kerygma/announcement-templates.git"
          pip install "git+https://${GH_TOKEN}@github.com/organvm-vii-kerygma/social-automation.git"
          pip install "git+https://${GH_TOKEN}@github.com/organvm-vii-kerygma/distribution-strategy.git"
          pip install pyyaml feedparser

      - name: Generate report
        run: |
          python kerygma_pipeline.py report --period weekly > report.md

      - name: Create report issue
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');
            const report = fs.readFileSync('report.md', 'utf8');
            const date = new Date().toISOString().split('T')[0];
            await github.rest.issues.create({
              owner: context.repo.owner,
              repo: context.repo.repo,
              title: `[Weekly Report] ${date}`,
              body: report,
              labels: ['analytics-report'],
            });
```

**Step 1: Commit**
```bash
git add .github/workflows/weekly-analytics.yml
git commit -m "feat: add weekly analytics report — auto-creates GH issue"
```

### Task 13: Status Badge

**Files:**
- Create: `.github/scripts/update-status-badge.py`
- Create: `.github/docs/status-badge.json`

The script writes a [shields.io endpoint badge JSON](https://shields.io/endpoint) to `docs/status-badge.json`. The dispatch-receiver workflow calls it after each successful dispatch.

```json
{
  "schemaVersion": 1,
  "label": "kerygma pipeline",
  "message": "operational — 0 dispatches",
  "color": "green"
}
```

**Step 1:** Write script that reads delivery log + updates badge JSON.
**Step 2:** Add a step to `dispatch-receiver.yml` that runs the script and commits.
**Step 3:** Commit: `feat: add dynamic status badge for pipeline health`

### Task 14: Push Phase III

```bash
cd /Users/4jp/Workspace/organvm-vii-kerygma/.github && git push origin main
cd /Users/4jp/Workspace/organvm-vii-kerygma/distribution-strategy && git push origin main
```

---

## Phase IV: SPECTACULUM — The Public Face

### Task 15: Ghost Theme Scaffold

**Files:**
- Create: `.github/organvm-theme/` directory with Ghost theme structure

Ghost themes use Handlebars. Minimal required files:
```
organvm-theme/
  package.json
  index.hbs          # Homepage
  post.hbs           # Single post
  default.hbs        # Base layout
  assets/
    css/
      screen.css     # Main stylesheet
    js/
      main.js        # Minimal JS (syntax highlighting)
  partials/
    header.hbs
    footer.hbs
    navigation.hbs
```

**Step 1:** Create `package.json` with Ghost theme metadata.
**Step 2:** Create `default.hbs` layout (dark theme, organ accent colors).
**Step 3:** Create `screen.css` — dark mode, typography, responsive grid, organ color variables.
**Step 4:** Create `index.hbs` — post grid, subscribe CTA, eight-organ links.
**Step 5:** Create `post.hbs` — article layout with syntax highlighting, share buttons.
**Step 6:** Create partials (header, footer, navigation).
**Step 7:** Commit: `feat: add organvm Ghost theme — dark mode, organ colors, responsive`

### Task 16: Theme Upload Script

**Files:**
- Create: `.github/scripts/deploy-ghost-theme.py`

Zips the `organvm-theme/` directory and uploads via Ghost Admin API `POST /ghost/api/admin/themes/upload/`.

**Step 1:** Write the script.
**Step 2:** Commit: `feat: add Ghost theme deploy script`

### Task 17: Landing Page Configuration

Create a Ghost page (via Admin API) that serves as the hub landing page:
- Eight-organ visual section
- Newsletter subscribe embed
- Social links
- Portfolio highlights

**Step 1:** Write `scripts/deploy-landing-page.py` that creates/updates the Ghost page via API.
**Step 2:** Commit: `feat: add landing page deploy script`

### Task 18: Profile Sync Script

**Files:**
- Create: `.github/scripts/sync-platform-profiles.py`

Updates GitHub org descriptions to reference the Ghost hub URL. Uses `gh api` to PATCH each org's profile.

**Step 1:** Write script.
**Step 2:** Commit: `feat: add platform profile sync script`

### Task 19: Push Phase IV + Final Validation

```bash
cd /Users/4jp/Workspace/organvm-vii-kerygma/.github && git push origin main
```

Run full test suite across all packages:
```bash
cd /Users/4jp/Workspace/organvm-vii-kerygma/social-automation && pytest tests/ -q
cd /Users/4jp/Workspace/organvm-vii-kerygma/announcement-templates && pytest tests/ -q
cd /Users/4jp/Workspace/organvm-vii-kerygma/distribution-strategy && pytest tests/ -q
cd /Users/4jp/Workspace/organvm-vii-kerygma && pytest tests/ -q
```

### Task 20: Registry Update

Update `registry-v2.json` ORGAN-VII entries:
- Update descriptions to mention IGNIS PERPETUUS sprint
- Update test counts
- Set `last_validated` to current date
- Note autonomous loop, cross-organ wiring, Ghost theme

---

## Verification Checklist

- [ ] `scripts/validate-live-config.py` reports all endpoints OK
- [ ] First live dispatch shows 4 PUBLISHED in delivery log
- [ ] `notify-kerygma.yml` callable as `workflow_call` from other orgs
- [ ] ORGAN-V essay push triggers automatic ORGAN-VII distribution
- [ ] `dispatch-log.md` updates automatically on each received event
- [ ] RSS cron workflow triggers successfully (manual `workflow_dispatch` test)
- [ ] Mastodon + Ghost metrics adapters pass tests
- [ ] Weekly report workflow creates a GitHub issue
- [ ] Ghost theme renders correctly
- [ ] All test suites pass (75 + 83 + 58+ + 11+)
