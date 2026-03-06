# Stakeholder Portal Memory

## Architecture
- Next.js 15 + Tailwind 4 + Postgres (Neon free tier) + pgvector
- Embeddings: HuggingFace `all-MiniLM-L6-v2` (384 dims, free via Inference API)
- Neon project: `small-fog-61557376`, DB: `neondb`, branch: `main`
- Connection string in `.env.local` and Vercel production/development envs
- HF token from `~/.cache/huggingface/token` (user `ajp41890`)

## Vector Pipeline
- Ingestion: `src/lib/ingestion/ingest-worker.ts` — reads local workspace, chunks with LangChain, embeds via HF API, writes to Neon
- Query-time: `src/lib/hybrid-retrieval.ts` Strategy 4 — embeds query via same HF API, cosine similarity search
- Both functions detect HF vs OpenAI format by URL pattern (`huggingface.co` or `hf-inference`)
- Ingestion is idempotent (upsert on chunk ID)
- ~27K+ chunks across 10+ repos as of 2026-03-06 (ingestion ongoing)

## Key Patterns
- `.env.local` is gitignored — contains real credentials (Neon URL, HF token)
- Vercel env vars set for production + development (preview needs manual branch specification)
- Pre-existing lint warnings in `scripts/validate-env.ts` and `tests/connector-types.test.ts` (not from our changes)
- `npm run build` runs `prebuild` which does `--allow-stale-manifest --skip-vector` — safe for CI

## Gotchas
- Don't pipe long-running ingestion through `head` — kills the process
- HF Inference API returns sporadic 500s — non-fatal, pipeline skips and continues
- Multiple ingestion processes can run simultaneously — wasteful but not destructive (upsert)
- Vercel `env add` for preview requires `--value` flag inline, not piped stdin
- Neon free tier SSL warning about `sslmode=require` vs `verify-full` — cosmetic only

## SOPs
- SOP-001 written to `organvm-corpvs-testamentvm/sops/SOP-001-vector-pipeline-activation.md`
- Generalizable pattern for any ORGANVM project needing semantic search
