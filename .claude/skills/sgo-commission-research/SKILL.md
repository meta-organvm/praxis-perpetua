---
name: sgo-commission-research
description: Conduct source-backed research for an SGO commission, from FINER question shaping through capability-based provider routing, attended Perplexity Pro handoff or credential-gated API execution, Markdown export ingestion, claim-to-source verification, and durable evidence receipts. Use for current-web research, literature discovery, standards or provider-change research, fact checking, public-claim due diligence, systematic reviews, and any commission whose downstream writing or implementation must consume a verified EvidencePacket.
---

# SGO Commission Research

Treat Studium Generale ORGANVM as the research-workflow authority. Treat Limen
as an invoking runtime, not as the owner of research methodology. Do not add a
research provider to Limen's agent registry.

> Adapted from concepts in Cheng-I Wu, *Academic Research Skills*
> (CC-BY-NC 4.0), https://github.com/Imbad0202/academic-research-skills.
> Re-authored in SGO idiom. No verbatim copy.

## Read first

- `governance/research-backend-profiles.yaml` for live profile states, health
  gates, capabilities, and guardrails.
- `schemas/research-request.schema.json`,
  `schemas/research-outcome.schema.json`, and
  `schemas/research-receipt.schema.json` for the external contracts.
- `schemas/source-verifier-attestation.schema.json` for the machine-readable
  verifier decision required by ingestion.
- `schemas/output-sanitization-attestation.schema.json` for the
  machine-readable export and tracked-output privacy proof.
- `standards/SOP--research-backend-routing.md` for routing and custody rules.
- `standards/SOP--public-private-classification.md` for P/O/C/E preservation.
- `references/provider-routing.md` when selecting or activating a profile.
- The mode-specific reference only when using `socratic` or
  `systematic-review`.

## Modes

| Mode | Output |
|---|---|
| `full` | Research brief, literature matrix, verified EvidencePacket |
| `quick` | Bounded thematic overview plus verified material claims |
| `socratic` | Five-layer dialogue and refined ResearchRequest |
| `lit-review` | Literature review, FINER score, matrix, EvidencePacket |
| `fact-check` | Claim-by-claim support, contradiction, and unknown report |
| `review` | Source and argument audit of an existing draft |
| `systematic-review` | Preregistered PRISMA-style review and risk-of-bias record |

## Outcome contract

Emit exactly one typed outcome:

- `EvidencePacket` when all material claims have resolvable supporting
  citations and the verification gate passes.
- `ManualHandoff` when an attended surface must be operated by the user, most
  notably `pro_research`.
- `BlockedReceipt` when no healthy profile can satisfy the request within its
  privacy, latency, or spend ceiling.

Never silently fall back to a more expensive, less private, or less verifiable
profile.

## Workflow

1. **Validate the commission.**
   - Create a `ResearchRequest`; validate it against the canonical schema.
   - Require an owner repository, report path, receipt path, preservation tier,
     external-transmission authority, and spend ceiling before routing.
   - Use `question-architect` and `methodology-designer` to refine scope and
     apply the FINER gate.

2. **Route by capability.**
   - Read the tracked profile registry at execution time.
   - Filter using each profile's declared outcome type, verification strength,
     preservation tiers, transmission authorities, capabilities, state,
     machine health, execution timeout, and USD cost. Treat `null` cost as
     unknown, never zero.
   - Treat provider catalogs as live external state.
   - Use provider Auto when live metadata is insufficient. Never invent,
     promise, or pin a model identifier.
   - Hash the validated request and observed catalog/profile view for the
     receipt.

3. **Execute or hand off.**
   - For `pro_research`, render a ready-to-submit prompt using
     `templates/perplexity-project-standing-instructions.md` and return a
     `ManualHandoff`. The attended Project or Space is named **Limen
     Research**.
   - Open Perplexity only for the qualifying request. Research mode chooses
     its own models; do not request a model.
   - Defer subscription, authentication, and provider-surface checks to the
     `ManualHandoff`; do not claim they passed during machine routing.
   - Enforce the `pro_research` 3,600-second attended execution timeout.
   - Require a Markdown session export. Do not schedule the run, connect apps,
     send messages, make purchases, or perform external writes.
   - Never use private connected sources. Perplexity profiles accept only
     P/O preservation and `public_only` or `sanitized_only` transmission.
   - API profiles remain impossible to execute until their credential,
     credit, catalog, and spend-policy health checks pass.

4. **Ingest the export.**
   - Place the raw export according to the request's P/O/C/E preservation tier.
     Sensitive raw material belongs in its designated private owner, never in
     a tracked public path.
   - Preserve retrieval dates, URLs, titles, author or publisher, publication
     date, source locator, and negative searches. Retain required metadata
     fields with `null` only when the source does not expose the value.
   - Split synthesis into atomic claims. Mark each as `evidence`,
     `inference`, or `unknown`; mark material claims explicitly.
   - Inspect the exact Markdown export and tracked derivatives, then emit
     `OutputSanitizationAttestation`. Bind the exact export UTF-8 bytes and
     record every required redaction.

5. **Verify sources.**
   - Run `bibliography-specialist`, then `source-verifier`.
   - Resolve every cited URL and verify that the source supports the linked
     claim. Prefer primary sources and name contradictions.
   - Emit the exact `SourceVerifierAttestation` contract from
     `templates/source-verifier-attestation.md`; include every claim/source,
     confirmed metadata, language, and jurisdiction needed by the request.
   - Drop or downgrade unsupported claims. A broken citation, missing
     retrieval date, or lost source record fails the packet.
   - Use `synthesis-agent` only after the graded corpus exists.

6. **Write durable outputs.**
   - Store the report and receipt in the request's owner repository.
   - Keep private prompt bodies, credentials, and sensitive raw exports out of
     tracked receipts.
   - Record observed provider/model only when the surface exposes them.
   - Validate the receipt schema and its sanitization assertions.
   - Run `uv run --with-requirements requirements-validation.txt python3
     scripts/validate-research-backend.py`.

7. **Hand off verified evidence only.**
   - Writing and coding agents consume only accepted `EvidencePacket`
     outcomes.
   - CCE may archive and evaluate packets but does not replace owner-repo
     custody.
   - A rejected packet yields a `BlockedReceipt` or a revised request, not a
     prose claim of completion.

## Roles

| Role | Responsibility |
|---|---|
| `question-architect` | Refine and FINER-score the commission |
| `methodology-designer` | Match method, evidence, and privacy constraints |
| `bibliography-specialist` | Search, log, normalize, and preserve sources |
| `source-verifier` | Verify claim support, source quality, and citations |
| `synthesis-agent` | Build a claim-linked synthesis and surface tensions |
| `socratic-mentor` | Clarify exploratory commissions without answering them |
| `risk-of-bias-assessor` | Apply RoB 2, ROBINS-I, or AMSTAR 2 when required |

## Required templates

- `templates/research-brief.md`
- `templates/literature-matrix.md`
- `templates/preregistration.md`
- `templates/evidence-packet.md`
- `templates/manual-handoff.md`
- `templates/blocked-receipt.md`
- `templates/research-receipt.md`
- `templates/source-verifier-attestation.md`
- `templates/output-sanitization-attestation.md`
- `templates/perplexity-project-standing-instructions.md`

## Terminal predicates

A commission run is accepted only when:

- the request, SourceVerifierAttestation, OutputSanitizationAttestation,
  outcome, and receipt validate against their schemas;
- every material claim resolves to at least one supporting source;
- every source retains required metadata, a retrieval date, and a
  source-manifest entry;
- preservation, transmission, and custody match the request and selected
  profile;
- variable spend does not exceed the request ceiling;
- the report and receipt exist in the owner repository.
