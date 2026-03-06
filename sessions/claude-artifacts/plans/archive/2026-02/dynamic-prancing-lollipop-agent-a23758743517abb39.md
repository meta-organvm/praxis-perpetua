# Pitch Deck Analysis: Three ORGANVM Pitch Decks

Comparative structural, technical, and design analysis of three GitHub Pages pitch decks.

---

## 1. STYX -- The Blockchain of Truth (Peer-Audited Behavioral Blockchain)

**URL:** `https://organvm-iii-ergon.github.io/peer-audited--behavioral-blockchain/`
**Organ:** III (Ergon / Commerce)

### Framework & Libraries

| Layer | Technology |
|-------|-----------|
| **UI Framework** | React 18 (production build) |
| **Build Tool** | Vite (modulepreload, hashed asset filenames `index-C1O4pFhU.js`) |
| **CSS Framework** | Tailwind CSS (full utility class output in CSS bundle) |
| **Generative Art** | p5.js (~180 references in bundle -- sketch canvases behind each slide section) |
| **3D** | three.js (~20 references -- likely used for a specific visualization) |
| **Icons** | lucide-react (6 references) |
| **Animation** | CSS transitions + IntersectionObserver-based reveal animations (vanilla). No GSAP. Custom `[data-reveal]`, `[data-reveal-left]`, `[data-reveal-scale]` data attributes with CSS transition classes. |
| **Fonts** | Google Fonts: Inter (400-900), JetBrains Mono (400-700) |

### Content Structure

- **SPA architecture**: Single `<div id="root">` mount point. All content rendered by React.
- **Slide-based vertical scroll**: Each section is a full-viewport "slide" (`min-height: 80vh` / `100vh`). Contains hero, section slides, and CTA.
- **Navigation**: Fixed right-side dot navigation (`#nav-dots`) tracking current section via IntersectionObserver.
- **Expandable sections**: Accordion/expandable UI components for detailed content.
- **Sketch stages**: p5.js canvas backgrounds behind certain section dividers (`.sketch-stage` elements with large section numbers as overlays).

### Data Sources

- **Hardcoded in React components**: All content (stats, flow steps, Q&A blocks, callouts) is baked into the JSX component tree within the bundle. No external JSON, no API calls, no frontmatter.
- **Stat cards** with values, labels, and source citations are inline.
- **Content cards** with bullet lists are inline.

### Visual / Animation Style

- **Dark mode**: Near-black background (`#0a0a0f`), light text (`#e2e8f0`), lime-green accent (`#a3e635`).
- **Palette**: `--paper: #0a0a0f`, `--accent: #a3e635`, `--muted: #64748b`. Fintech/blockchain aesthetic.
- **Typography**: Serif headings (Palatino Linotype / Book Antiqua / Georgia), sans body (Inter), mono for labels (JetBrains Mono). Three-font system.
- **Animations**: Scroll-triggered reveals via IntersectionObserver (translateY, opacity, scale). Staggered children with 150ms delays. Bounce animation on scroll hint. Reduced motion support via `@media(prefers-reduced-motion)`.
- **Generative backgrounds**: p5.js canvases render behind slide divider sections. Canvas overlays with large translucent section numbers.
- **Cards/borders**: 12px radius, 1px lime-tinted borders, dark surface backgrounds. Callout blocks with left accent border.
- **Flow diagrams**: Inline step-arrow-step layouts (`.flow-steps`, `.flow-arrow`).

### File Size & Complexity

| Asset | Gzipped | Uncompressed |
|-------|---------|-------------|
| `index.html` | ~522 B | 918 B |
| `index-C1O4pFhU.js` | 335 KB | 1,257 KB (1.26 MB) |
| `index-DJFROXte.css` | ~3.3 KB | 11.6 KB |
| **Total transfer** | **~339 KB** | **1,269 KB** |

- **Complexity: HIGH**. The 1.26MB uncompressed JS bundle includes React, ReactDOM, p5.js, three.js, lucide-react, and all application code. Most complex of the three by a wide margin. Build tooling (Vite) means this was a proper development project with source files, not a single-file artifact.

---

## 2. Ephemera Engine -- Unrepeatable Parlor Games

**URL:** `https://organvm-iii-ergon.github.io/parlor-games--ephemera-engine/`
**Organ:** III (Ergon / Commerce)

### Framework & Libraries

| Layer | Technology |
|-------|-----------|
| **UI Framework** | None (vanilla HTML, no JS framework) |
| **Animation** | GSAP 3.12.5 + ScrollTrigger (loaded from cdnjs CDN) |
| **CSS** | All inline in `<style>` tag (~937 lines of custom CSS). No framework. |
| **Fonts** | Google Fonts: Playfair Display (700), Lora (400/700/italic), JetBrains Mono |
| **Build Tool** | None. Single static HTML file. |

### Content Structure

- **Single HTML file**: All CSS inline in `<head>`, all JS inline at bottom of `<body>`, plus two CDN `<script>` tags for GSAP.
- **10 full-viewport slides**: Hero, Problem, Solution, Game I (Confession Album), Game II (Murder Mystery), Game III (Whose Memory?), Game IV (Exquisite Corpse), Artifacts, Competitive Landscape, Design Depth, Market, CTA.
- **Themed sections**: Each slide applies a `data-theme` attribute that swaps CSS custom properties. 6 themes defined: `confession-album` (cream/green), `murder-mystery` (dark/red), `personal-letter` (warm/brown), `whose-memory` (blue/kraft), `exquisite-corpse` (white/violet), `neutral-dark` (black/gold).
- **Split layouts**: Two-column grids with game descriptions + artifact miniature card previews.
- **Progress bar**: Fixed top progress bar that fills with scroll position (GSAP scrub).
- **Comparison table**: Competitive landscape table with checkmarks.
- **Pricing card**: Single pricing block ($9.99 one-time).

### Data Sources

- **100% hardcoded HTML**: All content is static HTML. Statistics use `data-count`, `data-prefix`, `data-suffix`, `data-decimals` attributes that GSAP animates (counter effect). No JSON, no API, no frontmatter.
- **Statistics**: Loneliness stats, market data, design corpus metrics all inline.
- **Citations**: Academic references (Aron et al., 1997; Gallup 2023) inline.

### Visual / Animation Style

- **Warm editorial aesthetic**: Parchment textures (CSS `::before` pseudo-elements with radial gradients), wax seal components, ornamental dividers (fleurons, dots), classified stamps. Victorian/literary design language.
- **Theme-shifting**: Background and accent colors change per section via `data-theme`. Transitions from warm cream to noir black to blue to violet and back.
- **Typography**: Playfair Display (headings) + Lora (body) + JetBrains Mono (metadata). Classic editorial stack. Small caps, letterspacing, uppercase labels.
- **GSAP animations**: ScrollTrigger-driven reveals (`anim-up`, `anim-fade`, `anim-left`, `anim-right`), stat counter animations, SVG timeline line-drawing, classified stamp "slam" (scale 3 -> 1 with back easing), table row stagger, wax seal fade-in.
- **Artifact miniatures**: CSS-only card previews of each game's physical artifact (album, dossier, anthology, chapbook) with distinct themed styling.
- **Texture system**: Three CSS textures -- `.texture-parchment` (dot grid), `.texture-aged` (dot grid + vignette), `.texture-noir` (subtle dots + dark vignette). Applied per-section.
- **Macro components**: Wax seals, classified stamps, dividers, ornaments, stat cards -- all CSS-only.
- **Reduced motion**: Full support; all animations disabled, elements shown at final state.

### File Size & Complexity

| Asset | Size |
|-------|------|
| `index.html` (single file) | 59.6 KB |
| GSAP 3.12.5 (CDN) | ~24 KB gzipped |
| ScrollTrigger (CDN) | ~9 KB gzipped |
| Google Fonts | ~variable |
| **Total transfer** | **~93 KB** (excluding fonts) |

- **Complexity: MEDIUM**. Single-file architecture with sophisticated CSS design system (6 layers: tokens, typography, textures, macros, pitch layout, responsive). GSAP is used as progressive enhancement only -- the page is fully readable without JS. 1704 lines total. The design system is the most polished of the three.

---

## 3. ARC4N -- Living Digital Canon (Nexus: Babel-Alexandria)

**URL:** `https://organvm-i-theoria.github.io/nexus--babel-alexandria/pitch/`
**Organ:** I (Theoria / Foundational Theory)

### Framework & Libraries

| Layer | Technology |
|-------|-----------|
| **UI Framework** | None (vanilla HTML + vanilla JS) |
| **Animation** | Vanilla JS: IntersectionObserver + scroll listeners + requestAnimationFrame. No GSAP. |
| **Canvas** | HTML5 Canvas API (hero particle system, CTA particle system, remix card micro-animations). No p5.js, no three.js. |
| **CSS** | All inline in `<style>` tag (~217 lines of minified/semi-minified CSS). No framework. |
| **Fonts** | System fonts only: Palatino Linotype / Book Antiqua / Georgia (serif), IBM Plex Sans (sans), IBM Plex Mono (mono). No Google Fonts CDN -- relies on local installation or system fallbacks. |
| **Build Tool** | None. Single static HTML file. |

### Content Structure

- **Single HTML file**: All CSS in `<head>`, all JS in a single `<script>` block at bottom of `<body>`.
- **11 sections (S0-S10)**: Hero, Problem, Vision/Spiral, Atomization (interactive demo), Evolution (interactive demo), Analysis (9-layer stack), Remix (4 strategies), Seed Texts, Architecture, Value Proposition, CTA.
- **Sticky scroll sections**: Atomization (500vh wrapper with sticky inner) and Evolution (400vh wrapper with sticky inner) use scroll-position-driven content switching. As you scroll, the active tab/level automatically changes.
- **Interactive demos**: Two fully functional demos:
  - **5-Level Atomization**: Decomposes Odyssey text into paragraphs -> sentences -> words -> syllables -> glyph-seeds. Each level rendered as styled units. Glyph-seeds show phonemes, historic forms, visual variants, thematic tags, and future forms.
  - **5-Event Evolution Engine**: Natural Drift, Synthetic Mutation, Phase Shift, Glyph Fusion, Remix -- each transforms the source text differently.
- **Navigation dots**: Fixed right-side dots auto-generated from `section[data-section]` elements.
- **Keyboard navigation**: Arrow keys scroll between sections.

### Data Sources

- **Hardcoded JS constants**: All data embedded as JavaScript objects/arrays at the top of the script block:
  - `GLYPH_POOL`: 25 Unicode symbols (Greek, runic, trigrams)
  - `NATURAL_MAP`: 20+ linguistic sound shift rules (th->thorn, ae->ash, etc.)
  - `SEED_TEXTS`: 5 canonical works (Odyssey, Divine Comedy, Leaves of Grass, Ulysses, Frankenstein) with titles/authors
  - `ANALYSIS_LAYERS`: 9 layer names
  - `REMIX_STRATEGIES`: 4 strategy names
  - `GLYPH_DATA`: 6 characters (A, O, S, T, M, W) with phoneme, historic forms, visual variants, thematic tags, future forms
  - `ODYSSEY_TEXT` + `ODYSSEY_ALT`: Two translations of the Odyssey opening for remix demo
- **Ported algorithms**: `syllabify()` function explicitly noted as "ported from text_utils.py" -- demonstrating the actual codebase logic.

### Visual / Animation Style

- **Light academic aesthetic**: Light paper background (`#f6f8fb`), dark ink text (`#102134`), teal accent (`#0f766e`), indigo glyph color (`#6366f1`), gold accent (`#d4a853`). Shifts to dark (`#0f172a`) for hero and problem sections.
- **Typography**: Palatino Linotype headings (classical), IBM Plex Sans body (technical), IBM Plex Mono labels (code). Academic/institutional feel.
- **Canvas particle systems**: Hero section has floating/rotating Unicode glyph particles with a spiral background. CTA section has particles settling toward center. All rendered with raw Canvas 2D API.
- **Scroll-driven reveals**: Custom IntersectionObserver with staggered delays (150ms per sibling). Elements translate up and fade in.
- **Scroll-driven interactivity**: Atomization and Evolution sections respond to scroll position -- the active tab changes as you scroll through the sticky section.
- **Interactive canvas micro-animations**: Each remix card has a small canvas that animates on hover (interleave bars, thematic blend tiles, temporal layers, glyph collision). Only animates while hovering.
- **Grid layouts**: Pain cards (3-col), metrics (6-col), remix cards (4-col), value cards (3-col), seed text "book spines" (5 items).
- **Book spine component**: Seed texts displayed as vertical book spines with vertical text, gold left border, hover preview popups, and a slow "breathe" animation.
- **Gradient transitions**: Sections smoothly gradient between light and dark backgrounds.
- **Reduced motion**: Full support; all animations/transitions disabled, all elements visible.

### File Size & Complexity

| Asset | Size |
|-------|------|
| `index.html` (single file) | 58.6 KB |
| External dependencies | **None** (zero CDN requests) |
| Google Fonts | None (system fonts only) |
| **Total transfer** | **~58.6 KB** (pre-gzip, likely ~15-20KB gzipped) |

- **Complexity: MEDIUM-HIGH**. Single-file, zero-dependency architecture with the most sophisticated interactivity of the three. 1170 lines total. Contains ported codebase algorithms (syllabification, text atomization), two interactive demos, 6 canvas animations (2 full-screen + 4 micro), scroll-driven tab switching via sticky sections, and keyboard navigation. The most "demo-heavy" of the three despite being the smallest in file size.

---

## Comparative Summary

| Dimension | STYX (Blockchain) | Ephemera Engine | ARC4N (Babel-Alexandria) |
|-----------|--------------------|-----------------|--------------------------|
| **Architecture** | React SPA (Vite build) | Single HTML file | Single HTML file |
| **JS Framework** | React 18 | None | None |
| **Animation Lib** | CSS + IO (vanilla) | GSAP 3.12.5 + ScrollTrigger | Vanilla JS (IO + rAF + scroll) |
| **Canvas/3D** | p5.js + three.js | None | HTML5 Canvas 2D (raw) |
| **CSS Approach** | Tailwind + custom properties | Hand-written design system (6 layers) | Hand-written minified CSS |
| **Fonts** | Google Fonts (Inter, JetBrains Mono) | Google Fonts (Playfair, Lora, JetBrains) | System fonts only (Palatino, IBM Plex) |
| **External Deps** | 5+ npm packages | 2 CDN scripts | Zero |
| **Transfer Size** | ~339 KB | ~93 KB | ~58.6 KB (raw) |
| **Content Sections** | ~12+ slides | 10 slides | 11 sections |
| **Data Source** | Hardcoded in JSX | Hardcoded in HTML | Hardcoded JS constants |
| **Interactivity** | Expandable sections, p5 sketches | Stat counters, SVG draw | 2 interactive demos, scroll-driven tabs, 6 canvases, keyboard nav |
| **Design Aesthetic** | Dark fintech (lime/black) | Warm editorial (parchment/wax seals) | Academic institutional (light/teal/gold) |
| **Theme System** | Single dark theme + custom props | 6 switchable themes per section | Gradient transitions light/dark |
| **Accessibility** | Basic (aria on scroll hint) | Good (aria-labels, role attrs) | Good (aria-labels, role attrs, ARIA live region, keyboard nav) |
| **Reduced Motion** | Yes | Yes | Yes |
| **Build Required** | Yes (Vite + npm) | No | No |

### Key Design Patterns

1. **All three use full-viewport slides** as the primary content unit. Vertical scroll is the navigation metaphor.
2. **All three have fixed dot navigation** on the right side tracking the active section.
3. **All three use scroll-triggered reveal animations** (fade-up, stagger), though via different mechanisms.
4. **All three hardcode their content** -- no CMS, no JSON files, no frontmatter, no API calls.
5. **All three respect `prefers-reduced-motion`** with comprehensive fallbacks.
6. **All three use a three-font type system** (serif heading, sans/serif body, monospace for labels/metadata).

### Complexity Gradient

- **Simplest build**: ARC4N (zero dependencies, single file, system fonts)
- **Middle ground**: Ephemera Engine (single file + 2 CDN scripts, most polished design system)
- **Most complex**: STYX (full React/Vite build pipeline, multiple npm dependencies, largest bundle)

### Most Interesting Pattern

The Ephemera Engine's **per-section theme switching** (`data-theme` attributes cascading CSS custom properties) is the most reusable design pattern. It allows a single page to feel like multiple distinct environments without any JavaScript, using only CSS custom property scoping.

ARC4N's **scroll-driven sticky section demos** (wrapping content in a tall container with a sticky inner that responds to scroll progress) is the most technically interesting interaction pattern -- it creates a "scroll as scrubber" effect for interactive content without any animation library.
