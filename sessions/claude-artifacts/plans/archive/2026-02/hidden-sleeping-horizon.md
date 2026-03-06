# Plan: Fix GitHub Pages Build Failure

## Context

The pitch deck was committed to `docs/pitch/index.html` and GitHub Pages was configured to serve from `/docs` on `main`. The legacy Jekyll build has been stuck in "building" for 2+ hours (since `20:19:50Z`), and the previous build also errored. Earlier builds that used `path: /` (root) succeeded fine.

**Root cause**: GitHub Pages legacy builds use Jekyll by default. The `/docs` directory contains raw markdown files (`OPERATOR_RUNBOOK.md`, `roadmap.md`) and subdirectories with non-Jekyll content. Without a `.nojekyll` bypass file, Jekyll tries to process everything and fails. There's also no `index.html` at the `/docs` root — only in `/docs/pitch/`.

## Files to Create

### 1. `docs/.nojekyll` (empty file)
Tells GitHub Pages to skip Jekyll processing entirely and serve static files as-is. This is the standard fix for non-Jekyll Pages sites.

### 2. `docs/index.html` (redirect)
A minimal HTML redirect from the `/docs` root to `/pitch/`. This ensures:
- Visitors hitting the base URL get redirected to the pitch deck
- GitHub Pages has a valid root `index.html` to serve
- Uses `<meta http-equiv="refresh">` + JS fallback

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="0;url=pitch/">
  <title>Redirecting...</title>
</head>
<body>
  <p>Redirecting to <a href="pitch/">ARC4N Pitch Deck</a>...</p>
  <script>window.location.replace("pitch/")</script>
</body>
</html>
```

## Steps

1. Create `docs/.nojekyll` (empty file)
2. Create `docs/index.html` (redirect to `pitch/`)
3. Commit both files
4. Push to `origin/main`
5. Verify the Pages build succeeds via `gh api`

## Verification

1. `gh api repos/ivviiviivvi/nexus--babel-alexandria-/pages/builds --jq '.[0]'` shows `status: "built"`
2. `https://organvm-i-theoria.github.io/nexus--babel-alexandria/` redirects to `/pitch/`
3. `https://organvm-i-theoria.github.io/nexus--babel-alexandria/pitch/` loads the pitch deck
