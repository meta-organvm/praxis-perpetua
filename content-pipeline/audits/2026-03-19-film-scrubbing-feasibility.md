# Film-Scrubbing System: Technical Feasibility Study

**Date:** 2026-03-19
**Status:** Research phase — no code yet
**Context:** AMP Lab / Object Lessons video essay series
**Organ placement:** ORGAN-II (Poiesis) if bespoke to Object Lessons; ORGAN-III (Ergon) if generalized as a product

---

## Executive Summary

Building an automated film-scrubbing system that ingests films, detects specific objects (milk, telephones, mirrors, etc.) across eras, and extracts searchable clip collections is **technically feasible with existing open-source tools**. No novel research is required — the system assembles proven components (YOLO-World, SigLIP, SAM2, FFmpeg, PySceneDetect) into a pipeline that doesn't currently exist for film studies purposes.

**Key findings:**

- A 4-stage cascade pipeline (frame sampling → embedding sweep → precise detection → tracking) can process 100 feature films for **under $20 cloud compute** or **~10 hours on an M3 MacBook**
- The critical challenge is **era variation** — a 1920s candlestick telephone shares almost no visual features with a 2020s smartphone. Multi-prompt ensembling and few-shot fine-tuning address this
- **No existing system** does what this proposes. The closest tools (PyCinemetrics, ShotDeck, Twelve Labs) each cover fragments of the pipeline but none offer cross-corpus object search with clip extraction
- **Fair use strongly favors** the Object Lessons format (short clips, many films, critical commentary). The practical constraint is YouTube's Content ID, not the law
- **MVP is achievable in 2-4 weeks** of engineering time: SigLIP frame scanning + SQLite search + FFmpeg clip extraction. Full system with tracking and web UI adds 4-8 weeks

---

## Table of Contents

1. [Architecture Overview](#1-architecture-overview)
2. [Model Comparison & Selection](#2-model-comparison--selection)
3. [The Era Variation Problem](#3-the-era-variation-problem)
4. [MVP Scope vs Full Scope](#4-mvp-scope-vs-full-scope)
5. [Compute Requirements & Cost Estimates](#5-compute-requirements--cost-estimates)
6. [Recommended Tech Stack](#6-recommended-tech-stack)
7. [Legal Considerations](#7-legal-considerations)
8. [Prior Art & Competitive Landscape](#8-prior-art--competitive-landscape)
9. [Known Risks & Limitations](#9-known-risks--limitations)
10. [Decision Framework](#10-decision-framework)

---

## 1. Architecture Overview

### Core Pipeline (4 stages)

```
┌─────────────────────────────────────────────────────────────────────┐
│                    FILM-SCRUBBING PIPELINE                         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  STAGE 1: INGEST + SAMPLE              STAGE 2: BROAD SWEEP        │
│  ┌──────────────┐  ┌──────────┐        ┌──────────────────┐        │
│  │ FFmpeg/Decord │→ │ PyScene- │→       │ SigLIP/CLIP      │        │
│  │ Frame Extract │  │ Detect   │        │ Embedding Search │        │
│  └──────────────┘  └──────────┘        └──────────────────┘        │
│  1-2 FPS uniform    shot boundary       multi-prompt text           │
│  + scene changes    keyframes           cosine similarity           │
│                                         ~30-50 frames/sec (M3)     │
│                            │                      │                 │
│                            └───────┬──────────────┘                 │
│                                    │ candidate frames               │
│                                    ▼ (10-30% of total)              │
│  STAGE 3: PRECISE DETECTION        STAGE 4: TRACKING               │
│  ┌──────────────────┐              ┌──────────────────┐            │
│  │ Grounding DINO   │→             │ SAM2 Video       │            │
│  │ or YOLO-World    │              │ Object Tracking  │            │
│  └──────────────────┘              └──────────────────┘            │
│  bounding boxes + class             per-frame masks                 │
│  era-aware multi-prompts            temporal propagation             │
│  ~2-25 FPS (M3)                     ~10-15 FPS (M3)                │
│                                                                     │
│                            │                                        │
│                            ▼                                        │
│  ┌──────────────────────────────────────────┐                      │
│  │ STORE: SQLite + sqlite-vec               │                      │
│  │ - Frame metadata (film, timestamp, etc.) │                      │
│  │ - Detection results (bbox, class, conf)  │                      │
│  │ - SigLIP embeddings (768-dim vectors)    │                      │
│  │ - Clip extraction commands (FFmpeg)      │                      │
│  └──────────────────────────────────────────┘                      │
│                            │                                        │
│                            ▼                                        │
│  ┌──────────────────────────────────────────┐                      │
│  │ QUERY + ASSEMBLE                         │                      │
│  │ "Show me all telephones" → ranked clips  │                      │
│  │ FFmpeg clip extraction → working files   │                      │
│  └──────────────────────────────────────────┘                      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Why 4 stages?

No single model handles all requirements. The cascade pattern reduces compute by 70-90%:

| Stage | Purpose | Speed | Precision | Processes |
|-------|---------|-------|-----------|-----------|
| 1. Sample | Extract frames intelligently | Fastest | N/A | 100% of video |
| 2. Sweep | Flag candidate frames | Fast | Moderate | 100% of frames |
| 3. Detect | Localize objects precisely | Moderate | High | 10-30% of frames |
| 4. Track | Propagate through time | Moderate | High | Detected segments only |

---

## 2. Model Comparison & Selection

### Detection Models

| Model | Type | Zero-Shot COCO AP | Speed (A100) | Speed (M3 est.) | VRAM (FP16) | Open Vocabulary? |
|-------|------|-------------------|-------------|-----------------|-------------|-----------------|
| YOLOv8-X | Closed-set | 53.9 (fine-tuned) | 80 FPS | 8-12 FPS | ~1.0 GB | No (80 COCO classes) |
| YOLOv10-X | Closed-set | 54.4 (fine-tuned) | 110+ FPS | 10-15 FPS | ~1.0 GB | No |
| **YOLO-World-L** | **Open-set** | **~46 (transfer)** | **52 FPS** | **15-25 FPS** | **~1.2 GB** | **Yes (text prompts)** |
| **Grounding DINO** | **Open-set** | **52.5 (zero-shot)** | **7-10 FPS** | **2-4 FPS** | **~2.0 GB** | **Yes (rich phrases)** |
| Florence-2-Large | Unified | ~46 | 8-12 FPS | 3-5 FPS | ~2.5 GB | Yes |

**Recommendation:** Use **YOLO-World** for high-throughput batch processing, **Grounding DINO** for accuracy-critical passes on candidate frames. The two are complementary, not competitive.

### Embedding Models (for similarity search)

| Model | Dims | Zero-Shot ImageNet | Speed (M3) | VRAM | Era Robustness |
|-------|------|-------------------|-----------|------|----------------|
| CLIP ViT-B/32 | 512 | 63.2% | ~50 img/s | ~0.3 GB | Moderate |
| CLIP ViT-L/14 | 768 | 76.2% | ~25 img/s | ~0.9 GB | Moderate |
| **SigLIP ViT-L/16@384** | **768** | **84.5%** | **~20 img/s** | **~1.0 GB** | **Better (10B training pairs)** |
| EVA-02-CLIP-E/14+ | 768 | 82.0% | ~15 img/s | ~1.2 GB | Good |

**Recommendation:** **SigLIP** — strictly superior to CLIP for the same use case. 8+ percentage points better on zero-shot classification, trained on 25x more data. Drop-in replacement.

### Segmentation / Tracking

| Model | Purpose | Speed (M3) | VRAM | Video Native? |
|-------|---------|-----------|------|---------------|
| SAM (ViT-H) | Single-frame segmentation | ~5 FPS | ~2.5 GB | No |
| **SAM2 (Hiera-L)** | **Video object tracking** | **~10-15 FPS** | **~1.5 GB** | **Yes** |

**Recommendation:** **SAM2** — native video tracking with memory bank for re-identification after occlusion. Runs on M3 within memory budget.

### Video-Understanding Models (contextual verification — optional Stage 5)

| Model | Size | Capability | Speed | Best For |
|-------|------|-----------|-------|----------|
| Qwen2-VL-7B | 7B | Native video input, temporal reasoning | ~1-3 FPS | "Is this a telephone or similar object?" |
| Florence-2 | 771M | Unified captioning + detection + grounding | ~3-5 FPS | Multi-task verification |
| CogVLM2-Video | ~19B | Video understanding, temporal reasoning | Too large for M3 | Cloud-only contextual analysis |

**Recommendation:** Reserve VLMs for low-confidence disambiguation. Too slow and large for primary detection.

---

## 3. The Era Variation Problem

This is the hardest technical challenge. A rotary desk phone (1940s) shares zero visual features with a smartphone (2020s), yet both are "telephones."

### Approaches ranked by effectiveness

**1. Multi-prompt ensembling (zero-shot, no training needed)**

For each target object, define a prompt bank covering era variants:

```yaml
telephone:
  prompts:
    - "telephone"
    - "rotary telephone"
    - "candlestick telephone"
    - "wall telephone"
    - "desk phone"
    - "touch-tone phone"
    - "payphone"
    - "phone booth"
    - "cell phone"
    - "smartphone"
    - "phone handset"
    - "phone receiver"
    - "telephone cord"
  era_specific:
    1890-1930: "candlestick telephone, wall-mounted telephone"
    1930-1970: "black rotary desk telephone, wall telephone"
    1970-2000: "touch-tone telephone, cordless phone"
    2000-2015: "flip phone, cell phone, BlackBerry"
    2015-present: "smartphone, iPhone"
```

Union all detections across prompts, apply NMS to deduplicate. Works with both YOLO-World (negligible cost — prompts are pre-encoded) and Grounding DINO (linear cost per prompt).

**2. Hierarchical CLIP/SigLIP retrieval**

- Level 1: Broad embedding ("communication device") — high recall, low precision
- Level 2: Era-specific embeddings ("1950s rotary telephone") — classify the variant
- Level 3: Reference image bank — nearest-neighbor match against 20-50 curated historical images per object

**3. Few-shot fine-tuning (most effective, requires data collection)**

Collect 10-50 examples per object variant from film stills databases (ShotDeck, MovieStillsDB, FILMGRAB). Fine-tune YOLO-World — its re-parameterizable architecture makes this lightweight (~1-2 hours on a single GPU for 5-10 object categories).

**4. VLM semantic detection (highest recall, slowest)**

Prompt Qwen2-VL: "Is there any type of telephone or phone visible in this image? Include historical telephones, rotary phones, wall phones, and any communication device."

The LLM's world knowledge bridges gaps in visual training data. Use sparingly on ambiguous detections only.

### Recommended strategy

Start with **approach 1 + 2** (zero-shot, no training). Measure recall on a test set of 10 films with known telephone appearances. If recall is below 80%, add **approach 3** (few-shot fine-tuning) for the weakest object categories.

---

## 4. MVP Scope vs Full Scope

### MVP (2-4 weeks engineering)

**Goal:** Given a film and an object name, find all frames containing that object and extract clips.

| Component | Implementation | Notes |
|-----------|---------------|-------|
| Frame extraction | FFmpeg at 1 FPS | `ffmpeg -i film.mp4 -vf "fps=1" frames/%04d.jpg` |
| Object detection | SigLIP embedding search | Multi-prompt cosine similarity against frame embeddings |
| Storage | SQLite + sqlite-vec | Embeddings + metadata per frame |
| Clip extraction | FFmpeg | Auto-generate extraction commands from detection timestamps |
| Interface | Python CLI | `scrub --film "Psycho" --object "milk" --threshold 0.25` |
| Film library | Local files (DVD/Blu-ray rips) | No streaming integration |

**MVP delivers:**
- Frame-level detection (which frames contain the object)
- Confidence scores per frame
- Auto-extracted clips as MP4 files
- Searchable database of all frames + detections

**MVP does NOT include:**
- Bounding box localization (knows *which* frames, not *where* in the frame)
- Temporal tracking (no shot-level continuity)
- Web UI
- Multi-film comparative views
- Era-aware fine-tuning

### Full System (4-8 additional weeks)

| Component | Implementation | Notes |
|-----------|---------------|-------|
| Scene detection | PySceneDetect (TransNetV2) | Shot boundary detection for intelligent sampling |
| Precise detection | Grounding DINO + YOLO-World | Bounding boxes with era-aware multi-prompts |
| Object tracking | SAM2 | Video object segmentation across shots |
| Screen-time metrics | Computed from SAM2 masks | % of frame occupied, total screen-time per film |
| Reference image bank | Curated per object per era | 20-50 reference images from ShotDeck/FILMGRAB |
| Web UI | FastAPI + HTMX (or Next.js) | Search, browse, assemble clips, side-by-side comparison |
| Cloud processing | Modal serverless | Burst to GPU for batch processing of full library |
| Metadata enrichment | TMDb API integration | Auto-tag clips with film title, year, director, genre |
| Export formats | EDL, FCPXML, individual clips | Direct import into DaVinci Resolve / Premiere Pro |

### Future expansions (not in initial scope)

- Audio analysis (detect telephone rings, dialogue about objects)
- Multi-object correlation ("scenes where both milk AND a telephone appear")
- Automated montage assembly (arrange clips by era, visual similarity, or narrative arc)
- Collaborative annotation (Chris can review/correct AI detections via web UI)
- Public-facing searchable archive (a la Kinolab but automated)

---

## 5. Compute Requirements & Cost Estimates

### Local Processing (M3 16GB MacBook)

| Operation | Speed (M3) | Time per Film (2hr, 1 FPS) | Time for 100 Films |
|-----------|-----------|---------------------------|-------------------|
| Frame extraction (FFmpeg) | Real-time | ~2 min | ~3 hrs |
| SigLIP embedding | ~20 img/s | ~6 min | ~10 hrs |
| YOLO-World detection | ~15-25 FPS | ~5-8 min | ~8-13 hrs |
| Grounding DINO (candidates only) | ~2-4 FPS | ~5-15 min | ~8-25 hrs |
| SAM2 tracking (detected segments) | ~10-15 FPS | varies | varies |

**Total local estimate for 100 films (MVP pipeline, 1 FPS):** ~10-15 hours
**Feasibility:** Overnight batch — completely viable on M3.

### Memory Budget (M3 16GB)

| Component | Memory |
|-----------|--------|
| macOS overhead | ~3-4 GB |
| SigLIP ViT-L (FP16) | ~1.0 GB |
| YOLO-World-L (FP16) | ~1.2 GB |
| Frame buffer (batch of 16 @ 1080p) | ~0.1 GB |
| SQLite + embeddings | ~0.2 GB |
| **Total** | **~5.5-6.5 GB** |
| **Available headroom** | **~9-10 GB** |

Running SigLIP + YOLO-World simultaneously fits comfortably. Adding Grounding DINO or SAM2 sequentially (not simultaneously) stays within budget.

### Cloud Processing Costs

| Provider | GPU | Cost/hr | Time for 100 Films (1 FPS) | Total Cost |
|----------|-----|---------|---------------------------|------------|
| **Modal (T4)** | T4 16GB | $0.59/hr | ~2.25 hrs | **$1.33** |
| **Modal (L4)** | L4 24GB | $0.80/hr | ~1.5 hrs | **$1.20** |
| **Modal (A100)** | A100 80GB | $2.50/hr | ~0.75 hrs | **$1.88** |
| GCP Spot (T4) | T4 16GB | $0.09/hr | ~2.25 hrs | **$0.20** |
| RunPod Serverless (L4) | L4 24GB | $0.68/hr | ~1.5 hrs | **$1.02** |
| Lambda Labs (A10) | A10 24GB | $0.75/hr | ~1.5 hrs | **$1.13** |

**Key insight: Cloud compute for this workload is astonishingly cheap.** Under $5 for the entire 100-film corpus at 1 FPS. Even at 5 FPS with full pipeline (SigLIP + Grounding DINO + SAM2): under $50.

### Managed API Costs (for comparison — NOT recommended)

| Service | Cost for 100 Films (9,000 min) |
|---------|-------------------------------|
| Google Video Intelligence | ~$800 |
| AWS Rekognition Video | ~$900 |
| Twelve Labs | ~$297 |

Managed APIs are 50-200x more expensive than self-hosted inference. Skip them.

### Storage Requirements

| Data | Per Film (1 FPS) | 100 Films | Notes |
|------|-----------------|-----------|-------|
| JPEG frames (1080p) | ~1.1 GB | ~110 GB | Can process in-memory to skip disk writes |
| SigLIP embeddings | ~14 MB | ~1.4 GB | 768-dim float32 per frame |
| Detection metadata (JSON) | ~5 MB | ~500 MB | bbox, class, confidence per detection |
| Extracted clips (MP4) | varies | ~10-50 GB | Only clips containing target objects |
| **Total (frames on disk)** | | **~120-160 GB** | |
| **Total (in-memory frames)** | | **~2-52 GB** | Embeddings + metadata only |

---

## 6. Recommended Tech Stack

### Core Pipeline

| Layer | Technology | Why |
|-------|-----------|-----|
| **Language** | Python 3.11+ | Ecosystem dominance for CV/ML. PyTorch, Ultralytics, HuggingFace all Python-first |
| **Frame extraction** | FFmpeg (subprocess) + Decord (Python) | FFmpeg for CLI-level extraction, Decord for GPU-accelerated in-memory frame loading |
| **Scene detection** | PySceneDetect | Mature, multiple algorithms, FFmpeg integration |
| **Embedding model** | SigLIP ViT-L/16@384 (via HuggingFace) | Best zero-shot accuracy, 768-dim embeddings, runs on M3 |
| **Object detection** | YOLO-World-L (Ultralytics) + Grounding DINO (IDEA Research) | Speed (YOLO-World) + accuracy (Grounding DINO). Both open-vocabulary |
| **Object tracking** | SAM2 (Meta) | Native video tracking with memory bank |
| **Storage** | SQLite + sqlite-vec | Zero-infrastructure, single-file, vector search |
| **Metadata** | TMDb API | Film title, year, director, genre auto-enrichment |
| **Clip extraction** | FFmpeg | Surgical clip extraction by timestamp |

### Infrastructure

| Component | Technology | Why |
|-----------|-----------|-----|
| **Package management** | uv (or pip) | Fast, lockfile support |
| **CLI framework** | Click or Typer | Matches ORGANVM CLI patterns |
| **Cloud burst** | Modal | Pay-per-second, scale-to-zero, free $30/month |
| **Database (production)** | PostgreSQL + pgvector (via Neon) | When/if web UI needs multi-client access |
| **Web UI** | FastAPI + HTMX (or Next.js via stakeholder-portal pattern) | Matches existing ORGANVM dashboard stack |
| **Export** | FFmpeg (MP4) + python-fcpxml (FCPXML for NLEs) | Direct import into editing software |

### Python Dependencies (core)

```
# Core pipeline
torch >= 2.3          # PyTorch with MPS backend
ultralytics >= 8.2    # YOLO-World
transformers >= 4.40  # SigLIP, Grounding DINO, Florence-2
segment-anything-2    # SAM2
decord >= 0.6         # GPU video decoding
scenedetect >= 0.6    # PySceneDetect

# Storage + search
sqlite-vec >= 0.1     # Vector search in SQLite

# Utilities
pillow >= 10.0        # Image processing
numpy >= 1.26         # Array operations
tmdbsimple >= 2.9     # TMDb API client
click >= 8.1          # CLI
rich >= 13.0          # Terminal output
```

---

## 7. Legal Considerations

### Fair Use Analysis (17 USC Section 107)

| Factor | Assessment | Reasoning |
|--------|-----------|-----------|
| **1. Purpose and character** | **Strongly favorable** | Transformative: clips serve as evidence for critical argument about objects' cultural meaning across cinema, not as entertainment substitutes. Post-*Warhol v. Goldsmith* (2023), the test is whether the new work serves a "substantially different purpose" — a comparative montage analyzing an object's evolution is categorically different from narrative entertainment |
| **2. Nature of the work** | Slightly unfavorable | Feature films are creative, published works. This factor almost always tilts against fair use in film criticism contexts. Courts treat it as the least significant factor |
| **3. Amount used** | **Favorable** | Short clips (2-10 seconds) from many films. No single film is substantially reproduced. The format structurally limits amount per source |
| **4. Market effect** | **Strongly favorable** | No viewer watches a montage of telephone clips instead of watching any source film. Zero market substitution |

**Overall assessment:** Strong fair use position. The Object Lessons format — short clips from many films with continuous critical commentary — is precisely the kind of comparative critical analysis that most clearly constitutes transformative use.

### Key Case Law

| Case | Relevance |
|------|-----------|
| **Hosseinzadeh v. Klein (2017)** | YouTube reaction video using substantial clips = fair use when constituting "critical commentary" and "decidedly not a market substitute." Most directly applicable precedent |
| **SOFA v. Dodger (2013, 9th Cir.)** | 7-second clip used for "biographical significance" = fair use. Even very short clips are transformative when repurposed for historical/critical commentary |
| **Campbell v. Acuff-Rose (1994, SCOTUS)** | Established transformative use framework. More transformative = other factors weigh less |
| **Warhol v. Goldsmith (2023, SCOTUS)** | New work must serve a *different purpose*, not just add "new expression." Actually *helps* Object Lessons — the purpose (critical analysis) is categorically different from source films (entertainment) |

### YouTube Content ID: The Practical Constraint

Content ID operates independently of fair use law. It flags mechanically via audio/video fingerprinting. The rights holder (not a court) decides the initial outcome: block, monetize, or track.

**Mitigation strategies (from established video essay channels):**

- Keep individual clips under 5-10 seconds
- Never play film audio alone — always layer voiceover commentary
- Remix, reorder, and flip shots rather than presenting them sequentially
- Draw from many films (inherent to Object Lessons format)
- Dispute claims when they arise — many auto-release after dispute
- Accept some revenue-sharing claims as cost of doing business

**Tony Zhou (Every Frame a Painting) disclosed** that he spent approximately one week per video testing edits against Content ID via private uploads. His channel's stylistic decisions — clip length, studio selection, audio remixing — were reverse-engineered from Content ID behavior.

### Film Sourcing

| Method | Legal Status | Practical |
|--------|-------------|-----------|
| **DVD/Blu-ray rips** | Technically violates DMCA Section 1201 (circumventing copy protection). However, 2024 Copyright Office rulemaking renewed exemptions for educators and critics | Standard method used by video essay channels. MakeMKV + HandBrake workflow |
| Streaming captures | Riskier — DMCA exemptions explicitly exclude streaming DRM | Not recommended |
| Public domain films | Clean — pre-1928 works | Internet Archive hosts 1M+ digital films. Covers early cinema only |
| Licensed stock footage | Clean but expensive | Impractical for the volume needed |

**Bottom line:** Physical media (DVDs/Blu-rays) ripped for analysis purposes, combined with the strong fair use defense, is the approach used by essentially every established video essay channel.

### International Note

If Chris operates from outside the US (UK, Canada, EU), fair dealing / quotation right standards may apply instead of US fair use. These are narrower but still support criticism and commentary with proper attribution. Safest approach: operate the channel from a US-based account.

---

## 8. Prior Art & Competitive Landscape

### The Gap

**No existing system does what this proposes** — automated detection of a specific recurring object across a large corpus of films, with automatic clip extraction. The landscape has fragments:

| System | What It Does | What It Lacks |
|--------|-------------|---------------|
| **PyCinemetrics** (2024, academic) | Shot detection + object recognition (VGG19) + color extraction for individual films | Cross-corpus search, era-aware detection, clip extraction pipeline |
| **ShotDeck** (commercial) | 318K hand-tagged film screenshots, searchable by 30+ categories | Stills only (no video clips), entirely human-curated, no object detection |
| **Twelve Labs** (commercial API) | Semantic video search via natural language queries | General-purpose (not film-studies-specific), expensive at scale ($297/100 films), API dependency |
| **Kinolab** (academic platform) | Annotated narrative media clips with controlled vocabulary | Human-curated, DMCA-compliant submission model, not automated |
| **Cinemetrics** (academic database) | Shot-length data for films | Human-submitted, no object detection |
| **Google Video Intelligence** | Label detection + object tracking in video | Generic labels (not film-studies-aware), expensive ($800/100 films) |
| **CLIP.cafe** | Find specific dialogue moments in films | Audio/text-based only, no visual object search |

### Academic Research

| Work | Contribution |
|------|-------------|
| "Recurring Element Detection in Movies" (2012, Springer) | Earliest academic work on detecting recurring visual elements across films — directly relevant concept |
| "Exploring Computer Vision for Film Analysis" (2021, Univ. of Regensburg) | Applied object detection + emotion recognition to 5 canonical films |
| "Object Detection in Movies — Case Study" (2024, Springer) | Object detection specifically in cinema contexts |
| Lev Manovich / Cultural Analytics Lab | Pioneered computational film analysis (color palettes, shot structure visualization) at scale |

### How Film Researchers Currently Work

The answer is largely **manual labor with enormous effort:**

1. Deep personal knowledge from watching thousands of films
2. Hand-curated databases (ShotDeck: years of human tagging)
3. Crowdsourced contributions (Cinemetrics, Internet Movie Firearms Database)
4. Published shooting scripts and continuity reports (rarely digitized)

**This system would be the first automated alternative for the query: "find me every instance of [object] across [film corpus]."**

---

## 9. Known Risks & Limitations

### Technical Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| **False negatives on historical objects** | HIGH | Multi-prompt ensembling + few-shot fine-tuning + curated reference image bank |
| **False positives (similar-looking objects)** | MEDIUM | VLM verification stage for low-confidence detections + human review queue |
| **Film quality variation** (grain, B&W, damaged prints) | MEDIUM | Preprocessing (denoising, histogram equalization) + model robustness testing on B&W footage |
| **Partial/occluded objects** | MEDIUM | SAM2 handles partial occlusion well; multi-prompt helps ("phone handset," "phone cord" as partial cues) |
| **Metaphorical/non-literal appearances** | LOW | Out of scope for MVP; VLMs could address in future ("painting of a telephone on the wall") |
| **4K processing on M3** | LOW | Resize to 1080p before inference — detection models use 640px internally anyway |

### Operational Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| **Film sourcing at scale** | HIGH | Physical media acquisition is slow and expensive. Start with films already owned/accessible. Library partnerships for research access |
| **Content ID blocking published videos** | MEDIUM | Pre-test clips via private uploads; accept revenue-sharing claims; maintain commentary density |
| **Model version churn** | LOW | Pin model versions in requirements; embedding vectors are format-stable |
| **Storage growth** | LOW | In-memory processing eliminates frame storage; embeddings are tiny (~14 MB/film) |

### Scope Risks

| Risk | Mitigation |
|------|------------|
| Over-engineering the pipeline before validating with actual Object Lessons content | MVP first — test with 10 films and 3 objects before building full system |
| Building for one use case when it could be a product | Decide organ placement (II vs III) before v2 engineering. If ORGAN-III, generalize the object prompt system early |
| Chris can't use the tool without ORGANVM context | Decouple the film-scrubbing CLI from ORGANVM infrastructure. Standalone Python package with zero ORGANVM dependencies |

---

## 10. Decision Framework

### Should you build this?

| Question | Answer |
|----------|--------|
| Is it technically feasible? | **Yes** — all components exist, assembly is the work |
| Is the compute affordable? | **Yes** — under $20 cloud or 10 hrs local for 100 films |
| Does it solve a real problem? | **Yes** — manual film scrubbing for Object Lessons is prohibitively labor-intensive |
| Is there prior art to compete with? | **No** — this system would be novel |
| Does it have product potential? | **Yes** — film scholars, video essayists, archivists all lack this tool |

### Recommended Next Steps

1. **Validate with a spike** (1-2 days): Process 3 known films where telephone appearances are already cataloged. Run SigLIP multi-prompt search. Measure precision/recall against ground truth.

2. **Build MVP** (2-4 weeks): SigLIP pipeline + SQLite + CLI + FFmpeg clip extraction. Deliver a working tool Chris can use immediately.

3. **Test with Chris** (1 week): Process 10-20 films from the Object Lessons backlog. Get feedback on detection quality, clip utility, and workflow integration.

4. **Decide organ placement**: If the tool stays bespoke for AMP Lab → ORGAN-II (Poiesis). If it generalizes to any object-across-films query → ORGAN-III (Ergon) as a product.

5. **Build full system** (4-8 weeks): Add Grounding DINO + SAM2 tracking, web UI, cloud burst processing, NLE export.

### Organ Placement Recommendation

**Start in ORGAN-II (Poiesis)**. The first version is a creative production tool for a specific series. If it proves general-purpose (any object, any film corpus, any user), promote to ORGAN-III (Ergon) as a product with its own seed.yaml, ecosystem.yaml, and kerygma profile.

---

## Appendix A: Model Quick Reference

### Recommended primary models

| Role | Model | Why | Fallback |
|------|-------|-----|----------|
| Embedding/sweep | SigLIP ViT-L/16@384 | Best zero-shot accuracy (84.5%), 768-dim, runs on M3 | CLIP ViT-L/14 (76.2%) |
| Fast detection | YOLO-World-L | Open-vocabulary, 52 FPS (A100), Ultralytics ecosystem | YOLOv8 + fine-tuning |
| Accurate detection | Grounding DINO (Swin-T) | 52.5 AP zero-shot, rich text grounding | Florence-2-Large |
| Video tracking | SAM2 (Hiera-L) | Native video mode, memory bank, 44 FPS (A100) | ByteTrack (no masks) |
| Verification (optional) | Qwen2-VL-7B | Temporal reasoning, era context understanding | Florence-2 captioning |

### Models NOT recommended

| Model | Why Not |
|-------|---------|
| Standard YOLOv8/v9/v10 | Closed vocabulary — cannot detect arbitrary objects without retraining |
| SAM (v1) | No video mode — frame-by-frame only |
| Large VLMs (CogVLM2, InternVL2-76B) | Too large for M3, too slow for batch processing |
| Google Video Intelligence / AWS Rekognition | 50-200x more expensive than self-hosted |

## Appendix B: Key References

### Academic
- PyCinemetrics — computational film analysis tool (ScienceDirect, 2024)
- "Recurring Element Detection in Movies" (Springer, 2012)
- "Exploring Computer Vision for Film Analysis" (Univ. of Regensburg, EADH 2021)
- Lev Manovich, Cultural Analytics Lab — computational visual culture studies

### Technical
- Ultralytics YOLO-World documentation
- Meta SAM2 — Segment Anything in Images and Videos
- Google SigLIP — Sigmoid Loss for Language Image Pre-Training
- IDEA Research Grounding DINO — Open-Set Object Detection

### Legal
- 17 USC Section 107 — Fair Use
- Hosseinzadeh v. Klein (2017) — YouTube fair use precedent
- Andy Warhol Foundation v. Goldsmith (2023, SCOTUS) — transformative purpose test
- DMCA Section 1201 — 2024 Copyright Office rulemaking (educator/critic exemptions)
- Tony Zhou, "Postmortem: Every Frame a Painting" — Content ID practical strategies

### Existing Tools
- ShotDeck (shotdeck.com) — 318K hand-tagged film screenshots
- Kinolab (kinolab.org) — DMCA-compliant annotated narrative media clips
- Cinemetrics (cinemetrics.lv) — crowdsourced shot-length data
- PySceneDetect (github.com/Breakthrough/PySceneDetect) — shot boundary detection
- Twelve Labs (twelvelabs.io) — semantic video search API
