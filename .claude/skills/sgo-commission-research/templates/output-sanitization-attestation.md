# OutputSanitizationAttestation

Emit this machine-readable record after binding the exact raw Markdown export
consumed by ingestion and inspecting its normalized tracked derivatives. Limen
consumes this exact contract through `--sanitization-file`; Studium owns it.

```yaml
schema_version: "1.0"
request_id:
attested_at:
attestor:
export_hash:
preservation_tier:
external_transmission:
tracked_output_safe: true
contains_credentials: false
contains_private_prompt_body: false
contains_sensitive_raw_material: false
redactions_applied: []
```

## Rules

- Compute `export_hash` as `sha256:` plus the SHA-256 digest of the exact raw
  Markdown UTF-8 bytes passed to ingestion. Do not normalize whitespace.
- Match `request_id`, `preservation_tier`, and `external_transmission` to the
  canonical ResearchRequest.
- Set `attested_at` at or after the research retrieval interval.
- Set `tracked_output_safe: true` only after inspecting the normalized
  EvidencePacket, tracked report, and receipt.
- `contains_credentials`, `contains_private_prompt_body`, and
  `contains_sensitive_raw_material` describe those tracked derivatives. They
  remain `false` for an accepted packet.
- The private raw Session export may echo the submitted question. That alone
  does not fail sanitization; when it contains prompt or credential material,
  preserve it only at a declared `private-owner://` `raw_export_ref`. Prompt or
  credential material surviving into any tracked derivative does fail.
- A `sanitized_only` request requires at least one specific nonempty
  `redactions_applied` entry. Other transmission modes may use an empty list.
- Use exactly the fields declared by
  `schemas/output-sanitization-attestation.schema.json`.
