# Vigiles Aeternae — Alpha↔Omega Roadmap

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the Vigiles Aeternae — Agon Cosmogonicum system from Genesis through full franchise activation across all eight ORGANVM organs.

**Architecture:** Hub-and-franchise model. META repo (`vigiles-aeternae--agon-cosmogonicum`) is the engine. ORGAN-I repo is the research corpus. ORGAN-II repo is the creative multiverse. Organs III-VII receive franchise expressions as they mature. Each phase produces working, testable, independently valuable output.

**Tech Stack:** Python (engine, CLI), YAML (regime definitions, order specs), JSON Schema (validation), Markdown (research corpus, worldbuilding), Three.js (future visualizations), Next.js (future products)

**Spec:** `praxis-perpetua/specifications/2026-03-20-vigiles-aeternae--agon-cosmogonicum-design.md`

---

## Sub-Project Decomposition

The Vigiles is too large for a single plan. It decomposes into 6 sub-projects, each producing working software independently:

| Sub-Project | Phase | Organs | Independently Valuable? |
|-------------|-------|--------|------------------------|
| **SP-0: Genesis** | 0 | META, I, II | Yes — repos exist, registered, seeded |
| **SP-1: Corpus Mythicum** | 1 | I | Yes — publishable research library |
| **SP-2: Watcher Orders** | 2 | META, I | Yes — governance audit layer for ORGANVM |
| **SP-3: Theatrum Mundi** | 3 | II | Yes — playable worldbuilding bible |
| **SP-4: Agon Engine** | 4 | META | Yes — running governance simulation |
| **SP-5: Franchise Activation** | 5 | III-VII | Yes — products, essays, community, broadcast |

**This document covers SP-0 (Genesis) in full task detail.** SP-1 through SP-5 are defined at the milestone/issue level for the Alpha→Omega roadmap.

---

## SP-0: GENESIS — Repo Creation, Registration, and Founding Documents

### Task 1: Create META hub repo — `vigiles-aeternae--agon-cosmogonicum`

**Files:**
- Create: `vigiles-aeternae--agon-cosmogonicum/README.md`
- Create: `vigiles-aeternae--agon-cosmogonicum/seed.yaml`
- Create: `vigiles-aeternae--agon-cosmogonicum/VIGILES.md`
- Create: `vigiles-aeternae--agon-cosmogonicum/.gitignore`
- Create: `vigiles-aeternae--agon-cosmogonicum/LICENSE`

- [ ] **Step 1: Create the GitHub repo**

```bash
gh repo create meta-organvm/vigiles-aeternae--agon-cosmogonicum \
  --public \
  --description "The Cosmogonic Contest — mythological governance simulation engine for ORGANVM" \
  --clone
```

- [ ] **Step 2: Create seed.yaml**

```yaml
organ: META
name: vigiles-aeternae--agon-cosmogonicum
tier: standard
status: LOCAL
description: >
  Mythological governance simulation engine. The Colosseum where competing
  cosmological regimes audit the real ORGANVM system, generating constitutional
  law from consensus and divergence data from disagreement.
produces:
  - target: all-organs
    type: constitutional-law
  - target: meta-organvm/praxis-perpetua
    type: governance-standards
  - target: meta-organvm/organvm-engine
    type: audit-lenses
consumes:
  - source: organvm-i-theoria/vigiles-aeternae--corpus-mythicum
    type: regime-specifications
  - source: organvm-ii-poiesis/vigiles-aeternae--theatrum-mundi
    type: narrative-scenarios
  - source: meta-organvm/organvm-corpvs-testamentvm
    type: registry-state
  - source: meta-organvm/organvm-ontologia
    type: entity-identity
subscriptions:
  - event: regime.cycle.complete
  - event: constitutional.candidate.proposed
  - event: regime.phaethon.triggered
```

- [ ] **Step 3: Create VIGILES.md (The Manifesto)**

The founding document of the Vigiles system. Contains: cosmological premise, the seven founding orders (summary), the Colosseum loop, and the franchise model. Adapted from design spec sections 2, 4, 5.2, and 3.

- [ ] **Step 4: Create README.md**

Standard ORGANVM README with: what this is, how it fits, current status, getting started, related repos.

- [ ] **Step 5: Create .gitignore and LICENSE**

```bash
# .gitignore — Python project
__pycache__/
*.pyc
.venv/
*.egg-info/
dist/
build/
.pytest_cache/
.ruff_cache/
```

LICENSE: MIT

- [ ] **Step 6: Initial commit and push**

```bash
cd vigiles-aeternae--agon-cosmogonicum
git add -A
git commit -m "feat: genesis — founding documents for the Cosmogonic Contest"
git push -u origin main
```

---

### Task 2: Create ORGAN-I research repo — `vigiles-aeternae--corpus-mythicum`

**Files:**
- Create: `vigiles-aeternae--corpus-mythicum/README.md`
- Create: `vigiles-aeternae--corpus-mythicum/seed.yaml`
- Create: `vigiles-aeternae--corpus-mythicum/.gitignore`
- Create: `vigiles-aeternae--corpus-mythicum/LICENSE`
- Create: `vigiles-aeternae--corpus-mythicum/corpus/README.md`
- Create: `vigiles-aeternae--corpus-mythicum/regimes/README.md`
- Create: `vigiles-aeternae--corpus-mythicum/taxonomy/README.md`
- Create: `vigiles-aeternae--corpus-mythicum/metalaws/README.md`

- [ ] **Step 1: Determine ORGAN-I GitHub org**

Check which GitHub org hosts ORGAN-I repos:

```bash
cd ~/Workspace/organvm-i-theoria && ls -d */ | head -5
# Check a repo's remote to find the org
cd $(ls -d */ | head -1) && git remote -v | head -1
```

- [ ] **Step 2: Create the GitHub repo in ORGAN-I org**

```bash
gh repo create <org>/vigiles-aeternae--corpus-mythicum \
  --public \
  --description "The Library of All Libraries — mythological research corpus for the Vigiles system" \
  --clone
```

- [ ] **Step 3: Create directory scaffold**

```
corpus/          # Synthesized mythology (one dir per tradition)
  greek-roman/
  tolkien/
  malazan/
  matrix/
  lynch/
  marvel-cosmic/
  ...
regimes/         # Formal regime YAML specifications
taxonomy/        # Cross-mythology power taxonomy schemas
metalaws/        # The metaLAWs codex (universal laws across 9 domains)
sources/         # Raw source references and bibliography
```

- [ ] **Step 4: Create seed.yaml**

```yaml
organ: ORGAN-I
name: vigiles-aeternae--corpus-mythicum
tier: standard
status: LOCAL
description: >
  The research corpus of the Vigiles Aeternae. Synthesized mythology across
  20+ traditions, comparative power taxonomies, formal regime specifications,
  and the metaLAWs codex serving as constitutional substrate.
produces:
  - target: organvm-ii-poiesis/vigiles-aeternae--theatrum-mundi
    type: creative-source-material
  - target: meta-organvm/vigiles-aeternae--agon-cosmogonicum
    type: regime-specifications
  - target: external
    type: publishable-research
consumes:
  - source: meta-organvm/alchemia-ingestvm
    type: ingested-material
  - source: organvm-vi-koinonia/vigiles-aeternae--collegium-mythicum
    type: community-research-insights
```

- [ ] **Step 5: Initial commit and push**

---

### Task 3: Create ORGAN-II creative repo — `vigiles-aeternae--theatrum-mundi`

**Files:**
- Create: `vigiles-aeternae--theatrum-mundi/README.md`
- Create: `vigiles-aeternae--theatrum-mundi/seed.yaml`
- Create: `vigiles-aeternae--theatrum-mundi/.gitignore`
- Create: `vigiles-aeternae--theatrum-mundi/LICENSE`
- Create: `vigiles-aeternae--theatrum-mundi/worldbuilding/README.md`
- Create: `vigiles-aeternae--theatrum-mundi/characters/README.md`
- Create: `vigiles-aeternae--theatrum-mundi/rpg/README.md`
- Create: `vigiles-aeternae--theatrum-mundi/rooms/README.md`
- Create: `vigiles-aeternae--theatrum-mundi/art/README.md`

- [ ] **Step 1: Determine ORGAN-II GitHub org**

- [ ] **Step 2: Create the GitHub repo in ORGAN-II org**

```bash
gh repo create <org>/vigiles-aeternae--theatrum-mundi \
  --public \
  --description "The Theater of the World — creative multiverse, RPG, and worldbuilding bible for the Vigiles system" \
  --clone
```

- [ ] **Step 3: Create directory scaffold**

```
worldbuilding/   # Multiverse skeleton, realm definitions, dimensional structure
characters/      # Character sheets per Watcher Order
  orders/        # The seven founding orders
  regimes/       # Regime-specific characters
rpg/             # RPG system rules, magic system, class definitions
rooms/           # Spatial room system (H.E.R.E., T.H.E.R.E., etc.)
  primary/       # H.E.R.E., T.H.E.R.E., E.V.E.R.Y.W.H.E.R.E., M41N_STR33T
  liminal/       # NOWHERE, SOMEWHERE, BACKTHEN, NEVERW4S
  streets/       # Symbolic street corridors
art/             # Generative art code, visual assets
sound/           # Sonic identities, regime soundscapes
narrative/       # Forking threads, chronicles, fold records
```

- [ ] **Step 4: Create seed.yaml**

```yaml
organ: ORGAN-II
name: vigiles-aeternae--theatrum-mundi
tier: standard
status: LOCAL
description: >
  The creative multiverse of the Vigiles Aeternae. Worldbuilding bible,
  character designs, RPG system, generative art, sound design, and the
  spatial room navigation system (H.E.R.E./T.H.E.R.E./E.V.E.R.Y.W.H.E.R.E.).
produces:
  - target: organvm-iii-ergon/vigiles-aeternae--mercatura-mythica
    type: creative-assets
  - target: organvm-v-logos/vigiles-aeternae--vox-custodes
    type: narrative-content
  - target: meta-organvm/vigiles-aeternae--agon-cosmogonicum
    type: narrative-scenarios
consumes:
  - source: organvm-i-theoria/vigiles-aeternae--corpus-mythicum
    type: research-material
  - source: organvm-ii-poiesis/alchemical-synthesizer
    type: synth-creature-framework
```

- [ ] **Step 5: Initial commit and push**

---

### Task 4: Register all three repos in registry-v2.json

**Files:**
- Modify: `organvm-corpvs-testamentvm/registry-v2.json`

- [ ] **Step 1: Add META repo entry**

```bash
organvm registry update vigiles-aeternae--agon-cosmogonicum \
  --organ META \
  --status LOCAL \
  --tier standard \
  --description "Mythological governance simulation engine — the Colosseum"
```

If CLI doesn't support creation, add manually to the META-ORGANVM section.

- [ ] **Step 2: Add ORGAN-I repo entry**

```bash
organvm registry update vigiles-aeternae--corpus-mythicum \
  --organ ORGAN-I \
  --status LOCAL \
  --tier standard \
  --description "Mythological research corpus — the Library of All Libraries"
```

- [ ] **Step 3: Add ORGAN-II repo entry**

```bash
organvm registry update vigiles-aeternae--theatrum-mundi \
  --organ ORGAN-II \
  --status LOCAL \
  --tier standard \
  --description "Creative multiverse and RPG — the Theater of the World"
```

- [ ] **Step 4: Validate registry**

```bash
organvm registry validate
```

Expected: PASS, no errors.

- [ ] **Step 5: Commit registry changes**

```bash
cd organvm-corpvs-testamentvm
git add registry-v2.json
git commit -m "registry: add three Vigiles Aeternae repos (META, I, II)"
```

---

### Task 5: Create founding Watcher Order documents

**Files:**
- Create: `vigiles-aeternae--agon-cosmogonicum/orders/ORDERS.md`
- Create: `vigiles-aeternae--agon-cosmogonicum/orders/ordo-architectorum.yaml`
- Create: `vigiles-aeternae--agon-cosmogonicum/orders/ordo-sibyllarum.yaml`
- Create: `vigiles-aeternae--agon-cosmogonicum/orders/ordo-seraphorum.yaml`
- Create: `vigiles-aeternae--agon-cosmogonicum/orders/ordo-psychopomporum.yaml`
- Create: `vigiles-aeternae--agon-cosmogonicum/orders/ordo-fabrorum-recursivorum.yaml`
- Create: `vigiles-aeternae--agon-cosmogonicum/orders/ordo-testium-aeternum.yaml`
- Create: `vigiles-aeternae--agon-cosmogonicum/orders/ordo-demiurgorum.yaml`

- [ ] **Step 1: Create ORDERS.md** — the pantheon manifest summarizing all seven orders

- [ ] **Step 2: Create YAML for each order** — structured data: name, latin, domain, power, constraint, failure_mode, rpg_class, system_function, mythological_sources, hierarchy_position

- [ ] **Step 3: Commit**

```bash
git add orders/
git commit -m "feat: seven founding Watcher Orders — the pantheon manifest"
```

---

### Task 6: Create Colosseum rules and regime schema

**Files:**
- Create: `vigiles-aeternae--agon-cosmogonicum/colosseum/COLOSSEUM.md`
- Create: `vigiles-aeternae--agon-cosmogonicum/colosseum/regime-schema.yaml`
- Create: `vigiles-aeternae--agon-cosmogonicum/colosseum/loop.md`

- [ ] **Step 1: Create COLOSSEUM.md** — rules of engagement, the Agon loop, how regimes compete

- [ ] **Step 2: Create regime-schema.yaml** — the formal YAML schema for regime definitions (from spec section 5.1)

- [ ] **Step 3: Create loop.md** — detailed Colosseum loop documentation (SUMMON→AUDIT→REPORT→DIVERGE→CONSENSUS→CHRONICLE→ROTATE)

- [ ] **Step 4: Commit**

```bash
git add colosseum/
git commit -m "feat: Colosseum rules, regime YAML schema, and Agon loop"
```

---

### Task 7: Create first two regime definitions (Tolkien + Malazan)

**Files:**
- Create: `vigiles-aeternae--agon-cosmogonicum/regimes/tolkien--delegated-authority.yaml`
- Create: `vigiles-aeternae--agon-cosmogonicum/regimes/malazan--pressure-ascendancy.yaml`

- [ ] **Step 1: Write Tolkien regime YAML** — full regime definition following the schema (priorities, violations, health_model, phaethon, audit_rules, narrative)

- [ ] **Step 2: Write Malazan regime YAML** — full regime definition, intentionally contrasting Tolkien on every axis

- [ ] **Step 3: Validate both against regime-schema.yaml**

- [ ] **Step 4: Commit**

```bash
git add regimes/
git commit -m "feat: founding regimes — Tolkien (delegated authority) and Malazan (pressure ascendancy)"
```

---

### Task 8: Ingest topological-mythos through alchemia

**Files:**
- Modify: routing through alchemia intake pipeline

- [ ] **Step 1: Create alchemia manifest for topological-mythos**

Map the 29 ChatGPT exports to corpus destinations:
- Matrix files → `corpus/matrix/`
- Tolkien files → `corpus/tolkien/`
- Malazan files → `corpus/malazan/`
- etc.

- [ ] **Step 2: Run alchemia intake**

```bash
alchemia intake --source-dir ~/Workspace/meta-organvm/topological-mythos/ \
  --output ~/Workspace/organvm-i-theoria/vigiles-aeternae--corpus-mythicum/corpus/
```

- [ ] **Step 3: Ingest metaLAWs and HERE/THERE/EVERYWHERE**

Copy and structure:
- `intake/OS-me/metaLAWs.md` → `metalaws/codex-v1.md`
- `intake/here-there-everywhere-nowhere.md` → fed to theatrum-mundi `rooms/`

- [ ] **Step 4: Commit ingested material**

---

### Task 9: Generate context files and sync submodules

- [ ] **Step 1: Generate CLAUDE.md for all three repos**

```bash
organvm context sync --organ META
organvm context sync --organ ORGAN-I
organvm context sync --organ ORGAN-II
```

- [ ] **Step 2: Add as submodules (if META superproject)**

```bash
cd ~/Workspace/meta-organvm
organvm git add-submodule --organ META --repo vigiles-aeternae--agon-cosmogonicum
```

- [ ] **Step 3: Sync superproject pointers**

```bash
organvm git sync-organ --organ META --message "chore: add vigiles-aeternae--agon-cosmogonicum submodule"
```

- [ ] **Step 4: Bootstrap ontologia entities**

```bash
organvm ontologia bootstrap
```

Register all three new repos as entities with UIDs.

---

### Task 10: Create GitHub issues for full roadmap

See Section: Alpha→Omega Issue Map below.

---

## Alpha→Omega Issue Map

All issues tracked in `meta-organvm/organvm-corpvs-testamentvm` (the central issue tracker) unless otherwise noted.

### Milestone: ALPHA — Genesis (SP-0)

| # | Title | Labels | Blocked By |
|---|-------|--------|------------|
| A1 | Create `vigiles-aeternae--agon-cosmogonicum` repo (META) | `vigiles`, `genesis`, `organ:meta` | — |
| A2 | Create `vigiles-aeternae--corpus-mythicum` repo (ORGAN-I) | `vigiles`, `genesis`, `organ:I` | — |
| A3 | Create `vigiles-aeternae--theatrum-mundi` repo (ORGAN-II) | `vigiles`, `genesis`, `organ:II` | — |
| A4 | Register all three repos in registry-v2.json | `vigiles`, `genesis`, `registry` | A1, A2, A3 |
| A5 | Write VIGILES.md manifesto | `vigiles`, `genesis`, `docs` | A1 |
| A6 | Write founding Watcher Orders (7 YAML + ORDERS.md) | `vigiles`, `genesis`, `orders` | A1 |
| A7 | Write Colosseum rules + regime YAML schema | `vigiles`, `genesis`, `colosseum` | A1 |
| A8 | Write Tolkien regime definition | `vigiles`, `genesis`, `regime` | A7 |
| A9 | Write Malazan regime definition | `vigiles`, `genesis`, `regime` | A7 |
| A10 | Ingest topological-mythos through alchemia | `vigiles`, `genesis`, `ingest` | A2 |
| A11 | Ingest metaLAWs codex into corpus | `vigiles`, `genesis`, `ingest` | A2 |
| A12 | Ingest HERE/THERE/EVERYWHERE into theatrum | `vigiles`, `genesis`, `ingest` | A3 |
| A13 | Generate context files for all three repos | `vigiles`, `genesis`, `context` | A4 |
| A14 | Bootstrap ontologia entities for Vigiles repos | `vigiles`, `genesis`, `ontologia` | A4 |
| A15 | Add META repo as superproject submodule | `vigiles`, `genesis`, `git` | A1 |

### Milestone: BETA — Corpus Mythicum (SP-1)

| # | Title | Labels | Blocked By |
|---|-------|--------|------------|
| B1 | Synthesize Greek/Roman mythology (Titans, Olympians, succession wars, Furies, mystery cults) | `vigiles`, `corpus`, `research`, `organ:I` | A10 |
| B2 | Synthesize Marvel cosmic hierarchy (Celestials, Living Tribunal, Beyonders, Watchers, Galactus, Phoenix) | `vigiles`, `corpus`, `research`, `organ:I` | A10 |
| B3 | Synthesize Hindu/Buddhist cosmology (Trimurti, yugas, dharma/karma, bodhisattva path) | `vigiles`, `corpus`, `research`, `organ:I` | A10 |
| B4 | Synthesize Norse mythology (Ragnarok, Norns, Yggdrasil, known-failure governance) | `vigiles`, `corpus`, `research`, `organ:I` | A10 |
| B5 | Synthesize Egyptian mythology (Ma'at, ritual governance, Duat) | `vigiles`, `corpus`, `research`, `organ:I` | A10 |
| B6 | Synthesize Mesoamerican mythology (sacrifice-as-fuel, Popol Vuh, blood economy) | `vigiles`, `corpus`, `research`, `organ:I` | A10 |
| B7 | Synthesize African mythologies (Yoruba Orishas, Anansi, ancestral governance) | `vigiles`, `corpus`, `research`, `organ:I` | A10 |
| B8 | Synthesize Abrahamic cosmology (angelic hierarchies, Kabbalistic sefirot, Islamic cosmology) | `vigiles`, `corpus`, `research`, `organ:I` | A10 |
| B9 | Synthesize Daoist cosmology (wu wei governance, Daodejing, balance philosophy) | `vigiles`, `corpus`, `research`, `organ:I` | A10 |
| B10 | Synthesize Indigenous Australian Dreamtime (concurrent reality, songlines as law) | `vigiles`, `corpus`, `research`, `organ:I` | A10 |
| B11 | Synthesize additional fictional mythologies (Dune, Foundation, Discworld) | `vigiles`, `corpus`, `research`, `organ:I` | A10 |
| B12 | Structure existing 29 ChatGPT exports into formal corpus entries | `vigiles`, `corpus`, `ingest`, `organ:I` | A10 |
| B13 | Build cross-mythology comparative analysis (universal structures, unique structures) | `vigiles`, `corpus`, `analysis`, `organ:I` | B1-B12 |
| B14 | Formalize power taxonomy schema (authority, enforcement, rebellion, decay per tradition) | `vigiles`, `corpus`, `schema`, `organ:I` | B13 |
| B15 | Structure metaLAWs codex with cross-references to mythology corpus | `vigiles`, `corpus`, `metalaws`, `organ:I` | A11, B13 |
| B16 | Draft regime specs for all 9 founding cosmologies | `vigiles`, `corpus`, `regimes`, `organ:I` | B13 |
| B17 | Draft regimes for newly researched traditions (Greek, Marvel, Hindu, Norse, Egyptian, etc.) | `vigiles`, `corpus`, `regimes`, `organ:I` | B1-B11, B16 |
| B18 | First publishable paper: comparative governance across mythologies | `vigiles`, `corpus`, `publication`, `organ:I` | B13, B14 |

### Milestone: GAMMA — Watcher Orders (SP-2)

| # | Title | Labels | Blocked By |
|---|-------|--------|------------|
| G1 | Expand Order YAML schema with RPG stats, visual identity, sonic identity | `vigiles`, `orders`, `schema` | A6 |
| G2 | Character sheets: Ordo Architectorum (visual, sonic, personality, powers, constraints) | `vigiles`, `orders`, `characters` | G1 |
| G3 | Character sheets: Ordo Sibyllarum | `vigiles`, `orders`, `characters` | G1 |
| G4 | Character sheets: Ordo Seraphorum | `vigiles`, `orders`, `characters` | G1 |
| G5 | Character sheets: Ordo Psychopomporum | `vigiles`, `orders`, `characters` | G1 |
| G6 | Character sheets: Ordo Fabrorum Recursivorum (Smiths) | `vigiles`, `orders`, `characters` | G1 |
| G7 | Character sheets: Ordo Testium Aeternum (Witnesses) | `vigiles`, `orders`, `characters` | G1 |
| G8 | Character sheets: Ordo Demiurgorum (Cosmogonists) | `vigiles`, `orders`, `characters` | G1 |
| G9 | Map each Order to concrete ORGANVM CLI commands and SOPs | `vigiles`, `orders`, `integration` | G2-G8 |
| G10 | Wire Orders into organvm-engine as a recognizable governance layer | `vigiles`, `orders`, `engine`, `code` | G9 |
| G11 | Add Order audit commands to organvm CLI | `vigiles`, `orders`, `cli`, `code` | G10 |
| G12 | Constitutional bedrock v1: extract immutable laws from initial regime consensus | `vigiles`, `orders`, `constitution` | A8, A9, G9 |
| G13 | Write CONSTITUTION--immutable-structural-laws.md in praxis-perpetua/standards/ | `vigiles`, `orders`, `constitution`, `docs` | G12 |
| G14 | Research: identify potential new Orders from deep mythology study | `vigiles`, `orders`, `research` | B1-B11 |

### Milestone: DELTA — Theatrum Mundi (SP-3)

| # | Title | Labels | Blocked By |
|---|-------|--------|------------|
| D1 | Define multiverse dimensional structure (Colosseum, Regime Realms, Folds) | `vigiles`, `theatrum`, `worldbuilding` | A3 |
| D2 | Design the spatial room system (H.E.R.E., T.H.E.R.E., E.V.E.R.Y.W.H.E.R.E., M41N_STR33T) | `vigiles`, `theatrum`, `rooms` | A12 |
| D3 | Design liminal rooms (NOWHERE, SOMEWHERE, BACKTHEN, NEVERW4S) | `vigiles`, `theatrum`, `rooms` | D2 |
| D4 | Design symbolic street corridors (Ocean Avenue, Mulholland Drive, Elm Street, etc.) | `vigiles`, `theatrum`, `rooms` | D2 |
| D5 | RPG system v1: character creation rules, Order-based classes | `vigiles`, `theatrum`, `rpg` | G2-G8 |
| D6 | Magic system v1: Absorb/Fuse/Evolve/Replicate/Relinquish mechanics | `vigiles`, `theatrum`, `rpg`, `magic` | D5 |
| D7 | Fusion rules: study requirements, instability, forbidden combinations | `vigiles`, `theatrum`, `rpg`, `magic` | D6 |
| D8 | Fork mechanic: data structure, branching rules, divergence calculation | `vigiles`, `theatrum`, `rpg`, `code` | D1 |
| D9 | Bestiary v1: formalize mythological beings as interactive entities | `vigiles`, `theatrum`, `bestiary` | B12 |
| D10 | Sonic identities: regime/order soundscapes (connect to alchemical-synthesizer) | `vigiles`, `theatrum`, `sound`, `organ:II` | G2-G8 |
| D11 | Visual identities: regime/order concept art and aesthetic definitions | `vigiles`, `theatrum`, `art`, `organ:II` | G2-G8 |
| D12 | Worldbuilding bible v1: comprehensive reference document | `vigiles`, `theatrum`, `docs` | D1-D11 |
| D13 | First forking narrative thread: Tolkien vs Malazan governance collision | `vigiles`, `theatrum`, `narrative` | D1, A8, A9 |

### Milestone: EPSILON — Agon Engine (SP-4)

| # | Title | Labels | Blocked By |
|---|-------|--------|------------|
| E1 | Regime YAML loader + validator (Python) | `vigiles`, `agon`, `engine`, `code` | A7 |
| E2 | Colosseum runner v1: apply regime audit_rules to ORGANVM registry state | `vigiles`, `agon`, `engine`, `code` | E1, G10 |
| E3 | Regime report generator (regime voice + aesthetic in output) | `vigiles`, `agon`, `engine`, `code` | E2 |
| E4 | Divergence analyzer: compare audit findings across regimes | `vigiles`, `agon`, `engine`, `code` | E3 |
| E5 | Consensus engine: identify where all regimes agree → Constitutional candidates | `vigiles`, `agon`, `engine`, `code` | E4 |
| E6 | Phaethon detector: flag when a regime's philosophy would burn the world | `vigiles`, `agon`, `engine`, `code` | E4 |
| E7 | Chronicle recorder: append-only JSONL history of each Agon cycle | `vigiles`, `agon`, `engine`, `code` | E2 |
| E8 | CLI: `vigiles colosseum run --regime tolkien` | `vigiles`, `agon`, `cli`, `code` | E2 |
| E9 | CLI: `vigiles colosseum compare --regimes tolkien,malazan` | `vigiles`, `agon`, `cli`, `code` | E4 |
| E10 | CLI: `vigiles colosseum consensus` | `vigiles`, `agon`, `cli`, `code` | E5 |
| E11 | Integration: wire Colosseum into organvm-engine governance module | `vigiles`, `agon`, `integration`, `code` | E2, G10 |
| E12 | MCP tools: expose Colosseum via organvm-mcp-server | `vigiles`, `agon`, `mcp`, `code` | E11 |
| E13 | Dashboard: regime audit visualizations in system-dashboard | `vigiles`, `agon`, `dashboard`, `code` | E3 |
| E14 | Run first full Agon cycle: Tolkien vs Malazan on real ORGANVM state | `vigiles`, `agon`, `milestone` | E9 |

### Milestone: ZETA — Franchise Activation (SP-5)

| # | Title | Labels | Blocked By |
|---|-------|--------|------------|
| Z1 | Create `vigiles-aeternae--mercatura-mythica` repo (ORGAN-III) | `vigiles`, `franchise`, `organ:III` | D12 |
| Z2 | Create `vigiles-aeternae--ordo-taxis` repo (ORGAN-IV) | `vigiles`, `franchise`, `organ:IV` | G10 |
| Z3 | Create `vigiles-aeternae--vox-custodes` repo (ORGAN-V) | `vigiles`, `franchise`, `organ:V` | E14 |
| Z4 | Create `vigiles-aeternae--collegium-mythicum` repo (ORGAN-VI) | `vigiles`, `franchise`, `organ:VI` | D12 |
| Z5 | Create `vigiles-aeternae--kerygma-custodes` repo (ORGAN-VII) | `vigiles`, `franchise`, `organ:VII` | E14 |
| Z6 | "Which Watcher Order Are You?" personality quiz (ORGAN-III product) | `vigiles`, `product`, `organ:III` | D5, G2-G8 |
| Z7 | Watcher Order character art prints (ORGAN-III product) | `vigiles`, `product`, `organ:III` | D11 |
| Z8 | Agent personas: Claude session that embodies regime philosophy (ORGAN-IV) | `vigiles`, `agents`, `organ:IV` | A8, A9, G10 |
| Z9 | First essay: "What Happens When Malazan Governs Your Codebase" (ORGAN-V) | `vigiles`, `essay`, `organ:V` | E14 |
| Z10 | Regime Election: community votes on next governing cosmology (ORGAN-VI) | `vigiles`, `community`, `organ:VI` | E14 |
| Z11 | First broadcast: character reveals + regime audit results (ORGAN-VII) | `vigiles`, `broadcast`, `organ:VII` | E14, D11 |
| Z12 | RPG on itch.io: playable web version (ORGAN-III product) | `vigiles`, `product`, `organ:III` | D5, D6, D12 |
| Z13 | The Book: mythology as publishable creative work (ORGAN-III product) | `vigiles`, `product`, `organ:III` | D12, B18 |

### Milestone: OMEGA — The Agon Continues (Perpetual)

| # | Title | Labels | Blocked By |
|---|-------|--------|------------|
| Ω1 | Research pipeline: ongoing mythology deep dives feed new regimes | `vigiles`, `perpetual`, `research` | B13 |
| Ω2 | Community worldbuilding: collaborative multiverse expansion | `vigiles`, `perpetual`, `community` | Z4 |
| Ω3 | Constitutional accumulation: Agon consensus feeds praxis-perpetua | `vigiles`, `perpetual`, `constitution` | E5 |
| Ω4 | Revenue pipeline: products generate income, fund deeper research | `vigiles`, `perpetual`, `revenue` | Z6, Z7 |
| Ω5 | Autopoietic evolution: the Vigiles watches itself, reshapes Orders | `vigiles`, `perpetual`, `meta` | E14, G14 |
| Ω6 | Hybrid regimes: emergent governance from cosmology collisions | `vigiles`, `perpetual`, `regimes` | E14, B17 |
| Ω7 | New Watcher Orders: research reveals orders the founding seven missed | `vigiles`, `perpetual`, `orders` | G14 |
| Ω8 | Full franchise revenue: all eight organs generating value | `vigiles`, `perpetual`, `revenue` | Z1-Z13 |

---

## Issue Label Taxonomy

Create these labels in the tracking repo:

| Label | Color | Description |
|-------|-------|-------------|
| `vigiles` | `#7B68EE` (medium slate blue) | All Vigiles Aeternae issues |
| `genesis` | `#FFD700` (gold) | Phase 0: Genesis |
| `corpus` | `#4169E1` (royal blue) | SP-1: Corpus Mythicum |
| `orders` | `#DC143C` (crimson) | SP-2: Watcher Orders |
| `theatrum` | `#9370DB` (medium purple) | SP-3: Theatrum Mundi |
| `agon` | `#FF4500` (orange red) | SP-4: Agon Engine |
| `franchise` | `#32CD32` (lime green) | SP-5: Franchise Activation |
| `perpetual` | `#C0C0C0` (silver) | Omega: perpetual/ongoing |
| `research` | `#87CEEB` (sky blue) | Research tasks |
| `regime` | `#B22222` (fire brick) | Regime definition work |
| `constitution` | `#DAA520` (goldenrod) | Constitutional law output |
| `ingest` | `#8B4513` (saddle brown) | Material ingestion |

---

## Execution Notes

- **SP-0 (Genesis)** can be executed in a single focused session (2-3 hours)
- **SP-1 (Corpus)** is research-heavy — best distributed across multiple sessions with deep web research
- **SP-2 and SP-3** can be developed in parallel (Orders are characters in both engine AND world)
- **SP-4 (Engine)** requires SP-2 completion for the governance integration
- **SP-5 (Franchise)** repos should be created only when their content is ready, not speculatively
- **GitHub issues should be created in batch** with proper dependency links

---

*Onw4rds && upw4rds. 4d.infinitum && in.perpetuity.*
*The roadmap from Alpha to Omega — and back again.*
