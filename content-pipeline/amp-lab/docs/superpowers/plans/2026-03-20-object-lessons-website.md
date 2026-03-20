# Object Lessons Website Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the full Object Lessons website — an Astro 5.x editorial site with MDX content collections, React interactive islands, Cloudflare D1 submission system, collaborator dashboard, and replicable template architecture.

**Architecture:** Astro in hybrid SSR mode (static pages + Cloudflare Worker API routes). Content lives in MDX collections (episodes, essays, objects) with a YAML film database loaded at build time. Five React islands hydrate for interactive features. Cloudflare D1 stores viewer submissions. Password-gated collaborator dashboard reads/writes D1 via API routes.

**Tech Stack:** Astro 5.x, React 19, TypeScript, Tailwind CSS, MDX, Cloudflare Pages + D1, @tanstack/react-table, Satori + resvg (OG images), Zod

**Spec:** `docs/superpowers/specs/2026-03-20-object-lessons-website-design.md`

---

## File Map

### Configuration & Root
| File | Responsibility |
|------|---------------|
| `astro.config.mjs` | Astro config: integrations (mdx, react, tailwind, sitemap, cloudflare), output mode hybrid |
| `tailwind.config.mjs` | Design tokens: colors, fonts, spacing from spec Section 2 |
| `tsconfig.json` | TypeScript strict mode, path aliases |
| `package.json` | Dependencies, scripts (dev, build, preview, validate) |
| `wrangler.toml` | Cloudflare Pages config, D1 binding |
| `site.config.ts` | Brand: name, tagline, domain, social links, nav items |

### Content & Data (`src/`)
| File | Responsibility |
|------|---------------|
| `src/content/config.ts` | Zod schemas for episodes, essays, objects |
| `src/content/episodes/*.mdx` | 10 episode files (4 V1 + 6 V2) |
| `src/content/essays/*.mdx` | 6 essay files (from research briefs) |
| `src/content/objects/*.mdx` | 10 object files |
| `src/data/films.yaml` | 302+ film database |
| `src/data/pipeline-status.yaml` | Production pipeline state |

### Library (`src/lib/`)
| File | Responsibility |
|------|---------------|
| `src/lib/films.ts` | Load + type films.yaml, export `getFilms()`, `getFilmById()`, `getFilmsByObject()` |
| `src/lib/pipeline.ts` | Load + type pipeline-status.yaml, export `getPipelineStatus()` |
| `src/lib/config.ts` | Re-export site.config.ts typed |
| `src/lib/d1.ts` | D1 client helpers: `createSubmission()`, `getSubmissions()`, `updateSubmission()` |
| `src/lib/auth.ts` | Collaborator auth: `validatePassword()`, `createSession()`, `checkSession()` |

### Layouts (`src/layouts/`)
| File | Responsibility |
|------|---------------|
| `src/layouts/BaseLayout.astro` | HTML shell, `<head>`, SEO component, nav, footer |
| `src/layouts/EssayLayout.astro` | 680px reading column, extends BaseLayout |
| `src/layouts/DataLayout.astro` | 1100px wide for tables/grids, extends BaseLayout |

### Pages (`src/pages/`)
| File | Responsibility |
|------|---------------|
| `src/pages/index.astro` | Home: hero, latest episode, object grid, latest essay |
| `src/pages/episodes/index.astro` | Episode archive grid with V1/V2 filter |
| `src/pages/episodes/[slug].astro` | Episode detail: video, essay, filmography |
| `src/pages/essays/index.astro` | Essay archive with type/object filter |
| `src/pages/essays/[slug].astro` | Essay detail: MDX body, citations |
| `src/pages/objects/index.astro` | Object catalog with status badges |
| `src/pages/objects/[slug].astro` | Object detail: biography, categories, filmography |
| `src/pages/research.astro` | Five mechanisms, dissertation overview, density |
| `src/pages/pipeline.astro` | Pipeline timeline + status |
| `src/pages/submit.astro` | Submission form host |
| `src/pages/about.astro` | Manifesto, team, links |
| `src/pages/collaborator.astro` | Auth-gated dashboard host |
| `src/pages/404.astro` | Custom 404 |
| `src/pages/rss.xml.ts` | RSS feed |
| `src/pages/api/submit.ts` | POST: create submission in D1 |
| `src/pages/api/submissions.ts` | GET: read submissions (auth required) |
| `src/pages/api/submissions/[id].ts` | PATCH: approve/reject (auth required) |
| `src/pages/api/collaborator/auth.ts` | POST: validate password, set cookie |

### Astro Components (`src/components/astro/`)
| File | Responsibility |
|------|---------------|
| `Header.astro` | Site header: brand, tagline |
| `Footer.astro` | Social links, RSS, template credit |
| `Nav.astro` | Navigation bar with active state |
| `EpisodeCard.astro` | Card for episode archives |
| `EssayCard.astro` | Card for essay archives |
| `ObjectCard.astro` | Card for object catalog |
| `StatusBadge.astro` | published / in-production / researching / candidate |
| `YouTubeEmbed.astro` | Lite-youtube facade: thumbnail until click |
| `Citation.astro` | Inline citation marker |
| `Footnote.astro` | Footnote rendering |
| `FilmStill.astro` | Responsive image with caption + alt text |
| `SEO.astro` | Meta tags, JSON-LD, OG tags (includes OG image references from `public/images/og/`) |

### React Islands (`src/components/react/`)
| File | Responsibility |
|------|---------------|
| `FilmographyTable.tsx` | Sortable/filterable film table via @tanstack/react-table |
| `PipelineTimeline.tsx` | Horizontal timeline with status indicators |
| `SubmissionForm.tsx` | Three-tab form with validation |
| `ObjectDensityGraph.tsx` | Co-occurrence visualization |
| `CollaboratorDashboard.tsx` | Auth-gated dashboard: status, submissions, calendar |

### Styles (`src/styles/`)
| File | Responsibility |
|------|---------------|
| `global.css` | @tailwind directives, base typography, prose styles |
| `theme.css` | CSS custom properties consumed by Tailwind config |

### Scripts
| File | Responsibility |
|------|---------------|
| `scripts/validate-categories.ts` | Build-time check: episode categories match object definitions |
| `scripts/generate-og-images.ts` | Pre-render OG images via Satori + resvg |
| `scripts/seed-d1.sql` | D1 schema creation SQL |

---

## Task 1: Project Scaffold + Configuration

**Files:**
- Create: `package.json`, `astro.config.mjs`, `tailwind.config.mjs`, `tsconfig.json`, `site.config.ts`, `wrangler.toml`
- Create: `src/styles/theme.css`, `src/styles/global.css`
- Create: `public/favicon.svg`

- [ ] **Step 1: Initialize Astro project**

```bash
cd /Users/4jp/Workspace/meta-organvm/praxis-perpetua/content-pipeline/amp-lab
mkdir -p object-lessons && cd object-lessons
npm create astro@latest -- --template minimal --no-install --no-git .
```

- [ ] **Step 2: Install all dependencies**

```bash
npm install astro @astrojs/mdx @astrojs/react @astrojs/tailwind @astrojs/sitemap @astrojs/cloudflare @astrojs/rss react@19 react-dom@19 @tanstack/react-table zod yaml
npm install -D @types/react @types/react-dom tailwindcss typescript satori @resvg/resvg-js tsx
```

- [ ] **Step 3: Write `site.config.ts`**

```typescript
// site.config.ts
export const siteConfig = {
  name: 'Object Lessons',
  tagline: 'The Recurring Objects of Cinema',
  domain: 'objectlessons.film',
  url: 'https://objectlessons.film',
  description: 'Tracing recurring objects across a hundred years of film — milk, mirrors, cigarettes, clocks, doors, guns.',
  author: 'Anthony James Padavano',
  socials: {
    youtube: 'https://youtube.com/@AmpLabMedia',
    patreon: '',
    letterboxd: '',
    bluesky: '',
    email: '',
  },
  nav: [
    { label: 'Episodes', href: '/episodes' },
    { label: 'Essays', href: '/essays' },
    { label: 'Objects', href: '/objects' },
    { label: 'Research', href: '/research' },
    { label: 'Pipeline', href: '/pipeline' },
    { label: 'Submit', href: '/submit' },
    { label: 'About', href: '/about' },
  ],
} as const;

export type SiteConfig = typeof siteConfig;
```

- [ ] **Step 4: Write `astro.config.mjs`**

```javascript
// astro.config.mjs
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import react from '@astrojs/react';
import tailwind from '@astrojs/tailwind';
import sitemap from '@astrojs/sitemap';
import cloudflare from '@astrojs/cloudflare';

export default defineConfig({
  site: 'https://objectlessons.film',
  output: 'hybrid',
  adapter: cloudflare({
    platformProxy: { enabled: true },
  }),
  integrations: [
    mdx(),
    react(),
    tailwind(),
    sitemap(),
  ],
});
```

- [ ] **Step 5: Write `tailwind.config.mjs`**

```javascript
// tailwind.config.mjs
/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        surface: 'var(--color-surface)',
        primary: 'var(--color-primary)',
        secondary: 'var(--color-secondary)',
        accent: 'var(--color-accent)',
        link: 'var(--color-link)',
        divider: 'var(--color-divider)',
        'data-bg': 'var(--color-data-bg)',
      },
      fontFamily: {
        serif: ['Lora', 'Georgia', 'Times New Roman', 'serif'],
        sans: ['system-ui', '-apple-system', 'Segoe UI', 'sans-serif'],
        mono: ['JetBrains Mono', 'ui-monospace', 'monospace'],
      },
      maxWidth: {
        reading: '680px',
        content: '1100px',
      },
      typography: {
        DEFAULT: {
          css: {
            maxWidth: '680px',
            lineHeight: '1.8',
            color: 'var(--color-primary)',
            a: { color: 'var(--color-link)' },
          },
        },
      },
    },
  },
  plugins: [],
};
```

- [ ] **Step 6: Write `src/styles/theme.css` and `src/styles/global.css`**

```css
/* src/styles/theme.css */
:root {
  --color-surface: #faf8f5;
  --color-primary: #1a1a1a;
  --color-secondary: #666666;
  --color-accent: #8a7e6e;
  --color-link: #2a4a7a;
  --color-divider: #e0dcd6;
  --color-data-bg: #f0ede8;
  --font-serif: 'Lora', Georgia, 'Times New Roman', serif;
  --font-sans: system-ui, -apple-system, 'Segoe UI', sans-serif;
  --font-mono: 'JetBrains Mono', ui-monospace, monospace;
}
```

```css
/* src/styles/global.css */
@tailwind base;
@tailwind components;
@tailwind utilities;

@import './theme.css';

@layer base {
  body {
    @apply bg-surface text-primary font-sans;
    font-size: 17px;
    line-height: 1.8;
  }
  h1, h2, h3, h4 {
    @apply font-serif;
  }
  h1 { @apply text-4xl font-light tracking-wide; }
  h2 { @apply text-2xl font-normal; }
  h3 { @apply text-xl font-normal; }
  a { @apply text-link underline-offset-2 hover:underline; }
}

@layer components {
  .reading-column {
    @apply max-w-reading mx-auto px-6;
  }
  .content-wide {
    @apply max-w-content mx-auto px-6;
  }
}
```

- [ ] **Step 7: Write `tsconfig.json`**

```json
{
  "extends": "astro/tsconfigs/strict",
  "compilerOptions": {
    "jsx": "react-jsx",
    "jsxImportSource": "react",
    "paths": {
      "@/*": ["./src/*"],
      "@components/*": ["./src/components/*"],
      "@layouts/*": ["./src/layouts/*"],
      "@lib/*": ["./src/lib/*"]
    }
  }
}
```

- [ ] **Step 8: Write `wrangler.toml`**

```toml
# wrangler.toml
name = "object-lessons"
compatibility_date = "2024-12-01"

[[d1_databases]]
binding = "DB"
database_name = "object-lessons-submissions"
database_id = "" # fill after `wrangler d1 create object-lessons-submissions`
```

- [ ] **Step 9: Write D1 seed script**

```sql
-- scripts/seed-d1.sql
CREATE TABLE IF NOT EXISTS submissions (
  id TEXT PRIMARY KEY,
  type TEXT NOT NULL,
  status TEXT DEFAULT 'pending',
  data TEXT NOT NULL,
  submitter_name TEXT,
  submitter_email TEXT,
  created_at TEXT NOT NULL,
  reviewed_at TEXT,
  reviewed_by TEXT
);

CREATE INDEX IF NOT EXISTS idx_submissions_status ON submissions(status);
CREATE INDEX IF NOT EXISTS idx_submissions_type ON submissions(type);
```

- [ ] **Step 10: Write `.gitignore`**

```
node_modules/
dist/
.astro/
.wrangler/
.dev.vars
.superpowers/
```

- [ ] **Step 11: Write placeholder favicon**

Create a minimal SVG favicon — a simple serif "O" (for Object).

- [ ] **Step 12: Verify build**

```bash
npm run dev
# Should start on localhost:4321 with empty site
```

- [ ] **Step 13: Commit**

```bash
git init && git add -A
git commit -m "feat: scaffold Astro project with full configuration

Astro 5.x hybrid mode, Tailwind with editorial design tokens,
Cloudflare Pages + D1 adapter, MDX + React islands configured."
```

---

## Task 2: Content Collections + Data Loaders

**Files:**
- Create: `src/content/config.ts`
- Create: `src/lib/films.ts`, `src/lib/pipeline.ts`, `src/lib/config.ts`
- Create: `src/data/films.yaml` (starter with ~20 films from density report)
- Create: `src/data/pipeline-status.yaml`

- [ ] **Step 1: Write `src/content/config.ts`**

Full Zod schemas for episodes, essays, objects as specified in spec Section 6.3. Include the `kebab` field on symbolic categories.

```typescript
// src/content/config.ts
import { defineCollection, z } from 'astro:content';

const episodes = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    object: z.string(),
    date: z.date(),
    youtube_id: z.string(),
    status: z.enum(['published', 'in-production', 'scripted', 'planned']),
    version: z.enum(['v1', 'v2']),
    duration: z.string().default(''),
    films: z.array(z.string()).default([]),
    symbolic_categories: z.array(z.string()).default([]),
    companion_essay: z.string().optional(),
    thumbnail: z.string().optional(),
    seo: z.object({
      description: z.string(),
      keywords: z.array(z.string()).default([]),
    }),
  }),
});

const essays = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    object: z.string(),
    date: z.date(),
    type: z.enum(['companion', 'standalone', 'research-note']),
    related_episodes: z.array(z.string()).default([]),
    excerpt: z.string(),
    citations: z.array(z.object({
      key: z.string(),
      text: z.string(),
    })).default([]),
  }),
});

const objects = defineCollection({
  type: 'content',
  schema: z.object({
    name: z.string(),
    status: z.enum(['published', 'in-production', 'researching', 'candidate']),
    film_count: z.number(),
    priority_score: z.number().min(1).max(5),
    symbolic_categories: z.array(z.object({
      name: z.string(),
      kebab: z.string(),
      description: z.string(),
    })),
    episodes: z.array(z.string()).default([]),
    essays: z.array(z.string()).default([]),
    co_occurrences: z.array(z.object({
      object: z.string(),
      count: z.number(),
      films: z.array(z.string()),
    })).default([]),
    landmark_scenes: z.array(z.object({
      film: z.string(),
      description: z.string(),
      tier: z.number().min(1).max(3),
    })).default([]),
  }),
});

export const collections = { episodes, essays, objects };
```

- [ ] **Step 2: Write `src/lib/films.ts`**

```typescript
// src/lib/films.ts
import { readFileSync } from 'node:fs';
import { parse } from 'yaml';

export interface FilmScene {
  description: string;
  symbolic_category: string;
  tier: number;
}

export interface FilmObject {
  object: string;
  scenes: FilmScene[];
}

export interface Film {
  id: string;
  title: string;
  year: number;
  director: string;
  objects: FilmObject[];
  density_score: number;
  letterboxd_url?: string;
  imdb_id?: string;
}

let _films: Film[] | null = null;

export function getFilms(): Film[] {
  if (!_films) {
    const raw = readFileSync(new URL('../data/films.yaml', import.meta.url), 'utf-8');
    _films = parse(raw) as Film[];
  }
  return _films;
}

export function getFilmById(id: string): Film | undefined {
  return getFilms().find(f => f.id === id);
}

export function getFilmsByObject(object: string): Film[] {
  return getFilms().filter(f => f.objects.some(o => o.object === object));
}

export function getHighDensityFilms(minDensity: number = 3): Film[] {
  return getFilms().filter(f => f.density_score >= minDensity);
}
```

- [ ] **Step 3: Write `src/lib/pipeline.ts`**

```typescript
// src/lib/pipeline.ts
import { readFileSync } from 'node:fs';
import { parse } from 'yaml';

export interface PipelineObject {
  name: string;
  status: string;
  research_films: number;
  outline: string;
  narration: string;
  edit: string;
  target_release: string;
  notes: string;
}

export interface PipelineStatus {
  current_sprint: string;
  last_updated: string;
  objects: PipelineObject[];
  submissions_pending: {
    objects: number;
    films: number;
    clips: number;
  };
}

export function getPipelineStatus(): PipelineStatus {
  const raw = readFileSync(new URL('../data/pipeline-status.yaml', import.meta.url), 'utf-8');
  return parse(raw) as PipelineStatus;
}
```

- [ ] **Step 4: Write `src/lib/config.ts`**

```typescript
// src/lib/config.ts
export { siteConfig } from '../../site.config';
export type { SiteConfig } from '../../site.config';
```

- [ ] **Step 5: Write starter `src/data/films.yaml`**

Populate with the 13 high-density films from the cross-object density report (A Clockwork Orange, Blade Runner, The Shining, Psycho, etc.) plus a representative sample from each object's research brief. Approximately 20-30 films to start — enough to demonstrate all features. The full 302+ film database is populated during data migration (Task 10).

- [ ] **Step 6: Write `src/data/pipeline-status.yaml`**

```yaml
current_sprint: AMP-LAB-V2
last_updated: "2026-03-20"

objects:
  - name: Milk
    status: narration-complete
    research_films: 71
    outline: complete
    narration: needs-recording
    edit: not-started
    target_release: "2026-05-01"
    notes: "First V2 episode. Strongest opener."
  - name: Mirrors
    status: narration-complete
    research_films: 85
    outline: complete
    narration: needs-recording
    edit: not-started
    target_release: "2026-05-15"
    notes: "Most philosophically loaded. Visual showpiece."
  - name: Cigarettes
    status: narration-complete
    research_films: 74
    outline: complete
    narration: needs-recording
    edit: not-started
    target_release: "2026-06-01"
    notes: "Cultural decline arc IS the story."
  - name: Clocks
    status: narration-complete
    research_films: 69
    outline: complete
    narration: needs-recording
    edit: not-started
    target_release: "2026-06-15"
    notes: "Cinema's most self-referential object."
  - name: Doors
    status: narration-complete
    research_films: 70
    outline: complete
    narration: needs-recording
    edit: not-started
    target_release: "2026-07-01"
    notes: "The object that IS the cut."
  - name: Guns
    status: narration-complete
    research_films: 76
    outline: complete
    narration: needs-recording
    edit: not-started
    target_release: "2026-07-15"
    notes: "The object that IS America."
  - name: Cereal
    status: published
    research_films: 0
    outline: complete
    narration: complete
    edit: complete
    target_release: "2018-01-01"
    notes: "V1 episode. Published."
  - name: Telephones
    status: published
    research_films: 0
    outline: complete
    narration: complete
    edit: complete
    target_release: "2018-06-01"
    notes: "V1 episode. Published."
  - name: Balloons
    status: published
    research_films: 0
    outline: complete
    narration: complete
    edit: complete
    target_release: "2019-01-01"
    notes: "V1 episode. Published."
  - name: Eggs
    status: published
    research_films: 0
    outline: complete
    narration: complete
    edit: complete
    target_release: "2020-01-01"
    notes: "V1 episode. Published."

submissions_pending:
  objects: 0
  films: 0
  clips: 0
```

- [ ] **Step 7: Verify collections load**

```bash
npm run dev
# Check terminal for Astro content collection validation — should show no errors
```

- [ ] **Step 8: Commit**

```bash
git add -A
git commit -m "feat: content collections, data loaders, pipeline status

Zod schemas for episodes/essays/objects, YAML film database loader,
pipeline status loader, starter film data from density report."
```

---

## Task 3: Layouts + Core Astro Components

**Files:**
- Create: `src/layouts/BaseLayout.astro`, `src/layouts/EssayLayout.astro`, `src/layouts/DataLayout.astro`
- Create: all files in `src/components/astro/`

- [ ] **Step 1: Write `src/components/astro/SEO.astro`**

Props: `title`, `description`, `image`, `type` (article/website/video), `jsonLd`. Renders `<title>`, `<meta>` tags, OG tags, Twitter cards, and optional JSON-LD `<script>` block.

- [ ] **Step 2: Write `src/components/astro/Nav.astro`**

Import nav items from `site.config.ts`. Render horizontal nav with active state detection via `Astro.url.pathname`. Semantic `<nav>` with `aria-label`. Links styled with accent color, active link underlined.

- [ ] **Step 3: Write `src/components/astro/Header.astro`**

"Object Lessons" in serif `<h1>` (on home) or linked `<div>` (on inner pages). Tagline in small caps below. Includes `<Nav />`.

- [ ] **Step 4: Write `src/components/astro/Footer.astro`**

Social links from `site.config.ts`. RSS link. "Built with Object Lessons Template" credit. Semantic `<footer>`.

- [ ] **Step 5: Write `src/layouts/BaseLayout.astro`**

Props: `title`, `description`, `image`, `type`, `jsonLd`. Renders `<!DOCTYPE html>`, `<head>` with `<SEO />`, Google Fonts link for Lora, `<body>` with `<Header />`, `<main><slot /></main>`, `<Footer />`. Imports `global.css`.

- [ ] **Step 6: Write `src/layouts/EssayLayout.astro`**

Wraps `BaseLayout`. Adds `<div class="reading-column">` around the slot. Adds essay-specific prose styling.

- [ ] **Step 7: Write `src/layouts/DataLayout.astro`**

Wraps `BaseLayout`. Adds `<div class="content-wide">` around the slot.

- [ ] **Step 8: Write `src/components/astro/StatusBadge.astro`**

Props: `status` (published | in-production | researching | candidate). Renders a `<span>` with color-coded background: green for published, amber for in-production, blue for researching, gray for candidate.

- [ ] **Step 9: Write `src/components/astro/YouTubeEmbed.astro`**

Props: `videoId`, `title`. Lite-youtube facade pattern: renders a clickable thumbnail with play button overlay. On click, replaces with `<iframe>`. No JS loaded until interaction. Responsive 16:9 container. Accessible: button has `aria-label="Play {title}"`.

- [ ] **Step 10: Write `src/components/astro/EpisodeCard.astro`**

Props: episode collection entry. Renders thumbnail (or YouTube poster), title, object name, version badge (V1/V2), status badge, duration, date. Links to `/episodes/{slug}`.

- [ ] **Step 11: Write `src/components/astro/EssayCard.astro`**

Props: essay collection entry. Renders title, object tag, type badge, date, excerpt, related episode link.

- [ ] **Step 12: Write `src/components/astro/ObjectCard.astro`**

Props: object collection entry. Renders name, status badge, film count, priority score. Links to `/objects/{slug}`.

- [ ] **Step 13: Write `src/components/astro/Citation.astro` and `src/components/astro/Footnote.astro`**

Citation: renders inline `[N]` superscript linked to footnote. Footnote: renders numbered footnote at bottom of essay.

- [ ] **Step 14: Write `src/components/astro/FilmStill.astro`**

Props: `src`, `alt`, `caption`, `film`, `year`. Responsive `<figure>` with `<img>`, `<figcaption>`. Alt text required (accessibility).

- [ ] **Step 15: Verify layouts render**

Create a temporary `src/pages/index.astro` that uses `BaseLayout` with placeholder content. Check it renders correctly.

```bash
npm run dev
# Visit localhost:4321 — should show header, nav, footer, placeholder content
```

- [ ] **Step 16: Commit**

```bash
git add -A
git commit -m "feat: layouts and core Astro components

BaseLayout, EssayLayout, DataLayout. Nav, Header, Footer, SEO,
StatusBadge, YouTubeEmbed, EpisodeCard, EssayCard, ObjectCard,
Citation, Footnote, FilmStill components."
```

---

## Task 4: Seed Content — Object Files

**Files:**
- Create: `src/content/objects/{milk,mirrors,cigarettes,clocks,doors,guns,cereal,telephones,balloons,eggs}.mdx`

- [ ] **Step 1: Create all 10 object MDX files**

Each object file has frontmatter matching the Objects schema (name, status, film_count, priority_score, symbolic_categories with kebab keys, episodes, essays, co_occurrences, landmark_scenes) plus an MDX body — a 2-4 paragraph "biography" of the object's career in cinema.

Source data:
- V2 objects (milk, mirrors, cigarettes, clocks, doors, guns): Extract from the existing research briefs in `/Users/4jp/Workspace/meta-organvm/praxis-perpetua/content-pipeline/amp-lab/research--*.md`. Each brief has structured filmography data, symbolic categories, and narrative overviews.
- V1 objects (cereal, telephones, balloons, eggs): Minimal frontmatter with `status: published`, `version: v1`, estimated film counts. Body is a brief placeholder — V1 objects don't have research briefs.

Read each research brief to extract: symbolic categories, film count, landmark scenes (Tier 1 entries), co-occurrence data from the density report.

- [ ] **Step 2: Verify collections load with all 10 objects**

```bash
npm run dev
# Check terminal — Astro should validate all 10 object files against schema
```

- [ ] **Step 3: Commit**

```bash
git add -A
git commit -m "feat: seed 10 object content files

6 V2 objects (milk, mirrors, cigarettes, clocks, doors, guns) with
full symbolic categories and landmark scenes from research briefs.
4 V1 objects (cereal, telephones, balloons, eggs) with minimal data."
```

---

## Task 5: Seed Content — Episode + Essay Files

**Files:**
- Create: `src/content/episodes/{milk,mirrors,cigarettes,clocks,doors,guns,cereal,telephones,balloons,eggs}.mdx`
- Create: `src/content/essays/{milk,mirrors,cigarettes,clocks,doors,guns}-in-cinema.mdx`

- [ ] **Step 1: Create 6 V2 episode files**

Each V2 episode MDX file has frontmatter (title, object, date, youtube_id placeholder, status: scripted, version: v2, duration: TBD, films list, symbolic_categories, companion_essay reference, seo). MDX body: a condensed version of the narration outline (key sections, not the full 30-40K outline).

Source: `/Users/4jp/Workspace/meta-organvm/praxis-perpetua/content-pipeline/amp-lab/episode-outlines/00N-*-narration-outline.md`

- [ ] **Step 2: Create 4 V1 episode files**

V1 episodes with frontmatter: title (using the SEO-optimized titles from the relaunch plan), object, approximate date, youtube_id (placeholder — real IDs need to be looked up), status: published, version: v1. Minimal body — V1 format was pure compilation.

- [ ] **Step 3: Create 6 essay files**

Each essay MDX file has frontmatter (title, object, date, type: companion, related_episodes, excerpt, citations array). MDX body: a public-facing adaptation of the research brief — the narrative sections, symbolic category analysis, and key close readings. Not the full 40-70K research doc — a 3,000-5,000 word essay distilled from the research. Citations extracted from the academic references in each brief.

Source: `/Users/4jp/Workspace/meta-organvm/praxis-perpetua/content-pipeline/amp-lab/research--*.md`

- [ ] **Step 4: Verify all collections load**

```bash
npm run dev
# 10 episodes + 6 essays + 10 objects should all validate
```

- [ ] **Step 5: Commit**

```bash
git add -A
git commit -m "feat: seed episodes and essays from research briefs

10 episodes (4 V1 + 6 V2) with structured frontmatter.
6 companion essays distilled from 580K+ of research docs."
```

---

## Task 6: Static Pages — Home, About, Research, 404

**Files:**
- Create: `src/pages/index.astro`, `src/pages/about.astro`, `src/pages/research.astro`, `src/pages/404.astro`

- [ ] **Step 1: Write `src/pages/index.astro` (Home)**

Uses `BaseLayout`. Sections: manifesto hero excerpt, latest episode (YouTube embed), object grid (2x3, get all objects from collection, sort by priority), latest essay card, "Seen an object we missed?" CTA linking to `/submit`.

- [ ] **Step 2: Write `src/pages/about.astro`**

Uses `EssayLayout`. Content sourced from `theory/manifesto.md`: who we are, the manifesto excerpt, intellectual tradition summary, social links, credits. See spec Section 5.9.

- [ ] **Step 3: Write `src/pages/research.astro`**

Uses `EssayLayout` (680px). Five mechanisms section, dissertation overview (general audience, no ORGANVM jargon), methodology, cross-object density summary, bibliography. Includes `<ObjectDensityGraph client:visible />` React island for the co-occurrence visualization. See spec Section 5.6.

- [ ] **Step 4: Write `src/pages/404.astro`**

Uses `BaseLayout`. "The object you're looking for has withdrawn from view." Navigation links to Home, Episodes, Objects, Essays. See spec Section 5.11.

- [ ] **Step 5: Verify all four pages render**

```bash
npm run dev
# Visit /, /about, /research, /asdf (404)
```

- [ ] **Step 6: Commit**

```bash
git add -A
git commit -m "feat: home, about, research, and 404 pages

Home with manifesto hero, object grid, latest episode/essay.
About with manifesto and team info. Research with five mechanisms.
Custom 404 with editorial tone."
```

---

## Task 7: Collection Pages — Episodes, Essays, Objects (archives + detail)

**Files:**
- Create: `src/pages/episodes/index.astro`, `src/pages/episodes/[slug].astro`
- Create: `src/pages/essays/index.astro`, `src/pages/essays/[slug].astro`
- Create: `src/pages/objects/index.astro`, `src/pages/objects/[slug].astro`

- [ ] **Step 1: Write `src/pages/episodes/index.astro`**

Uses `DataLayout`. Query all episodes from collection, sort by date descending. V1/V2 filter via URL query param (`?version=v1`). Render 2-column grid of `<EpisodeCard />` components. See spec Section 5.2.

- [ ] **Step 2: Write `src/pages/episodes/[slug].astro`**

Uses `BaseLayout` (custom layout — wide for video, narrow for text). Static paths from `getStaticPaths()` returning all episode slugs. YouTubeEmbed, episode metadata, companion essay link, `<FilmographyTable client:visible />` React island with films data passed as prop, symbolic categories, related episodes. JSON-LD VideoObject. See spec Section 5.3.

- [ ] **Step 3: Write `src/pages/essays/index.astro`**

Uses `EssayLayout`. Query all essays, sort by date descending. Filter by type and object via URL params. Render list of `<EssayCard />` components. See spec Section 5.4.

- [ ] **Step 4: Write `src/pages/essays/[slug].astro`**

Uses `EssayLayout`. Static paths from all essay slugs. Render MDX body with prose styling, citations rendered as footnotes, related episode link. JSON-LD Article. See spec Section 5.3.

- [ ] **Step 5: Write `src/pages/objects/index.astro`**

Uses `DataLayout`. Query all objects, sort by status (published first, then by priority_score descending). Render grid of `<ObjectCard />` components with status badges. See spec Section 5.5 (catalog).

- [ ] **Step 6: Write `src/pages/objects/[slug].astro`**

Uses `BaseLayout` (custom — 680px main column, optional data sidebar). Static paths from all object slugs. Object biography (MDX body), symbolic categories (expandable), landmark scenes, co-occurrence links, `<FilmographyTable client:visible />` for full filmography, related episodes/essays, "Know a film with {object}?" CTA. See spec Section 5.5.

- [ ] **Step 7: Verify all collection pages render**

```bash
npm run dev
# Visit /episodes, /episodes/milk, /essays, /essays/milk-in-cinema, /objects, /objects/milk
```

- [ ] **Step 8: Commit**

```bash
git add -A
git commit -m "feat: episode, essay, and object archive + detail pages

Archive pages with filtering. Detail pages with YouTube embeds,
filmography tables, symbolic categories, cross-references."
```

---

## Task 8: React Islands — FilmographyTable + PipelineTimeline + ObjectDensityGraph

**Files:**
- Create: `src/components/react/FilmographyTable.tsx`
- Create: `src/components/react/PipelineTimeline.tsx`
- Create: `src/components/react/ObjectDensityGraph.tsx`
- Create: `src/pages/pipeline.astro`

- [ ] **Step 1: Write `src/components/react/FilmographyTable.tsx`**

Props: `films: Film[]`, `objectFilter?: string`. Uses `@tanstack/react-table` with columns: Title (linked to Letterboxd/IMDB), Year, Director, Object(s), Symbolic Category, Tier. Sortable by all columns. Filterable by symbolic category dropdown. Keyboard-navigable, proper `<th>` scope, sort indicators with `aria-sort`. Renders inside a scrollable container for mobile.

- [ ] **Step 2: Write `src/components/react/PipelineTimeline.tsx`**

Props: `objects: PipelineObject[]`. Horizontal timeline grouped by month from `target_release`. Each object rendered as a card on the timeline with color-coded status: green (published), amber (narration-complete), blue (research). Responsive — stacks vertically on mobile. Uses CSS only (no charting library).

- [ ] **Step 3: Write `src/components/react/ObjectDensityGraph.tsx`**

Props: `films: Film[]`, `objects: string[]`. Renders a co-occurrence matrix: objects on both axes, cells showing count of films where both objects co-occur. Color intensity maps to count. Clickable cells show the film list. Pure CSS grid — no charting library. Accessible: data available as table with screen reader text.

- [ ] **Step 4: Write `src/pages/pipeline.astro`**

Uses `DataLayout`. Loads pipeline status via `getPipelineStatus()`. Renders `<PipelineTimeline client:visible objects={status.objects} />`. Below: object queue table, shorts pipeline status, research queue. See spec Section 5.7.

- [ ] **Step 5: Verify all islands render**

```bash
npm run dev
# Visit /pipeline — timeline should render
# Visit /episodes/milk — filmography table should render
# Visit /research — density graph should render
```

- [ ] **Step 6: Commit**

```bash
git add -A
git commit -m "feat: React islands — filmography table, pipeline timeline, density graph

FilmographyTable with @tanstack/react-table sorting/filtering.
PipelineTimeline with monthly grouping. ObjectDensityGraph
co-occurrence matrix. Pipeline page."
```

---

## Task 9: Submission System — Form + API + D1

**Files:**
- Create: `src/components/react/SubmissionForm.tsx`
- Create: `src/lib/d1.ts`
- Create: `src/pages/submit.astro`
- Create: `src/pages/api/submit.ts`

- [ ] **Step 1: Write `src/lib/d1.ts`**

D1 helper functions. Each function takes the D1 binding as first arg (from `Astro.locals.runtime.env.DB`).

```typescript
// src/lib/d1.ts
export interface Submission {
  id: string;
  type: 'object' | 'film' | 'clip';
  status: 'pending' | 'approved' | 'rejected';
  data: string; // JSON
  submitter_name: string | null;
  submitter_email: string | null;
  created_at: string;
  reviewed_at: string | null;
  reviewed_by: string | null;
}

export async function createSubmission(db: D1Database, submission: Omit<Submission, 'status' | 'reviewed_at' | 'reviewed_by'>): Promise<void> {
  await db.prepare(
    'INSERT INTO submissions (id, type, status, data, submitter_name, submitter_email, created_at) VALUES (?, ?, ?, ?, ?, ?, ?)'
  ).bind(
    submission.id, submission.type, 'pending', submission.data,
    submission.submitter_name, submission.submitter_email, submission.created_at
  ).run();
}

export async function getSubmissions(db: D1Database, status?: string): Promise<Submission[]> {
  const query = status
    ? db.prepare('SELECT * FROM submissions WHERE status = ? ORDER BY created_at DESC').bind(status)
    : db.prepare('SELECT * FROM submissions ORDER BY created_at DESC');
  const result = await query.all<Submission>();
  return result.results;
}

export async function updateSubmission(db: D1Database, id: string, status: 'approved' | 'rejected', reviewedBy: string): Promise<void> {
  await db.prepare(
    'UPDATE submissions SET status = ?, reviewed_at = ?, reviewed_by = ? WHERE id = ?'
  ).bind(status, new Date().toISOString(), reviewedBy, id).run();
}
```

- [ ] **Step 2: Write `src/pages/api/submit.ts`**

```typescript
// src/pages/api/submit.ts
import type { APIRoute } from 'astro';
import { createSubmission } from '@lib/d1';

export const prerender = false;

export const POST: APIRoute = async ({ request, locals }) => {
  const db = locals.runtime.env.DB as D1Database;
  const body = await request.json();

  // Validate type
  if (!['object', 'film', 'clip'].includes(body.type)) {
    return new Response(JSON.stringify({ error: 'Invalid submission type' }), { status: 400 });
  }

  const id = crypto.randomUUID();
  await createSubmission(db, {
    id,
    type: body.type,
    data: JSON.stringify(body.data),
    submitter_name: body.submitter_name || null,
    submitter_email: body.submitter_email || null,
    created_at: new Date().toISOString(),
  });

  return new Response(JSON.stringify({ id, status: 'pending' }), { status: 201 });
};
```

- [ ] **Step 3: Write `src/components/react/SubmissionForm.tsx`**

Three-tab form matching spec Section 5.8. Tab 1: Suggest an Object (name, why, 3+ film examples as repeatable group, name/email). Tab 2: Flag a Film (title, year, director, object dropdown, scene description, timestamp, name). Tab 3: Submit a Clip (title, object, URL, timestamp, context, name). Client-side validation with Zod. POST to `/api/submit`. Success/error states. All form fields have `<label>` associations and `aria-describedby` for validation errors.

- [ ] **Step 4: Write `src/pages/submit.astro`**

Uses `BaseLayout`. Brief intro text explaining the three submission types. Renders `<SubmissionForm client:load />`. See spec Section 5.8.

- [ ] **Step 5: Test submission flow locally**

```bash
npm run dev
# Visit /submit, fill out form, submit
# Check D1 local storage via wrangler d1 execute
wrangler d1 execute object-lessons-submissions --local --command "SELECT * FROM submissions"
```

- [ ] **Step 6: Commit**

```bash
git add -A
git commit -m "feat: submission system — form, API endpoint, D1 integration

Three-tab SubmissionForm React island with client-side validation.
POST /api/submit writes to Cloudflare D1. D1 helper functions."
```

---

## Task 10: Collaborator Dashboard — Auth + API + Dashboard

**Files:**
- Create: `src/lib/auth.ts`
- Create: `src/pages/api/collaborator/auth.ts`
- Create: `src/pages/api/submissions.ts`
- Create: `src/pages/api/submissions/[id].ts`
- Create: `src/components/react/CollaboratorDashboard.tsx`
- Create: `src/pages/collaborator.astro`

- [ ] **Step 1: Write `src/lib/auth.ts`**

Simple shared-secret auth. Password stored as `COLLABORATOR_PASSWORD` environment variable in Cloudflare. Session is an HTTP-only cookie containing an HMAC of the password + a timestamp. `validatePassword()` checks against env var. `createSession()` returns a signed cookie. `checkSession()` validates the cookie HMAC.

```typescript
// src/lib/auth.ts
const COOKIE_NAME = 'ol_collab_session';
const SESSION_DURATION_MS = 7 * 24 * 60 * 60 * 1000; // 7 days

export function validatePassword(input: string, expected: string): boolean {
  // Constant-time comparison
  if (input.length !== expected.length) return false;
  let result = 0;
  for (let i = 0; i < input.length; i++) {
    result |= input.charCodeAt(i) ^ expected.charCodeAt(i);
  }
  return result === 0;
}

export async function createSessionCookie(password: string): Promise<string> { # allow-secret
  const expiry = Date.now() + SESSION_DURATION_MS;
  const payload = `${expiry}`;
  const encoder = new TextEncoder();
  const key = await crypto.subtle.importKey <!-- allow-secret -->('raw', encoder.encode(password), { name: 'HMAC', hash: 'SHA-256' }, false, ['sign']);
  const sig = await crypto.subtle.sign('HMAC', key, encoder.encode(payload));
  const sigHex = Array.from(new Uint8Array(sig)).map(b => b.toString(16).padStart(2, '0')).join('');
  return `${COOKIE_NAME}=${payload}.${sigHex}; HttpOnly; Secure; SameSite=Strict; Path=/; Max-Age=${SESSION_DURATION_MS / 1000}`;
}

export async function checkSession(cookieHeader: string | null, password: string) <!-- allow-secret -->: Promise<boolean> {
  if (!cookieHeader) return false;
  const match = cookieHeader.match(new RegExp(`${COOKIE_NAME}=([^;]+)`));
  if (!match) return false;
  const [payload, sigHex] = match[1].split('.');
  if (!payload || !sigHex) return false;
  const expiry = parseInt(payload, 10);
  if (Date.now() > expiry) return false;
  const encoder = new TextEncoder();
  const key = await crypto.subtle.importKey <!-- allow-secret -->('raw', encoder.encode(password), { name: 'HMAC', hash: 'SHA-256' }, false, ['verify']);
  const sig = new Uint8Array(sigHex.match(/.{2}/g)!.map(b => parseInt(b, 16)));
  return crypto.subtle.verify('HMAC', key, sig, encoder.encode(payload));
}
```

- [ ] **Step 2: Write `src/pages/api/collaborator/auth.ts`**

POST endpoint. Reads password from request body, validates against `COLLABORATOR_PASSWORD` env var. On success, returns `Set-Cookie` header with session cookie. On failure, returns 401.

- [ ] **Step 3: Write `src/pages/api/submissions.ts`**

GET endpoint. Checks session cookie via `checkSession()`. If valid, returns submissions from D1 (optional `?status=pending` filter). If invalid, returns 401.

- [ ] **Step 4: Write `src/pages/api/submissions/[id].ts`**

PATCH endpoint. Checks session cookie. Reads `{ status: 'approved' | 'rejected' }` from body. Calls `updateSubmission()`. Returns updated submission.

- [ ] **Step 5: Write `src/components/react/CollaboratorDashboard.tsx`**

Two states: (a) login form (password input + submit), (b) dashboard (shown after successful auth).

Dashboard sections:
1. **Production status:** Reads pipeline-status.yaml data (passed as prop from Astro page). Color-coded status rows per object.
2. **Content calendar:** Monthly grouping of target_release dates.
3. **Pending submissions:** Fetched from `GET /api/submissions?status=pending`. Table with type, summary, date, submitter. Approve/reject buttons calling `PATCH /api/submissions/[id]`.
4. **Narration queue:** Objects where `narration === 'needs-recording'`.

Login flow: POST to `/api/collaborator/auth`, on success the cookie is set by the response, re-fetch submissions.

- [ ] **Step 6: Write `src/pages/collaborator.astro`**

Uses `DataLayout`. Loads pipeline status server-side. Renders `<CollaboratorDashboard client:load pipelineData={status} />`.

Marked `export const prerender = false;` for SSR (API cookies need to be checked server-side for the page itself, though the dashboard is client-rendered).

- [ ] **Step 7: Test collaborator flow**

```bash
# Set env var for local dev
echo "COLLABORATOR_PASSWORD=test123" >> .dev.vars

npm run dev
# Visit /collaborator, enter password, verify dashboard loads
# Submit something via /submit, verify it appears in dashboard
# Approve it, verify status changes
```

- [ ] **Step 8: Commit**

```bash
git add -A
git commit -m "feat: collaborator dashboard with auth, submission review

HMAC-based session auth. GET/PATCH API endpoints for submissions.
CollaboratorDashboard React island with login, production status,
content calendar, submission review with approve/reject."
```

---

## Task 11: RSS, OG Images, Validation Script

**Files:**
- Create: `src/pages/rss.xml.ts`
- Create: `scripts/generate-og-images.ts`
- Create: `scripts/validate-categories.ts`

- [ ] **Step 1: Write `src/pages/rss.xml.ts`**

```typescript
// src/pages/rss.xml.ts
import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';
import { siteConfig } from '../../site.config';

export async function GET(context: { site: string }) {
  const essays = await getCollection('essays');
  const sorted = essays.sort((a, b) => b.data.date.getTime() - a.data.date.getTime());

  return rss({
    title: siteConfig.name,
    description: siteConfig.description,
    site: context.site,
    items: sorted.map(essay => ({
      title: essay.data.title,
      pubDate: essay.data.date,
      description: essay.data.excerpt,
      link: `/essays/${essay.slug}/`,
    })),
  });
}
```

- [ ] **Step 2: Write `scripts/generate-og-images.ts`**

Node script that reads all episodes, essays, and objects from the content directory, generates an OG image for each using Satori (renders JSX → SVG) + `@resvg/resvg-js` (SVG → PNG). Output to `public/images/og/{type}-{slug}.png`. Image design: warm white background, serif title, object name, "Object Lessons" branding. 1200x630px.

Add to `package.json` scripts: `"og": "tsx scripts/generate-og-images.ts"`.

- [ ] **Step 3: Write `scripts/validate-categories.ts`**

Node script that reads all episode and object content files, checks that every `symbolic_categories` string in an episode matches a `kebab` field in the parent object's `symbolic_categories` array. Exits with error code 1 if any mismatch found. Reports all mismatches.

Add to `package.json` scripts: `"validate": "tsx scripts/validate-categories.ts"`.

- [ ] **Step 4: Run validation**

```bash
npm run validate
# Should pass with no errors
```

- [ ] **Step 5: Generate OG images**

```bash
npm run og
# Should generate PNG files in public/images/og/
ls public/images/og/
```

- [ ] **Step 6: Commit**

```bash
git add -A
git commit -m "feat: RSS feed, OG image generation, category validation

RSS feed for essays. Satori + resvg OG images pre-rendered at build.
Build-time validation: episode categories match object definitions."
```

---

## Task 12: Data Migration — Full Film Database + Content Polish

**Files:**
- Modify: `src/data/films.yaml` (expand from starter to full 302+ films)
- Modify: All content files (polish, cross-references, real YouTube IDs)

- [ ] **Step 1: Build full film database**

Extract film data from all 6 research briefs. Each brief contains structured filmography sections with film titles, years, directors, scene descriptions, and symbolic categories. Parse these into the `films.yaml` format. Also incorporate the density report's cross-object data.

Source files:
- `research--milk-in-cinema.md` (71 films)
- `research--mirrors-in-cinema.md` (85 films)
- `research--cigarettes-in-cinema.md` (74 films)
- `research--clocks-in-cinema.md` (69 films)
- `research--doors-in-cinema.md` (70 films)
- `research--guns-in-cinema.md` (76+ films)

Deduplicate films that appear across multiple objects (e.g., A Clockwork Orange appears in milk, cigarette, clock, and mirror research). Each film entry consolidates all its object appearances.

- [ ] **Step 2: Update episode files with real YouTube IDs**

Look up the 4 V1 episodes on YouTube (@AmpLabMedia) and fill in real `youtube_id` values. V2 episodes keep placeholder IDs (not yet published).

- [ ] **Step 3: Cross-reference polish**

Verify all `films` arrays in episode frontmatter reference valid IDs in `films.yaml`. Verify all `co_occurrences` in object files reference valid object slugs. Verify all `companion_essay` and `related_episodes` references are valid.

- [ ] **Step 4: Run validation**

```bash
npm run validate
npm run build
```

- [ ] **Step 5: Commit**

```bash
git add -A
git commit -m "feat: full film database (302+ films) and content polish

Complete films.yaml extracted from 6 research briefs, deduplicated.
Real YouTube IDs for V1 episodes. Cross-reference validation passes."
```

---

## Task 13: Build Verification + Deploy Prep

**Files:**
- Modify: `package.json` (add scripts)

- [ ] **Step 1: Add build and deploy scripts to `package.json`**

```json
{
  "scripts": {
    "dev": "astro dev",
    "build": "npm run validate && npm run og && astro build",
    "preview": "astro preview",
    "validate": "tsx scripts/validate-categories.ts",
    "og": "tsx scripts/generate-og-images.ts",
    "check": "astro check"
  }
}
```

- [ ] **Step 2: Full build test**

```bash
npm run build
# Should: validate categories, generate OG images, build Astro site
# Check dist/ for output
```

- [ ] **Step 3: Local preview**

```bash
npm run preview
# Visit localhost:4321 — full site should render with all content
# Test: /, /episodes, /episodes/milk, /essays, /essays/milk-in-cinema
# Test: /objects, /objects/milk, /research, /pipeline, /submit, /about
# Test: /collaborator (enter password from .dev.vars)
# Test: /nonexistent (404 page)
# Test: /rss.xml (RSS feed)
```

- [ ] **Step 4: Lighthouse audit**

Run Lighthouse on the home page and one essay page. Target: Performance > 95, Accessibility > 95. Fix any issues found.

- [ ] **Step 5: Commit**

```bash
git add -A
git commit -m "feat: build pipeline, verified full site build

Build: validate → generate OG images → astro build.
Full site renders locally with all 12 routes + 404 + RSS."
```

---

## Task 14: Cloudflare Deployment

**Files:**
- Modify: `wrangler.toml` (fill D1 database ID)

- [ ] **Step 1: Create D1 database**

```bash
npx wrangler d1 create object-lessons-submissions
# Copy the database_id from output into wrangler.toml
```

- [ ] **Step 2: Seed D1 schema**

```bash
npx wrangler d1 execute object-lessons-submissions --file scripts/seed-d1.sql
```

- [ ] **Step 3: Set environment variables**

```bash
npx wrangler pages secret put COLLABORATOR_PASSWORD
# Enter the collaborator password when prompted
```

- [ ] **Step 4: Deploy to Cloudflare Pages**

```bash
npx wrangler pages deploy dist/
# Note the deployment URL
```

- [ ] **Step 5: Verify production deployment**

Visit the Cloudflare Pages URL. Test all routes. Test submission form (writes to production D1). Test collaborator dashboard.

- [ ] **Step 6: Commit final config**

```bash
git add wrangler.toml
git commit -m "chore: Cloudflare D1 database ID configured for production"
```

---

## Task Summary

| Task | Description | Depends On |
|------|-------------|------------|
| 1 | Project scaffold + configuration | — |
| 2 | Content collections + data loaders | 1 |
| 3 | Layouts + core Astro components | 1 |
| 4 | Seed content — object files | 2 |
| 5 | Seed content — episode + essay files | 2, 4 |
| 6 | Static pages — Home, About, Research, 404 | 3, 4, 5 |
| 7 | Collection pages — archives + detail | 3, 4, 5 |
| 8 | React islands — FilmographyTable, PipelineTimeline, ObjectDensityGraph | 2, 3 |
| 9 | Submission system — form + API + D1 | 1, 3 |
| 10 | Collaborator dashboard — auth + API + dashboard | 9 |
| 11 | RSS, OG images, validation script | 5 |
| 12 | Data migration — full film database | 4, 5 |
| 13 | Build verification + deploy prep | all above |
| 14 | Cloudflare deployment | 13 |

**Parallelizable:** Tasks 2+3 can run in parallel. Tasks 4+5 depend on 2. Tasks 6+7+8+9 can run in parallel once 3+4+5 are done. Task 10 depends on 9. Tasks 11+12 can run in parallel once 5 is done.
