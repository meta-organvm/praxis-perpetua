# SourceVerifierAttestation

Emit this machine-readable record after resolving citations and grading every
claim and source. Limen consumes this exact contract through
`--verification-file`; it is owned here by Studium.

```yaml
schema_version: "1.0"
request_id:
verified_at:
verifier:
verdict: accepted
private_connected_sources_used: false
claims:
  - claim_id:
    verification_status:
    source_ids: []
sources:
  - source_id:
    url:
    resolvable: true
    source_type:
    primary_source:
    quality_tier:
    metadata_confirmed: true
    language:
    jurisdictions: []
```

## Rules

- Use exactly the fields declared by
  `schemas/source-verifier-attestation.schema.json`.
- Include every normalized claim and source exactly once. Claim `source_ids`
  must match the EvidencePacket edges, and each attested `url` must exactly
  match its normalized source record.
- Set `resolvable: true` only after the Source Verifier resolves the citation.
  A broken or unresolved citation cannot enter an accepted packet. Runtime
  adapters trust this owner attestation and must not perform independent
  redirect or DNS fetching.
- Set `metadata_confirmed: true` only after checking the source title, URL,
  author or publisher, publication date, retrieval date, and locator.
- Record `language` and `jurisdictions` whenever the request constrains them.
- `private_connected_sources_used` is always `false`.
- An accepted material claim uses `supported`; do not upgrade a partial,
  contradicted, unsupported, or unknown claim.
- The terminal receipt records the attestation's canonical hash in
  `verification.verifier`.
