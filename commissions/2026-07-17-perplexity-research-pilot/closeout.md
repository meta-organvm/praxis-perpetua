# Closeout

## Per-run predicate

A run is accepted only when:

- every material claim has a resolvable supporting citation;
- all cited sources retain retrieval dates and source metadata;
- the report and receipt exist in the declared owner repository;
- the request, SourceVerifierAttestation, OutputSanitizationAttestation,
  outcome, and receipt pass `uv run --with-requirements
  requirements-validation.txt python3 scripts/validate-research-backend.py`;
- at least one novel actionable finding is recorded;
- operator handling is no more than 20 minutes;
- variable Perplexity spend is USD 0.

Reject a run with broken citations, unsupported material claims, missing
retrieval dates, lost source metadata, incompatible preservation or
transmission, invalid custody, or excess handling/spend.

## Aggregate predicate

The pilot passes only when:

- at least three of four packets are accepted;
- 100 percent of material claims in accepted packets have resolvable
  citations;
- at least 80 percent of all accepted-packet citations are primary sources;
- all four runs have durable owner-repo reports and receipts;
- each accepted packet contains at least one novel actionable finding;
- every run stays within the 20-minute operator-handling ceiling;
- total variable Perplexity spend is USD 0.

## Terminal effects

- **Pass:** keep `pro_research` enabled. API activation remains a separate
  future decision requiring credentials, credits, refreshed pricing, and an
  accepted spend case.
- **Fail:** disable `pro_research` and forbid API spending until a new value
  case is accepted.

Record the aggregate evaluation in this directory and link every owner receipt.
Do not recite residual work after terminal classification; owner-route it
before closing.
