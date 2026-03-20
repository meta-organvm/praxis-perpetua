# Materia Collider: Automated Film-Scrubbing System

**Working name:** Materia Collider (`materia-collider`)
**Date:** 2026-03-19
**Status:** DRAFT
**ORGANVM placement:** ORGAN-III (Ergon) -- commercial/utility tooling
**Tier:** standard
**Author:** 4JP

---

## 1. System Overview

### Problem

The AMP Lab / Object Lessons YouTube channel compiles clips of recurring objects across 100 years of cinema -- a single episode covers 50-70 films for one object (milk, telephones, cigarettes, etc.). The bottleneck is research: manually scrubbing through films to find where objects appear, logging timestamps, extracting clips, and tracking what has been used. A 2-hour film takes 2-3 hours to scrub manually. At 60 films per episode, that is 120-180 hours of labor before editing even begins.

### Solution

Materia Collider automates the most labor-intensive phase: finding where objects appear in films. It ingests film files, runs object detection on sampled frames, extracts timestamped clips around detections, and maintains a searchable clip database. The operator reviews and curates detections rather than performing exhaustive manual scrubbing.

### Competitive Moat

No existing tool combines cinema-specific object detection with structured clip management and episode assembly support. General-purpose video analysis tools (Google Video AI, Amazon Rekognition) require cloud upload of copyrighted content and lack the domain-specific metadata model (symbolic valence, Content ID tracking, episode assembly). This system is purpose-built for transformative film criticism at scale.

---

## 2. Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                      MATERIA COLLIDER                        │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│   INGEST ──▶ DETECT ──▶ EXTRACT ──▶ TAG ──▶ STORE          │
│                                       │                      │
│                                 ASSEMBLE ◀───────────────── │
│                                       │                      │
│                                    TRACK                     │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│   CLI: materia <command> [options]                           │
│   DB:  SQLite (local) / PostgreSQL (scale)                  │
│   ML:  YOLOv8 → DETR → fine-tuned (phased)                 │
└──────────────────────────────────────────────────────────────┘
```

### Pipeline Stages

#### INGEST

Accept film files and create structured records in the database.

**Inputs:** MP4, MKV, AVI, MOV files (or directories of them).

**Operations:**
- Extract technical metadata via ffprobe: codec, resolution, duration, bitrate, audio tracks.
- Extract or accept editorial metadata: title, year, director, genre, country of origin.
- Compute file hash (SHA-256) for deduplication and provenance.
- Create a `Film` record in the database.
- Generate a poster-frame thumbnail (frame at 10% runtime).
- Batch mode: walk a media library directory, ingest all recognized video files, skip duplicates by hash.

**Metadata sources (priority order):**
1. Embedded metadata (MP4 tags, MKV tags).
2. Filename parsing (conventions like `Title (Year) [Director].mkv`).
3. Manual CLI flags (`--title`, `--year`, `--director`).
4. Future: TMDb API lookup by title+year.

**CLI:**
```
materia ingest <path>                    # single file
materia ingest <directory> --batch       # batch from directory
materia ingest <path> --title "Psycho" --year 1960 --director "Alfred Hitchcock"
materia films list [--year-range 1920-1970] [--director X]
materia films show <film-id>
```

#### DETECT

Run object detection on film frames to locate specific objects.

**Two sampling strategies:**

| Strategy | Frames/Film (2hr) | When to Use |
|----------|-------------------|-------------|
| Uniform sampling | ~7,200 (1 fps) | Thorough search, small objects |
| Scene-change detection | ~500-1,500 | Fast pass, prominent objects |

**Uniform sampling** extracts one frame every N seconds (default: 1 second). Simple, predictable, guarantees coverage. For a 120-minute film at 1 fps, this produces 7,200 frames.

**Scene-change detection** uses ffmpeg's `select='gt(scene,0.3)'` filter to extract frames only at shot boundaries. Reduces frame count by 5-15x while capturing the visual content of each shot. Tunable threshold (0.1 = aggressive, many frames; 0.5 = conservative, fewer frames).

**Detection models (phased):**

| Phase | Model | COCO Classes | Custom Classes | M3 Performance |
|-------|-------|-------------|----------------|----------------|
| V1 | YOLOv8-nano | 80 | 0 | ~400 fps |
| V2 | YOLOv8-small | 80 | 0 | ~200 fps |
| V3 | YOLOv8-small fine-tuned | 80 + N custom | cinema-specific | ~180 fps |
| V4 | DETR (optional) | 91 | transformer context | ~30 fps |

**Detection output:** For each frame where a target object is found, record:
- `timestamp_seconds`: position in the film
- `object_label`: detected class label
- `confidence`: model confidence score (0.0-1.0)
- `bounding_box`: `[x_min, y_min, x_max, y_max]` normalized coordinates
- `frame_path`: path to the extracted frame image (for review UI)
- `model_version`: which model produced this detection

**Confidence filtering:** Default threshold 0.5. Configurable per object -- common objects (cup, bottle) benefit from higher thresholds (0.7+) to reduce noise. Rare objects (typewriter, gramophone) can use lower thresholds (0.3) to avoid misses.

**CLI:**
```
materia detect <film-id> --object milk         # detect specific object
materia detect <film-id> --all                 # detect all known objects
materia detect <film-id> --strategy scene      # scene-change sampling
materia detect <film-id> --threshold 0.6       # custom confidence
materia detect <directory> --batch --object telephone   # batch detection
materia detections list <film-id> [--object X] [--min-confidence 0.5]
```

#### EXTRACT

Given detected object appearances, extract video clips from the source film.

**Clip extraction logic:**
1. For each detection (or cluster of nearby detections), define a temporal window.
2. Apply configurable padding: N seconds before and after the detection timestamp (default: 2s before, 2s after).
3. Snap to scene boundaries when possible: if a scene change occurs within the padding window, extend the clip to that natural cut point rather than cutting mid-shot.
4. Merge overlapping windows: if two detections of the same object are 3 seconds apart with 2-second padding, produce one continuous clip instead of two overlapping ones.

**Export formats:**

| Format | Codec | Use Case | File Size (30s clip) |
|--------|-------|----------|---------------------|
| Preview | H.264, 720p | Quick review, web | ~5-10 MB |
| Edit | ProRes 422, source resolution | NLE timeline import | ~100-300 MB |
| Archive | Source copy (stream copy) | Lossless preservation | Varies |

Stream copy (`ffmpeg -c copy`) is preferred when start/end align to keyframes. Otherwise, re-encode at source quality.

**CLI:**
```
materia extract <film-id> --object milk           # extract all milk clips
materia extract <film-id> --detection-id 42       # extract specific detection
materia extract <film-id> --object milk --format prores   # ProRes export
materia extract <film-id> --padding 3             # 3s before and after
materia clips list [--film-id X] [--object X]
```

#### TAG

Enrich clips with structured metadata beyond what detection provides.

**Automated tags (from detection context):**
- Co-occurring objects: what else was detected in the same frame or temporal window.
- Shot composition: approximated from bounding box position (center frame, foreground, background, edge).
- Temporal position: percentage through the film (opening, midpoint, climax, denouement -- mapped from runtime quartiles).

**Manual annotation fields:**
- `scene_type`: dialogue, action, montage, establishing, close-up, insert, dream-sequence, flashback.
- `symbolic_valence`: free-text field for what the object "means" in this scene. This is the intellectual core of Object Lessons -- the system stores it, the human provides it.
- `usage_status`: unused, selected, used-in-episode-N, rejected, Content-ID-flagged.
- `notes`: free-text notes for the operator.

**CLI:**
```
materia tag <clip-id> --scene-type dialogue --valence "domesticity, maternal control"
materia tag <clip-id> --status used-in-episode-3
materia tags list --object milk [--scene-type X]
```

#### STORE

Searchable clip database with full-text search and structured filtering.

**Primary store:** SQLite via `sqlite3` (stdlib). Single file, zero-config, portable. The entire database for 500 films with 10,000 clips will be under 50 MB (metadata only -- clips are files on disk referenced by path).

**Search capabilities:**
- Full-text search (FTS5) on: film title, director, object label, symbolic valence, notes.
- Structured filters: object, film, director, year range, genre, country, scene type, usage status, confidence range.
- Compound queries: "all milk clips from 1940-1960 by Hitchcock in dialogue scenes, unused."

**Thumbnail generation:** Extract a representative frame from each clip (midpoint) and store as JPEG at 320px width. Enables visual browsing without loading video files.

**Timeline export:**
- EDL (Edit Decision List): universal, works with Premiere, DaVinci Resolve, Avid.
- FCPXML: Final Cut Pro native.
- Premiere XML: direct import to Premiere Pro timeline.

**CLI:**
```
materia search milk                               # simple object search
materia search milk --year-range 1940-1960 --director "Hitchcock"
materia search --scene-type montage --unused       # find unused montage clips
materia export <episode-id> --format edl           # timeline export
materia export <episode-id> --format fcpxml
materia stats                                      # database summary
materia stats --object milk                        # per-object coverage
```

#### ASSEMBLE

Episode compilation support: from a bag of clips to a rough cut.

**Given an object, the assembler:**
1. Retrieves all clips tagged for that object.
2. Filters by usage status (exclude already-used, Content-ID-flagged).
3. Suggests ordering strategies:
   - **Chronological**: by film release year (default for Object Lessons format).
   - **Thematic**: group by symbolic valence or scene type.
   - **Directorial**: group by director, then chronological within each group.
   - **Visual similarity**: cluster by frame content (future -- requires embeddings).
4. Generates a rough cut timeline (EDL) with configurable transitions.
5. Estimates episode duration from total clip length.
6. Identifies coverage gaps: which decades have no clips? Which major directors are missing? Which scene types are underrepresented?

**Gap analysis output example:**
```
Object: milk
Total clips: 47 across 38 films
Coverage by decade:
  1920s: 2 clips (weak)
  1930s: 5 clips
  1940s: 8 clips
  1950s: 6 clips
  1960s: 9 clips
  1970s: 7 clips
  1980s: 4 clips
  1990s: 3 clips (weak)
  2000s: 2 clips (weak)
  2010s: 1 clip  (gap)
Missing directors: Kubrick, Kurosawa, Bergman, Fellini
Estimated duration: 14:30 (target: 12-15 min) -- on track
```

**CLI:**
```
materia assemble milk                             # default chronological
materia assemble milk --order thematic            # thematic grouping
materia assemble milk --gaps                      # show coverage gaps
materia assemble milk --export edl --output milk-rough.edl
materia episodes create "Object Lessons: Milk" --object milk
materia episodes list
materia episodes show <episode-id>
```

#### TRACK

Usage and copyright tracking for published episodes.

**Content ID tracking:**
- Log which clips were used in which published episodes.
- Record Content ID claims per clip: claimant, claim type (audio/visual/both), status, revenue impact.
- Flag high-risk sources: studios known for aggressive Content ID enforcement (e.g., Disney, Warner Bros, Universal). Maintained as a configurable risk list.
- Generate per-episode risk assessment before publish.

**Usage statistics:**
- Films scrubbed vs. total in library.
- Clips extracted vs. clips used (utilization rate).
- Objects covered vs. objects in the target list.
- Episode production velocity (episodes/month, clips/episode).

**CLI:**
```
materia track claim <clip-id> --claimant "Universal" --type visual --status active
materia track claims [--film-id X] [--status active]
materia track risk <episode-id>                   # pre-publish risk report
materia track stats                               # usage statistics
```

---

## 3. Data Model

### Entity-Relationship Diagram

```
┌──────────┐       ┌───────────┐       ┌───────────┐
│   Film   │──1:N──│ Detection │──N:1──│  Object   │
└──────────┘       └───────────┘       └───────────┘
     │                   │                    │
     │              (promotes to)             │
     │                   ▼                    │
     │             ┌──────────┐              │
     └────1:N──────│   Clip   │──────N:1─────┘
                   └──────────┘
                        │
                   N:M (via EpisodeClip)
                        │
                   ┌──────────┐
                   │ Episode  │──N:1──Object
                   └──────────┘
                        │
                   ┌──────────────────┐
                   │ ContentIDClaim   │──N:1──Film
                   └──────────────────┘
```

### Table Definitions

#### Film

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INTEGER | PK, AUTOINCREMENT | Internal identifier |
| title | TEXT | NOT NULL | Film title |
| year | INTEGER | | Release year |
| director | TEXT | | Director name |
| genre | TEXT | | Primary genre |
| country | TEXT | | Country of origin |
| runtime_seconds | INTEGER | | Duration in seconds |
| source_path | TEXT | NOT NULL | Absolute path to source file |
| file_hash | TEXT | UNIQUE, NOT NULL | SHA-256 of source file |
| resolution | TEXT | | e.g., "1920x1080" |
| codec | TEXT | | e.g., "h264", "hevc" |
| thumbnail_path | TEXT | | Path to poster-frame thumbnail |
| tmdb_id | INTEGER | | TMDb ID for future API integration |
| ingested_at | TEXT | NOT NULL | ISO 8601 timestamp |
| notes | TEXT | | Free-text notes |

#### Object

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INTEGER | PK, AUTOINCREMENT | Internal identifier |
| label | TEXT | UNIQUE, NOT NULL | Machine label (COCO class or custom) |
| canonical_name | TEXT | NOT NULL | Human-readable name |
| aliases | TEXT | | JSON array of alternate names |
| category | TEXT | | Grouping: food, communication, weapon, furniture, etc. |
| coco_class_id | INTEGER | | COCO dataset class ID if applicable |
| description | TEXT | | What this object is, for disambiguation |
| priority | INTEGER | DEFAULT 0 | Higher = process first in batch detection |

**Alias examples:**
- `telephone`: ["phone", "rotary phone", "cell phone", "mobile phone", "payphone", "receiver"]
- `milk`: ["glass of milk", "milk bottle", "milk carton", "milk jug", "dairy"]
- `cigarette`: ["smoke", "cig", "cigar", "smoking", "ashtray"]

#### Detection

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INTEGER | PK, AUTOINCREMENT | Internal identifier |
| film_id | INTEGER | FK → Film.id, NOT NULL | Which film |
| object_id | INTEGER | FK → Object.id, NOT NULL | What was detected |
| timestamp_seconds | REAL | NOT NULL | Position in film |
| confidence | REAL | NOT NULL | Model confidence (0.0-1.0) |
| bounding_box | TEXT | | JSON: [x_min, y_min, x_max, y_max] |
| frame_path | TEXT | | Path to extracted frame image |
| frame_index | INTEGER | | Frame number in source video |
| model_version | TEXT | NOT NULL | Model identifier string |
| strategy | TEXT | NOT NULL | "uniform" or "scene_change" |
| reviewed | INTEGER | DEFAULT 0 | 0=unreviewed, 1=confirmed, -1=rejected |
| created_at | TEXT | NOT NULL | ISO 8601 timestamp |

**Index:** `(film_id, object_id, timestamp_seconds)` for fast lookups per film per object.

#### Clip

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INTEGER | PK, AUTOINCREMENT | Internal identifier |
| film_id | INTEGER | FK → Film.id, NOT NULL | Source film |
| object_id | INTEGER | FK → Object.id, NOT NULL | Primary object |
| detection_id | INTEGER | FK → Detection.id | Source detection (NULL for manual clips) |
| start_seconds | REAL | NOT NULL | Clip start in film |
| end_seconds | REAL | NOT NULL | Clip end in film |
| duration_seconds | REAL | GENERATED | end - start |
| clip_path | TEXT | | Path to extracted clip file |
| thumbnail_path | TEXT | | Path to midpoint thumbnail |
| format | TEXT | | "h264", "prores", "copy" |
| scene_type | TEXT | | dialogue, action, montage, etc. |
| symbolic_valence | TEXT | | What the object means here |
| co_objects | TEXT | | JSON array of other detected objects |
| shot_position | TEXT | | foreground, center, background, edge |
| film_position | REAL | | 0.0-1.0 normalized position in film |
| usage_status | TEXT | DEFAULT 'unused' | unused, selected, used, rejected, flagged |
| notes | TEXT | | Free-text notes |
| created_at | TEXT | NOT NULL | ISO 8601 timestamp |

#### Episode

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INTEGER | PK, AUTOINCREMENT | Internal identifier |
| title | TEXT | NOT NULL | Episode title |
| object_id | INTEGER | FK → Object.id | Primary object for this episode |
| status | TEXT | DEFAULT 'draft' | draft, assembling, editing, published |
| published_date | TEXT | | ISO 8601 date |
| youtube_url | TEXT | | Published URL |
| duration_seconds | INTEGER | | Final episode duration |
| clip_count | INTEGER | | Number of clips used |
| film_count | INTEGER | | Number of distinct films |
| notes | TEXT | | Production notes |
| created_at | TEXT | NOT NULL | ISO 8601 timestamp |

#### EpisodeClip

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| episode_id | INTEGER | FK → Episode.id, NOT NULL | |
| clip_id | INTEGER | FK → Clip.id, NOT NULL | |
| position | INTEGER | NOT NULL | Order in episode timeline |
| transition_type | TEXT | DEFAULT 'cut' | cut, dissolve, fade, wipe |
| PRIMARY KEY | | (episode_id, clip_id) | Composite key |

#### ContentIDClaim

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INTEGER | PK, AUTOINCREMENT | Internal identifier |
| clip_id | INTEGER | FK → Clip.id | Specific clip if known |
| film_id | INTEGER | FK → Film.id, NOT NULL | Source film |
| episode_id | INTEGER | FK → Episode.id | Which episode triggered claim |
| claimant | TEXT | NOT NULL | Studio or rights holder |
| claim_type | TEXT | NOT NULL | "audio", "visual", "both" |
| status | TEXT | DEFAULT 'active' | active, disputed, released, monetized |
| revenue_impact | TEXT | | "none", "shared", "blocked" |
| filed_date | TEXT | | ISO 8601 date |
| resolved_date | TEXT | | ISO 8601 date |
| notes | TEXT | | Dispute details, resolution notes |

---

## 4. Technology Evaluation

### Object Detection

| Approach | Pros | Cons | M3 Perf | Recommendation |
|----------|------|------|---------|----------------|
| **YOLOv8-nano** | Fastest inference, 3.2M params, 80 COCO classes, runs well on MPS (Metal) | Lowest accuracy of YOLO family, generic training data | ~400 fps | **V1 baseline** -- start here |
| **YOLOv8-small** | Better accuracy (11.2M params), same 80 classes, still fast on M3 | 2x slower than nano, still generic data | ~200 fps | **V2 upgrade** -- once pipeline is stable |
| **YOLOv8-small fine-tuned** | Cinema-specific accuracy: handles film grain, aspect ratios, low-light, B&W | Requires annotated training data (500-1000 frames per object), training time | ~180 fps | **V3 goal** -- use Object Lessons back-catalog as ground truth |
| **DETR (DEtection TRansformer)** | Transformer-based, better contextual reasoning, 91 COCO classes | 6-10x slower than YOLO, heavier memory footprint (~2GB) | ~30 fps | **V4 optional** -- only if transformer context proves valuable |
| **CLIP (OpenAI)** | Text-to-image search: "find a scene with someone pouring milk" | Not object detection -- computes frame-text similarity, no bounding boxes | ~50 fps (embedding) | **Complementary** -- add as search layer over detection results |
| **Grounding DINO** | Open-vocabulary detection: detect any object from text prompt | Heavier than YOLO (~1.5GB), slower | ~15 fps | **V3 alternative** -- if fine-tuning proves too costly |

**V1 decision: YOLOv8-nano via Ultralytics Python API.** The `ultralytics` package handles model loading, MPS acceleration on Apple Silicon, and result parsing. COCO's 80 classes cover many Object Lessons targets (bottle, cup, knife, fork, clock, book, etc.). Objects not in COCO (e.g., typewriter, gramophone, rotary phone) will require V3 fine-tuning or CLIP-based search.

### Video Processing

| Tool | Role | Notes |
|------|------|-------|
| **ffmpeg** (via subprocess) | Frame extraction, clip cutting, scene detection, format conversion | Industry standard, stream copy avoids re-encoding, `select` filter for scene detection |
| **ffprobe** (via subprocess) | Metadata extraction | Codec, duration, resolution, bitrate |
| **PyAV** | Programmatic frame access | Python bindings for libav/ffmpeg, faster than subprocess for per-frame work |
| **Pillow** | Thumbnail generation, frame preprocessing | Resize, crop, format conversion before model inference |

**Decision:** ffmpeg/ffprobe via subprocess for clip extraction and metadata. PyAV for frame extraction during detection (avoids writing 7,200 temporary frame files to disk -- decode frames in-memory, pass directly to YOLO).

### Database

| Option | Pros | Cons | Decision |
|--------|------|------|----------|
| **SQLite + FTS5** | Zero-config, single file, stdlib, FTS5 for full-text search | No concurrent writes (not an issue for solo operator) | **Use this** |
| **PostgreSQL + pgvector** | Semantic search via embeddings, concurrent access | Requires server, overkill for solo | Future option if Chris needs shared access |
| **DuckDB** | Fast analytics, Parquet export | Less mature for OLTP workloads | Not needed |

### Python Packaging

| Component | Package |
|-----------|---------|
| CLI framework | `click` (consistent with organvm-engine) |
| Object detection | `ultralytics` (YOLOv8) |
| Frame decoding | `av` (PyAV) |
| Video processing | `ffmpeg` / `ffprobe` (subprocess, system install via Homebrew) |
| Image handling | `Pillow` |
| Database | `sqlite3` (stdlib) |
| Testing | `pytest` |
| Linting | `ruff` |

---

## 5. MVP Definition

### Phase 1: Manual + Database (1-2 weeks)

**No object detection.** The operator manually timestamps clips (as they do now), but stores everything in a structured, searchable database instead of spreadsheets/notes.

**Deliverables:**
- SQLite database with full schema (all 7 tables).
- CLI: `materia ingest`, `materia films`, `materia clip add/list`, `materia search`, `materia assemble`, `materia export`, `materia episodes`, `materia track`.
- Batch ingestion from a media library directory.
- Full-text search across all metadata fields.
- EDL export for rough cut timelines.
- Thumbnail generation for visual clip browsing.
- `seed.yaml` and ORGANVM registry entry.

**What this unlocks:** Immediate productivity gain. Every clip ever found is searchable. Episode assembly moves from "scroll through notes" to "query the database." Coverage gaps become visible. Content ID history accumulates.

**Test plan:**
- Unit tests for all database operations (CRUD, search, export).
- Integration test: ingest a film, add clips manually, search, assemble, export EDL.
- Validate EDL output against DaVinci Resolve import.

### Phase 2: Semi-Automated Detection (2-4 weeks)

**YOLOv8-nano object detection with human review.**

**Deliverables:**
- Frame extraction pipeline (uniform + scene-change sampling).
- YOLOv8-nano inference via Ultralytics API with MPS acceleration.
- Detection storage with confidence scores and bounding boxes.
- Review workflow: operator confirms/rejects each detection.
- Automatic clip extraction from confirmed detections.
- CLI: `materia detect`, `materia review`, `materia detections`.

**What this unlocks:** A 2-hour film that took 2-3 hours to scrub manually now takes ~2 minutes for detection + 10-20 minutes for review. 10x time reduction on the research phase.

**Test plan:**
- Unit tests for frame extraction (uniform, scene-change).
- Unit tests for detection pipeline (mock YOLO inference).
- Integration test: ingest film, detect objects, review, extract clips.
- Benchmark: measure detection time and accuracy on 5 known films with pre-labeled ground truth.

### Phase 3: Full Automation (1-3 months)

**Fine-tuned model, semantic search, batch processing.**

**Deliverables:**
- Training data pipeline: annotate existing Object Lessons episodes as ground truth.
- Fine-tuned YOLOv8-small on cinema-specific data.
- CLIP-based semantic search: "find scenes where someone pours a glass of milk."
- Batch processing: queue an entire media library for overnight detection.
- Confidence-based auto-extraction: clips above threshold are extracted without review.
- Dashboard (Streamlit or CLI-based TUI) for visual clip browsing.

**What this unlocks:** Fully automated pipeline. Point it at a library of 500 films, come back in the morning with a database of every detected object appearance. Episode research drops from weeks to hours.

**Test plan:**
- Fine-tuned model evaluation: precision/recall on held-out test set.
- CLIP search evaluation: relevance ranking on known queries.
- End-to-end pipeline test: batch ingest 10 films, detect, extract, assemble episode.
- Performance regression: ensure batch processing stays under memory limits.

---

## 6. System Constraints

### Hardware

| Resource | Constraint | Mitigation |
|----------|-----------|------------|
| **RAM** | 16 GB (M3 MacBook) | YOLOv8-nano (~50 MB model) or -small (~100 MB). Process one film at a time. Decode frames in-memory via PyAV (do not write 7,200 temp files). |
| **GPU** | Apple M3 integrated (MPS) | Ultralytics supports MPS backend. Expect 200-400 fps for YOLO-nano. Not viable for DETR -- defer to V4. |
| **CPU** | 8-core M3 | ffmpeg operations are CPU-bound. Clip extraction parallelizable across cores. |
| **Disk** | Plan for 1-2 TB total | Films: 2-8 GB each (50-500 films = 100 GB - 4 TB). Clips: 50-200 MB per film. Thumbnails: ~5 MB per film. Database: <50 MB. External SSD recommended for media library. |

### Processing Time Estimates

| Operation | Time per Film (2hr) | Notes |
|-----------|---------------------|-------|
| Ingest (metadata + hash) | ~30 seconds | SHA-256 on 4 GB file |
| Frame extraction (1 fps) | ~60 seconds | 7,200 frames via PyAV |
| Scene-change detection | ~60 seconds | ffmpeg scene filter |
| YOLOv8-nano inference | ~18-36 seconds | 7,200 frames at 200-400 fps |
| YOLOv8-small inference | ~36-72 seconds | 7,200 frames at 100-200 fps |
| Clip extraction (10 clips) | ~20 seconds | Stream copy, no re-encode |
| Total (uniform + nano) | ~2-3 minutes | End-to-end per film |
| Total (scene-change + nano) | ~1-2 minutes | Reduced frame count |

**Batch estimate:** 60 films for one Object Lessons episode at 3 minutes each = 3 hours unattended. Overnight batch is viable for up to ~200 films.

### Copyright

- All processing is local. No copyrighted content is uploaded to cloud services.
- Source films are locally-owned media (physical media rips, legitimate digital purchases).
- Extracted clips are used under fair use for transformative commentary and criticism.
- The system tracks Content ID claims to inform editorial decisions (shorter clips, audio replacement, avoidance of high-risk sources).
- No clips are distributed outside the Object Lessons channel. The database is a production tool, not a distribution platform.

---

## 7. File System Layout

```
materia-collider/
├── src/
│   └── materia/
│       ├── __init__.py
│       ├── cli/                  # Click CLI commands
│       │   ├── __init__.py
│       │   ├── ingest.py
│       │   ├── detect.py
│       │   ├── extract.py
│       │   ├── tag.py
│       │   ├── search.py
│       │   ├── assemble.py
│       │   ├── track.py
│       │   ├── films.py
│       │   ├── clips.py
│       │   ├── episodes.py
│       │   └── stats.py
│       ├── db/                   # Database layer
│       │   ├── __init__.py
│       │   ├── schema.py         # Table definitions, migrations
│       │   ├── models.py         # Dataclasses for Film, Object, Detection, etc.
│       │   └── queries.py        # Query builders, search, FTS
│       ├── pipeline/             # Core processing pipeline
│       │   ├── __init__.py
│       │   ├── ingest.py         # Metadata extraction, hashing
│       │   ├── detect.py         # YOLO inference, frame sampling
│       │   ├── extract.py        # Clip cutting, format conversion
│       │   ├── assemble.py       # Episode assembly, gap analysis
│       │   └── export.py         # EDL, FCPXML, Premiere XML
│       ├── video/                # Video utilities
│       │   ├── __init__.py
│       │   ├── frames.py         # Frame extraction (PyAV)
│       │   ├── scenes.py         # Scene-change detection (ffmpeg)
│       │   ├── ffmpeg.py         # ffmpeg/ffprobe wrappers
│       │   └── thumbnails.py     # Thumbnail generation
│       └── models/               # ML model management
│           ├── __init__.py
│           ├── yolo.py           # YOLOv8 wrapper
│           ├── clip_search.py    # CLIP-based semantic search (V3)
│           └── registry.py       # Model version tracking
├── tests/
│   ├── conftest.py               # Fixtures: temp DB, sample frames
│   ├── test_db.py
│   ├── test_ingest.py
│   ├── test_detect.py
│   ├── test_extract.py
│   ├── test_assemble.py
│   ├── test_search.py
│   └── test_export.py
├── data/
│   └── objects.json              # Default object catalog with aliases
├── pyproject.toml
├── seed.yaml
├── CLAUDE.md
└── README.md
```

**Data directory (outside repo, configurable via env var):**

```
$MATERIA_DATA_DIR/               # Default: ~/.materia/
├── materia.db                   # SQLite database
├── frames/                      # Extracted frames (organized by film hash)
│   └── <film-hash>/
│       ├── uniform/             # Uniform-sampled frames
│       └── scene/               # Scene-change frames
├── clips/                       # Extracted clips (organized by film hash)
│   └── <film-hash>/
│       ├── preview/             # H.264 720p previews
│       └── edit/                # ProRes masters
├── thumbnails/                  # Clip and film thumbnails
│   ├── films/
│   └── clips/
└── exports/                     # EDL, FCPXML output files
```

---

## 8. Integration Points

### ORGANVM Registry

Register as an ORGAN-III (Ergon) repository:

```yaml
# seed.yaml
schema_version: "1.0"
organ: III
organ_name: Ergon
repo: materia-collider
org: labores-profani-crux
metadata:
  implementation_status: ACTIVE
  tier: standard
  promotion_status: LOCAL
  language: python
  tags: [video-analysis, object-detection, clip-management, amp-lab]
  ci_workflow: ci.yml
produces:
  - type: content_metadata
    description: "Structured clip database, episode timelines, coverage reports"
    consumers: [organvm-vii-kerygma]
consumes:
  - type: media_files
    source: local
    description: "Film files from local media library"
```

**Note on naming collision:** The `meta-organvm/materia-collider` repo is a pre-codified idea space under META. This film-scrubbing system is a distinct, codified product under ORGAN-III. Options:
1. Rename this to `object-lessons-scrubber` to avoid confusion.
2. Graduate the name `materia-collider` from META to ORGAN-III, repurposing it.
3. Use `materia-collider` for this and rename the META repo to `idea-bench` or similar.

Decision deferred -- see Open Questions.

### Kerygma Pipeline (ORGAN-VII)

When an Object Lessons episode is published:
- `content.published` event triggers distribution via kerygma-profiles.
- Episode metadata (title, object, film count, duration) feeds into social media posts.
- Kerygma profile for AMP Lab channel handles platform-specific formatting.

### Praxis-Perpetua (META)

- Episode production SOP references Materia Collider workflow stages.
- Session logs for AMP Lab production sessions stored in `praxis-perpetua/sessions/`.
- Content ID dispute procedures documented as an SOP.

### Alchemia-Ingestvm (META)

Shared ingestion pattern:

| Alchemia | Materia Collider | Mapping |
|----------|-----------------|---------|
| INTAKE | INGEST | Accept raw material, extract metadata |
| ABSORB | DETECT + TAG | Classify and enrich |
| ALCHEMIZE | EXTRACT + ASSEMBLE | Transform into output |

No code sharing needed -- the conceptual parallel is useful for documentation and mental model consistency.

### Organvm-Engine Metrics

Surface in system dashboard:
- `films_ingested`: total film records.
- `clips_extracted`: total clip records.
- `objects_cataloged`: total object records.
- `episodes_published`: total published episodes.
- `detection_coverage`: percentage of ingested films that have been detection-scanned.
- `episode_velocity`: episodes published per month (rolling 3-month average).

---

## 9. Open Questions

### Q1: Naming and organ placement

The name `materia-collider` is currently used by a pre-codified idea space under META-ORGANVM. This film-scrubbing system is a codified product. Options:

| Option | Pros | Cons |
|--------|------|------|
| **A: Use `materia-collider` in ORGAN-III** | Powerful name, thematic fit ("colliding" objects with films) | Naming collision with META repo |
| **B: Use `object-lessons-scrubber`** | Descriptive, no collision | Boring name, ties to one channel |
| **C: Rename META repo, use `materia-collider` here** | Clean namespace | Disrupts existing references |

**Recommendation:** Option A. The META `materia-collider` is pre-codified by design -- this is a graduation event. Move the idea-space content to `intake/` or `bench/` within the new codified repo, and repurpose the name for its production incarnation.

### Q2: CLIP-based semantic search vs. pure object detection

These are complementary, not competing:
- **Object detection** (YOLO) answers: "Is there a bottle in this frame?" Binary, bounded, fast.
- **Semantic search** (CLIP) answers: "Find frames that look like someone pouring milk." Fuzzy, contextual, slower.

**Recommendation:** Build on object detection first (V1-V2). Add CLIP as a secondary search interface in V3. CLIP is especially valuable for objects not in the COCO class list and for queries about actions rather than objects ("someone drinking" vs. "cup").

### Q3: Shared database with collaborator

Chris (AMP Lab co-creator) may need access to the clip database for episode planning.

| Option | Mechanism | Complexity |
|--------|-----------|------------|
| **SQLite file sync** | Share via Dropbox/iCloud | Low -- but no concurrent writes |
| **PostgreSQL** | Shared server (Neon, Supabase) | Medium -- requires migration |
| **Export/import** | JSON/CSV dumps per episode | Low -- manual but sufficient for now |

**Recommendation:** Start with SQLite (solo operator). If Chris needs access, add a `materia export --format json` command and share per-episode data bundles. Migrate to PostgreSQL only if concurrent editing becomes a real need.

### Q4: Training data from back-catalog

Existing Object Lessons episodes are annotated ground truth: the final edit implicitly labels which objects appear at which timestamps. This can be reverse-engineered:

1. For each published episode, note the object and the films used.
2. For each film clip in the episode, extract the timestamp range.
3. Run frame extraction on those ranges.
4. Label extracted frames as positive examples for the object.
5. Sample random frames from the same films as negative examples.

This produces a cinema-specific training dataset without manual annotation. Estimate: 10 episodes x 50 clips x 5 frames per clip = 2,500 positive examples per object. Sufficient for fine-tuning.

**Recommendation:** Yes, build the annotation pipeline as part of V3. The back-catalog is the training data moat.

### Q5: Legal considerations

Automated clip extraction at scale does not change the fair use analysis -- the transformation is in the commentary, not the extraction. The system is a production tool, not a distribution mechanism. However:

- Keep clips short (under 10 seconds preferred, under 30 seconds maximum).
- Never distribute raw clips outside the channel.
- Document the transformative purpose in episode descriptions.
- Track Content ID claims systematically to identify patterns and adjust source selection.

**Recommendation:** No additional legal review needed for the tool itself. Fair use analysis applies to the published episodes, which already have a strong transformative argument. The system makes the existing workflow faster, not legally different.

---

## 10. Success Criteria

### V1 (Phase 1) is successful if:

- [ ] Ingesting 10 films takes under 10 minutes total.
- [ ] Manual clip entry is faster than the current spreadsheet/notes workflow.
- [ ] `materia search <object>` returns results in under 1 second.
- [ ] EDL export opens correctly in DaVinci Resolve.
- [ ] Coverage gap analysis identifies at least one useful missing film per object.

### V2 (Phase 2) is successful if:

- [ ] Detection on a 2-hour film completes in under 5 minutes.
- [ ] Precision > 70% for COCO-native objects (bottle, cup, knife, clock).
- [ ] Recall > 50% for COCO-native objects (misses are acceptable; false positives waste time).
- [ ] Human review of 100 detections takes under 15 minutes.
- [ ] Total time from "new film" to "clips in database" is under 30 minutes (including review).

### V3 (Phase 3) is successful if:

- [ ] Fine-tuned model achieves > 80% precision and > 70% recall on cinema-specific objects.
- [ ] CLIP search returns relevant results for natural-language queries.
- [ ] Batch processing of 100 films completes overnight (under 8 hours).
- [ ] Episode assembly (search + gap analysis + rough cut export) takes under 30 minutes per episode.

---

## 11. Risk Register

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| YOLO misses objects in B&W / low-light / unusual aspect ratios | Medium | High | Fine-tuning in V3. Manual fallback in V1-V2. |
| 16 GB RAM insufficient for larger models (DETR, Grounding DINO) | High | Medium | Stick with YOLO-nano/small. Defer heavy models to cloud or future hardware. |
| Object Lessons objects not in COCO class list | High | High | 52 of 80 COCO classes are relevant. Non-COCO objects use manual entry (V1) or CLIP search (V3). |
| Storage exceeds available disk for large film libraries | Medium | Medium | External SSD. Purge extracted frames after detection (keep only clips + thumbnails). |
| ffmpeg version incompatibilities across macOS updates | Low | Low | Pin Homebrew ffmpeg version. Test after macOS upgrades. |
| Fine-tuning requires more training data than back-catalog provides | Medium | Medium | Supplement with manual annotation. Use active learning (model flags uncertain frames for human review). |
| Content ID claims make certain films unusable | Low | High | Track and avoid. Flag high-risk studios in the risk list. Prefer independent films, pre-1964 works (public domain). |

---

## Appendix A: COCO Classes Relevant to Object Lessons

The COCO dataset defines 80 object classes. The following are directly relevant to Object Lessons episodes (current or planned):

**High relevance (likely episode subjects):**
bottle, wine glass, cup, fork, knife, spoon, bowl, banana, apple, orange, sandwich, cake, dining table, chair, couch, bed, clock, vase, scissors, book, teddy bear, suitcase, umbrella, handbag, tie, hat

**Medium relevance (contextual or supporting):**
person, car, bicycle, motorcycle, bus, train, truck, boat, traffic light, fire hydrant, stop sign, bench, bird, cat, dog, horse, potted plant, laptop, cell phone, remote, keyboard, mouse, tv/monitor, microwave, oven, toaster, refrigerator, sink, toilet

**Not in COCO (requires V3 fine-tuning or CLIP search):**
typewriter, gramophone, rotary phone, cigarette case, pocket watch, monocle, top hat, candelabra, quill pen, telegraph, abacus, hourglass, music box, lantern, compass, telescope, magnifying glass, chess set

## Appendix B: Example EDL Output

```
TITLE: Object Lessons - Milk
FCM: NON-DROP FRAME

001  AX       V     C        00:00:00:00 00:00:08:15 00:00:00:00 00:00:08:15
* FROM CLIP NAME: milk_psycho_1960_001.mov
* COMMENT: Psycho (1960) - Marion Crane's apartment, glass of milk on nightstand

002  AX       V     C        00:00:08:15 00:00:14:22 00:00:08:15 00:00:23:07
* FROM CLIP NAME: milk_clockwork_1971_001.mov
* COMMENT: A Clockwork Orange (1971) - Korova Milk Bar, milk-plus dispensers

003  AX       V     C        00:00:14:22 00:00:22:10 00:00:23:07 00:00:45:17
* FROM CLIP NAME: milk_no_country_2007_001.mov
* COMMENT: No Country for Old Men (2007) - Chigurh drinks milk from the carton
```

## Appendix C: Related Prior Art

| Tool | What It Does | Why It Is Not Sufficient |
|------|-------------|-------------------------|
| **Google Video Intelligence API** | Cloud-based object detection in video | Requires uploading copyrighted content. No local processing. No clip management. |
| **Amazon Rekognition Video** | Cloud-based label detection | Same cloud upload problem. Pay-per-minute pricing adds up for 500+ films. |
| **Shotdetect** | Open-source scene boundary detection | Scene detection only. No object detection. No database. |
| **VLC media player** | Manual scrubbing with bookmarks | What we do now. No search, no structure, no automation. |
| **Kyno** | Professional media management with metadata | Commercial, expensive. No object detection. Focused on camera originals, not cinema analysis. |
| **FilmGrab** | Screenshot database of films | Static frames only. No temporal data. No clip extraction. Web-based, not local. |

None of these tools combine local object detection + structured clip management + episode assembly support + Content ID tracking. Materia Collider is purpose-built for this workflow.
