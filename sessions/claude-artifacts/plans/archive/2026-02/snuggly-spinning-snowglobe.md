# Plan: GitHub Pages Interactive Pitch Deck

## Context

The Ephemera Engine project has a complete design corpus (DESIGN, STRATEGY, RESEARCH, PRD, EVALUATION), a working artifact rendering pipeline, 7 SpecKit specs, and 226 planned implementation tasks. The user wants a GitHub Pages web application that functions as an interactive pitch deck — showcasing the project to potential partners, investors, and clients through animation and interaction.

No GitHub Pages config currently exists. The existing design system (3 color themes, Playfair Display/Lora/JetBrains Mono typography, CSS-only textures) should be reused directly.

## Technology

**Single `index.html` file. No build step. No framework.**

- Vanilla HTML/CSS/JS with all styles inlined
- GSAP + ScrollTrigger from CDN (~38KB) for scroll-driven animations and section pinning
- Google Fonts (same import as existing `artifacts/design-system/typography.css`)
- Total page weight: ~133KB (HTML/CSS/JS inline + CDN assets)
- Fully readable without JS (animations are progressive enhancement)
- `prefers-reduced-motion` respected — all animations disabled when set

**Why not a framework:** This is a 10-section scrolling document, not an application. No state, no routing, no interactivity beyond scroll triggers.

## File Structure

```
docs/pitch-deck/
  index.html          # Complete self-contained pitch deck
  README.md           # Brief description + live URL
.github/workflows/
  deploy-pitch-deck.yml  # GitHub Pages deployment (new)
```

Deploy from `docs/pitch-deck/` on `main` via GitHub Actions. URL: `https://organvm-iii-ergon.github.io/parlor-games--ephemera-engine/`

## Narrative Arc (10 Sections)

| # | Section | Theme | Key Content | Animation |
|---|---------|-------|-------------|-----------|
| 0 | **Hero** | personal-letter + texture-aged | Wax seal, title, tagline, "4 games, 3 phases, beautiful artifacts" | Seal bounce, title fade-up, scroll indicator |
| 1 | **Problem** | neutral-dark | 20% lonely, 160% dinner party search growth, $12.7B escape rooms | Stat counters roll on scroll, pinned section |
| 2 | **Solution** | personal-letter + texture-aged | Three-phase structure SVG timeline (Preparation → Game Night → Post-Game) | SVG line draw, nodes appear sequentially |
| 3 | **Confession Album** | confession-album + texture-parchment | Game description, Aron et al. citation, artifact miniature | Split layout, mini slides in from below |
| 4 | **Murder Mystery** | murder-mystery + texture-noir | Game description, setting seed teaser, CLASSIFIED stamp, dossier miniature | Spotlight reveal, stamp slam, typewriter text |
| 5 | **Artifacts** | personal-letter + texture-aged | Side-by-side album vs dossier features, stat badges (A5, PDF, CSS, 3 themes) | Columns slide in from edges, badges pop |
| 6 | **Competitive Landscape** | neutral-dark | 6-row comparison table (vs Jackbox, WNRS, Mystery Night, Night of Mystery) | Table rows stagger in, gold checkmarks pulse |
| 7 | **Design Depth** | personal-letter + texture-aged | ~2700 lines PRD, ~270 citations, 45 screens, 226 tasks, 7 specs, 8.7/10 score | Counters roll, 4 constitution seal stamps |
| 8 | **Market** | neutral-dark | $12.7B, $281B, 24.23% CAGR, target audience, V1 pricing ($9.99) | Stats cascade, pricing reveal |
| 9 | **CTA** | personal-letter + texture-aged | "Let's make the evening unforgettable", looking for (partners, collaborators, adopters), GitHub link | Seal bounce, list stagger |

## CSS Architecture (6 Layers, All Inlined)

1. **Design Tokens** — verbatim from `artifacts/design-system/tokens.css` + new `neutral-dark` theme
2. **Typography** — verbatim from `artifacts/design-system/typography.css`
3. **Textures** — verbatim from `artifacts/design-system/textures.css`
4. **Macro Components** — adapted from `artifacts/templates/_macros.njk`: wax seal, classified stamp, dividers, ornaments, era badge, stat cards (units changed from mm to viewport)
5. **Pitch Deck Layout** — new: `.slide`, `.slide__inner`, `.hero-title`, `.stat-number`, `.stats-row`, `.split`, `.comparison-table`, `.artifact-mini`, `.constitution-seals`, `.scroll-indicator`, `.progress-bar`
6. **Responsive** — tablet (≤1024px: split → single column), mobile (≤640px: no pinning, smaller artifacts), `prefers-reduced-motion`

## Animation Strategy

- **Section pinning** (desktop only): Sections with `data-pin-duration` are pinned while internal animations play via ScrollTrigger
- **Stat counters**: GSAP tweens `{ val: 0 }` to target, updates `textContent` via `onUpdate`
- **Stagger reveals**: `.anim-up` elements fade in + rise 30px on scroll-enter
- **SVG line draw**: `stroke-dashoffset` animation for the three-phase timeline
- **Classified stamp**: Scale 3→1, rotate -25→-15deg, opacity 0→0.7
- **Constitution seals**: Scale 2.5→1, rotate -10→0, staggered 0.15s
- **Progress bar**: Fixed top, `scaleX` scrubbed to overall scroll position
- **Mobile**: No pinning, animations still trigger on scroll-enter via Intersection Observer

## Key Source Files to Reuse

| What | Source |
|------|--------|
| Color tokens, spacing, type scale, 3 themes | `artifacts/design-system/tokens.css` |
| Font imports, hierarchy, special styles | `artifacts/design-system/typography.css` |
| 5 CSS-only textures | `artifacts/design-system/textures.css` |
| Wax seal, stamp, dividers, ornaments, stat cards | `artifacts/templates/_macros.njk` |
| Market data, competitive landscape, pricing | `docs/STRATEGY.md` |
| Research citation (Aron et al.) | `docs/RESEARCH.md` |
| Design principles, game descriptions | `docs/DESIGN.md` |
| Evaluation score, stats | `docs/EVALUATION.md` |
| Constitution gates | `memory/constitution.md` |
| Album cover styling | `artifacts/templates/confession-album/the-album.njk` |
| Dossier cover styling | `artifacts/templates/murder-mystery/the-dossier.njk` |
| Murder mystery seed data | `content/murder-mystery-seeds/curated-seeds.yaml` |
| CI workflow pattern | `.github/workflows/ci.yml` |

## GitHub Actions Workflow

New file `.github/workflows/deploy-pitch-deck.yml`:
- Triggers on push to `main` when `docs/pitch-deck/**` changes + manual dispatch
- Uses `actions/configure-pages@v5`, `actions/upload-pages-artifact@v3`, `actions/deploy-pages@v4`
- Serves `docs/pitch-deck/` directory
- **One-time setup**: Repository Settings → Pages → Source → "GitHub Actions"

## Implementation Sequence

### Phase 1: Scaffold (~1-2h)
1. Create `docs/pitch-deck/index.html` with HTML skeleton, meta tags, Google Fonts
2. Inline design system CSS (tokens + typography + textures) verbatim
3. Add pitch-deck-specific CSS (layout, components, responsive)
4. Verify themes render correctly in browser

### Phase 2: Content (~2-3h)
5. Write all 10 sections' HTML with correct themes and textures
6. Build artifact miniatures (album cover, dossier cover) as inline HTML/CSS
7. Build SVG timeline, comparison table, stats grids, constitution seals
8. Verify: full page reads correctly as static document, all content present

### Phase 3: Animation (~3-4h)
9. Add GSAP initialization, reduced-motion guard, progress bar
10. Implement section pinning with mobile breakpoint disable
11. Add all section-specific animations (counters, reveals, stamps, draws)
12. Test full scroll-through

### Phase 4: Polish (~1-2h)
13. Test responsive (1024px, 640px), verify pinning disabled on mobile
14. Add `aria-label` and `aria-hidden` attributes
15. Cross-browser test (Chrome, Safari, Firefox)

### Phase 5: Deploy (~30min)
16. Create `.github/workflows/deploy-pitch-deck.yml`
17. Create `docs/pitch-deck/README.md`
18. Enable GitHub Pages (Settings → Pages → GitHub Actions)
19. Push, verify deployment
20. Add pitch deck link to root `README.md` documentation table

## Verification

1. Open `docs/pitch-deck/index.html` locally in browser — all content visible, themes correct
2. Scroll through — all 10 sections animate, counters roll, timeline draws, stamps slam
3. Toggle `prefers-reduced-motion` in dev tools — all animations disabled, content still visible
4. Test at 640px viewport — no pinning, single-column layouts, smaller artifacts
5. After push: verify GitHub Actions workflow succeeds, site loads at expected URL
6. Lighthouse audit: aim for 90+ Performance, 100 Accessibility
