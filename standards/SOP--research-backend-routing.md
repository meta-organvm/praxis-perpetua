# SOP: Research Backend Routing

- **Version:** 1.0.0
- **Status:** ENACTED
- **Date:** 2026-07-17
- **Owner:** Studium Generale ORGANVM
- **Runtime consumer:** Limen

## Purpose

Route current-external-evidence commissions through a provider-neutral
contract while preserving SGO methodology, source verification, privacy, cost,
and owner-repo custody. A provider is a backend, not an autonomous SGO agent.

This SOP governs `.claude/skills/sgo-commission-research/` and supersedes
provider-specific routing examples in older research-pipeline documents.

## Contracts

- Input: `schemas/research-request.schema.json`.
- Verification:
  `schemas/source-verifier-attestation.schema.json`.
- Sanitization:
  `schemas/output-sanitization-attestation.schema.json`.
- Output: one `EvidencePacket`, `ManualHandoff`, or `BlockedReceipt` validated
  by `schemas/research-outcome.schema.json`.
- Provenance: `schemas/research-receipt.schema.json`.
- Profiles: `governance/research-backend-profiles.yaml`.

The request declares the question, capabilities, freshness and domain
constraints, verification strength, preservation tier, external-transmission
authority, latency ceiling, variable spend ceiling, and durable output
contract. The receipt records hashes rather than private prompt bodies.

The executable semantic predicate is:

```bash
uv run --with-requirements requirements-validation.txt \
  python3 scripts/validate-research-backend.py
```

## Routing algorithm

1. Validate the request and its owner-repo output paths.
2. Read the profile registry and discover reachable capabilities live.
3. Filter profiles using their declared `outcome_type`,
   `verification_strength`, `preservation_tiers`, `external_transmission`,
   capabilities, state, health, execution timeout, and `variable_cost_usd`.
4. Rank remaining profiles by verification fit, preservation/transmission fit,
   projected cost, then latency.
5. Use provider Auto when live metadata is insufficient.
6. Select one profile or return a typed unavailable outcome.

Do not infer capability from a provider or model name. Do not encode model IDs,
fixed provider catalogs, or fixed fallback tables. Do not silently cross a
privacy, latency, or spend boundary.

A `null` profile cost is unknown, not zero: execution remains gated until a
live cost projection fits the request ceiling. `provider_auto` declares
`selected_adapter`; resolve that sentinel to the selected concrete adapter's
typed outcome before emitting a `ResearchOutcome`.

Health has two explicit surfaces. `health.machine` contains predicates the
runtime can evaluate. `health.attended` lists checks deferred to the
`ManualHandoff`; routing must not claim that a subscription, authenticated
session, credit balance, or provider surface is live merely because the
profile is enabled.

## Attended Pro Research path

`pro_research` is initially enabled for qualifying requests under an existing
subscription. It is disabled at startup and activated only on demand.

1. Render the request using the **Limen Research** standing instructions at
   `.claude/skills/sgo-commission-research/templates/perplexity-project-standing-instructions.md`.
2. Emit a `ManualHandoff` naming the prompt reference, Project or Space,
   Markdown ingest destination, and resume predicate.
3. The operator verifies the deferred subscription, authentication, and
   Research-mode checks in the attended session, then submits the prompt.
   Research mode selects its own models; do not choose one.
4. Export the completed Session answer as Markdown.
5. Place the raw export in its preservation-appropriate owner.
6. Normalize it into atomic claims and a source manifest.
7. Verify every material claim and emit the final outcome and receipt.

The attended path may not schedule tasks, connect apps, make purchases, send
messages, publish, access private connected sources, or perform any external
write. Its executable envelope is 3,600 seconds after attended execution
begins. Expiry yields a typed handoff or blocked receipt; it does not authorize
background polling.

## Export normalization and verification

Ingestion must preserve:

- source title, URL, author or publisher, publication date, retrieval date,
  source type, primary-source status, and locator;
- the queries and surfaces searched, including negative searches;
- atomic claim IDs and source IDs;
- explicit evidence, inference, contradiction, and unknown labels.

The Source Verifier resolves each citation and checks whether the source
supports its linked claim. Broken citations, unsupported material claims,
missing retrieval dates, or lost source metadata reject the packet. Writing
and coding agents may consume only an accepted `EvidencePacket`.

The verifier emits the exact `SourceVerifierAttestation` contract before
ingestion can accept a packet. Its claim and source sets must equal the
normalized packet, its grading overwrites provisional provider labels, and
the terminal receipt binds the canonical attestation hash. Language and
jurisdiction constraints are proven through this attestation rather than
trusted from provider prose.

The Source Verifier also records each exact normalized source URL and a
`resolvable` decision. An accepted packet requires `resolvable: true`; runtime
adapters compare the attested URL to the export and do not independently
follow redirects or resolve DNS.

Before ingestion accepts tracked output, bind the exact raw Markdown export,
inspect its normalized tracked derivatives, and emit
`OutputSanitizationAttestation`. Its `export_hash` is the SHA-256 digest of the
exact UTF-8 text consumed, without whitespace normalization. It must match the
request's preservation and transmission boundary, postdate the retrieval
interval, and prove tracked-output safety. The private raw Session export may
echo the submitted question; prompt or credential material in that raw export
requires declared `private-owner://` custody.
The normalized EvidencePacket, tracked report, and receipt must contain no
private prompt body, credentials, or sensitive raw material.
`sanitized_only` requires at least one specific redaction entry.

Every source record includes `author_or_publisher`, `published_at`, and
`locator`; each may be `null` only when the verifier confirms that the source
does not expose that metadata. `freshness.published_after` and
`freshness.published_before` constrain publication dates independently of
retrieval time.

## API activation

`api_search` and `api_synthesis` begin dormant. Each remains non-executable
until all of its registry health checks pass, including:

- credential presence checked without revealing the value;
- live credit and automatic-top-up state;
- refreshed live pricing and catalog;
- explicit per-request spend ceiling;
- projected cost within that ceiling.

Search API results are structured discovery records, not generated synthesis.
Generated cited prose uses a separate synthesis-capable API surface. Adapters
must keep those contracts distinct.

## Privacy and custody

Preservation follows `standards/SOP--public-private-classification.md`:

| Symbol | `preservation_tier` | Meaning |
|---|---|---|
| P | `public_facing` | Ready for public distribution |
| O | `operational_internal` | Continuity material without private IP |
| C | `client_private` | Per-client confidential material |
| E | `essence_private` | Cross-client or distinguishing private IP |

`external_transmission` is a separate authority: `public_only` permits only
already-public inputs, `sanitized_only` permits only a minimized and inspected
derivative, and `forbidden` permits no provider transmission.

- Pro and API profiles accept only P/O preservation tiers and
  `public_only`/`sanitized_only`. They never access private connected sources.
  C/E requests require `forbidden` transmission and therefore return a typed
  unavailable outcome for these profiles.
- Safe reports and sanitized receipts live in the requesting owner repository.
- Sensitive raw exports live only in their designated private owner.
- Tracked receipts contain no credentials, private prompt bodies, or sensitive
  raw material.
- CCE may archive and evaluate packets; it does not replace owner-repo custody.
- Praxis Perpetua owns the aggregate workflow and pilot evaluation, not copies
  of every owner report.

## Receipt gate

A terminal receipt must include:

- request and observed catalog/profile hashes;
- selected profile and observed provider/model when exposed;
- retrieval interval and source-manifest hash;
- usage, variable cost, and attended operator-handling time;
- verification counts and primary-source ratio;
- durable report and receipt references;
- preservation tier, external-transmission authority, custody, and
  sanitization assertions.

Compute `sha256:` hashes over UTF-8 JSON with keys sorted and separators
`,`/`:` without added whitespace. Sort source records by `source_id` before
hashing the source manifest; hash the exact validated request and observed
catalog/profile snapshot.

If the profile is unavailable before research begins, emit `ManualHandoff` or
`BlockedReceipt`. If verification fails after research, preserve the rejected
receipt and do not represent the report as accepted evidence.

## Executable validation

`uv run --with-requirements requirements-validation.txt python3
scripts/validate-research-backend.py` validates:

- all five JSON Schemas, both ingestion-attestation fixtures, and the four
  pilot requests;
- the exact four generated pilot ManualHandoffs, prompts, and preliminary
  receipts, including request/catalog hashes, zero-spend state,
  `manual_pending`, prompt-file linkage, portable paths, and credential
  sanitization;
- profile state, structured machine/attended health, manual-handoff metadata,
  timeout, preservation, transmission, and private-source denial;
- safe relative owner paths, every declared freshness/domain/source/language/
  jurisdiction constraint, ordered retrieval timestamps, request
  catalog/profile-snapshot and source-manifest hashes, cost ceilings, and
  consistent custody;
- recursive rejection of fixed model fields, catalog snapshots, provider
  order tables, and silent fallbacks;
- accepted-packet claim/source links, bounded verification counts, and
  primary-source ratio arithmetic;
- final serialized-receipt rejection for request-question leakage or
  credential-shaped values, in addition to the schema sanitization assertions;
- pilot-only novelty, handling-time, and zero-variable-spend gates;
- positive outcomes plus committed negative fixtures for each semantic
  boundary.

CI installs `requirements-validation.txt` and runs this predicate. A prose
closeout cannot substitute for it.

## Pilot gate

The initial four-run pilot is registered at
`commissions/2026-07-17-perplexity-research-pilot/`. It uses `pro_research`
only and permits zero variable Perplexity spend.

The pilot passes only when:

- at least three packets are accepted;
- every material claim has a resolvable citation;
- at least 80 percent of citations are primary sources;
- every run has a durable owner-repo report and receipt;
- each accepted packet contributes at least one novel actionable finding;
- operator handling is no more than 20 minutes per run;
- variable Perplexity spend is zero.

A passing pilot keeps `pro_research` enabled and merely permits a later API
activation decision. A failing pilot disables the profile and forbids API
spending until a new value case is accepted.

Novel actionable findings are a pilot predicate, not a global
`EvidencePacket` schema requirement. The semantic validator enforces the
requirement only for pilot fixtures and receipts.

## Observed-current provider facts

As checked on 2026-07-17:

- Research mode selects its own model combination and Pro has extended access.
- Session answers support PDF, Markdown, and DOCX export.
- Search API returns raw structured results; cited generated prose is a
  separate Agent API surface.
- Published Search API pricing is USD 5 per 1,000 requests.
- Ask and standard searches do not consume Computer credits; Computer does.
  Auto-refill is off by default but must be verified.

These are dated observations, not timeless constants. Refresh them before any
API or Computer activation.

Sources:

- https://www.perplexity.ai/help-center/en/articles/10738684-what-is-research-mode
- https://www.perplexity.ai/help-center/en/articles/10354769-what-is-a-thread
- https://www.perplexity.ai/help-center/en/articles/13838041-how-credits-work-on-perplexity
- https://docs.perplexity.ai/docs/search/quickstart
- https://docs.perplexity.ai/docs/agent-api/quickstart
- https://docs.perplexity.ai/docs/getting-started/pricing

## Prohibited activation effects

This SOP introduces no login item, scheduled task, background daemon,
connector, automatic refill, unattended outward action, or new agent-registry
entry.
