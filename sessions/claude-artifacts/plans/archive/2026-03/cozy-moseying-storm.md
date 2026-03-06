# Plan: Stripe Issue + Free Deployment Strategy Diversification

## Context

We've deployed 12 products across Netlify (11 sites) and Render (4 web services + 1 Redis). We're consuming shared free-tier credits on both platforms. Before deploying more, we need to diversify hosting to avoid hitting limits. Separately, Stripe integration needs to be tracked as an issue.

## Part 1: Create GitHub Issue for Stripe Integration

Create an issue on `organvm-iii-ergon/a-mavs-olevm` (or the appropriate repo) tracking the Stripe Payment Link / tip jar setup for etceter4. This unblocks omega criteria #9 and #10.

**Issue content:**
- Title: `feat: add Stripe Payment Link for tip jar (omega #9/#10)`
- Body: Steps to set up Stripe account, create Payment Link (pay-what-you-want), update the existing "SUPPORT US" footer link in `index.html` (line 718) from Bandcamp to Stripe, add to mobile menu
- Labels: `enhancement`, `omega`

## Part 2: Deployment Platform Diversification

### Current Platform Usage

| Platform | Used | Free Limit | Headroom |
|----------|------|-----------|----------|
| **Netlify** | 11 sites | Unlimited sites, 300 credits/month | Credits OK for low-traffic static sites, but adding many more increases risk |
| **Render Web Services** | 4 services | 750 compute hrs/month | Oversubscribed (4 × 744 = 2,976 hrs), saved by auto-sleep. Adding more is risky |
| **Render Redis** | 1 instance | 1 per workspace | **FULL** |
| **Render Static Sites** | 0 | Unlimited, no compute cost | Untapped |
| **Neon PostgreSQL** | 2 projects | 10 projects free | 8 remaining |
| **GitHub Pages** | 0 | Unlimited (public repos only) | Fully untapped |
| **Cloudflare Pages** | 0 | Unlimited sites, unlimited bandwidth, 500 builds/month | Fully untapped |

### Recommended Platform Assignments

**Cloudflare Pages** — Primary platform for new static site deployments. Unlimited sites, unlimited bandwidth, 500 builds/month. Best free tier available.

Deploy via CLI:
```bash
npm install -g wrangler
wrangler pages project create <name>
wrangler pages deploy dist/
```

Or connect Git repos in Cloudflare dashboard for auto-deploy on push.

**GitHub Pages** — For public repos that are docs/specs (no build step or simple Jekyll/static). Free, already integrated with GitHub.

Deploy via GitHub Actions workflow:
```yaml
# .github/workflows/pages.yml
name: Deploy to GitHub Pages
on:
  push:
    branches: [main]
permissions:
  pages: write
  id-token: write # allow-secret
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/configure-pages@v4
      - uses: actions/upload-pages-artifact@v3
        with:
          path: dist/  # or docs/ for spec repos
      - uses: actions/deploy-pages@v4
```

**Render Static Sites** — For sites that need to coexist with Render backend services (e.g., frontends that talk to Render APIs). Static sites on Render are free and do NOT consume compute hours.

**Keep existing Netlify sites as-is** — No migration. They work, they're low-traffic, credit cost is minimal.

### Deployment Map for Remaining Repos

#### Wave 5: Cloudflare Pages (static Vite SPAs)

| Repo | Stack | Notes |
|------|-------|-------|
| `gamified-coach-interface` | Vite + Three.js | Frontend only; Python backend skipped for MVP |
| `tab-bookmark-manager` | Vite frontend | Chrome extension backend skipped; deploy landing/dashboard page |
| `the-actual-news` | Next.js (`apps/public-web`) | Static export of frontend; gateway services not deployed |
| `my-block-warfare` | Vite prototypes | Two sub-apps: `mcp-maps-3d`, `spatial-understanding`. May need `GEMINI_API_KEY` as build env |

For each:
```bash
cd <repo>
npm install && npm run build
wrangler pages project create <site-name>
wrangler pages deploy dist/
```
Then update seed.yaml + registry.

#### Wave 6: GitHub Pages (public spec/docs repos)

| Repo | Content | Deploy Method |
|------|---------|---------------|
| `card-trade-social` | Hydra Platform TCG marketplace specs | GitHub Actions → Pages (build TypeScript docs or serve README as site) |
| `hokage-chess` | Chess variant design docs | GitHub Actions → Pages |
| `your-fit-tailored` | Circular apparel subscription specs | GitHub Actions → Pages |
| `multi-camera--livestream--framework` | 4K livestream pipeline docs | GitHub Actions → Pages (documentation site) |

For each:
1. Enable GitHub Pages in repo Settings → Pages → Source: GitHub Actions
2. Add `.github/workflows/pages.yml` (template above)
3. Build step: if spec-only, serve docs/ or README as static site; if TypeScript, run `tsc` and serve output

#### Wave 7: Render Static Sites (frontend + Render backend pairs)

| Repo | Notes |
|------|-------|
| `public-record-data-scrapper` frontend | Currently on Netlify. Could migrate to Render Static to co-locate with `ucc-mca-api`. **Optional** — only if Netlify credits become a concern. |
| `life-my--midst--in` frontend | Currently on Render as a web service (consuming compute hours). Could convert to Render Static Site to save compute. **Recommended** — frees up ~744 hrs/month of compute budget. |

#### Not Deployable (skip)

| Repo | Reason |
|------|--------|
| `anon-hookup-now` | Android APK, not a web deployment |
| `universal-mail--automation` | Python CLI, no frontend |
| `my--father-mother` | Local macOS clipboard tool |
| `select-or-left-or-right-or` | Private repo, minimal value |
| `a-i-chat--exporter` | Browser extension — distribute via Chrome Web Store, not hosting |
| `commerce--meta` | Private governance docs |
| `peer-audited--behavioral-blockchain` | Needs NestJS + 2nd Redis + Postgres — blocked by Render free tier. Defer until budget allows. |
| `parlor-games--ephemera-engine` | Spec-only, no build output |

### Execution Order

1. **Create Stripe GitHub issue** (Part 1)
2. **Install `wrangler` CLI** and authenticate with Cloudflare
3. **Wave 5**: Deploy 4 repos to Cloudflare Pages
4. **Wave 6**: Enable GitHub Pages on 4 spec/docs repos
5. **Wave 7** (optional): Migrate `life-my--midst--in` frontend to Render Static Site to reclaim compute hours
6. Update seed.yaml + registry-v2.json + superproject pointers after each wave

### Platform Summary After All Waves

| Platform | Sites | Purpose |
|----------|-------|---------|
| Netlify | 11 | Existing static SPAs (no changes) |
| Cloudflare Pages | 4 | New static SPA deployments |
| GitHub Pages | 4 | Public spec/docs repos |
| Render Web Services | 3-4 | Backend APIs only |
| Render Static Sites | 0-1 | Optional frontend co-location |
| Neon | 2 | PostgreSQL databases |

Total deployed products: **~23** (up from 12)

## Verification

After each wave:
1. `curl -s -o /dev/null -w "%{http_code}" <url>` — expect 200
2. Update `seed.yaml` with `deployment_url`
3. Update `registry-v2.json` with `deployment_url`
4. Sync superproject pointers
5. Commit + push all changes

## Files Modified

- `organvm-iii-ergon/a-mavs-olevm` — GitHub issue (Stripe)
- `<repo>/seed.yaml` — deployment_url per repo
- `<repo>/.github/workflows/pages.yml` — GitHub Pages workflow (Wave 6 repos)
- `meta-organvm/organvm-corpvs-testamentvm/registry-v2.json` — deployment URLs + statuses
- Superproject pointer commits across ORGAN-III, META
