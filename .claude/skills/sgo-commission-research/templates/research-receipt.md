# ResearchReceipt

```yaml
schema_version: "1.0"
receipt_id:
request_id:
request_hash:
catalog_hash:
selected_profile:
observed_provider:
observed_model:
retrieval_started_at:
retrieval_finished_at:
source_manifest_hash:
outcome_type:
usage:
  currency: USD
  variable_cost:
  requests:
  input_tokens:
  output_tokens:
  computer_credits:
  operator_handling_seconds:
  usage_source:
verification:
  status:
  verified_at:
  verifier:
  material_claims:
  supported_material_claims:
  resolvable_citations:
  total_citations:
  primary_source_citations:
  primary_source_ratio:
  rejection_reasons: []
durable_output:
  owner_repo:
  report_path:
  receipt_path:
  raw_export_ref:
privacy:
  preservation_tier:
  external_transmission:
  tracked_output_safe:
  raw_export_disposition:
  private_connected_sources_used: false
  redactions_applied: []
sanitization:
  contains_credentials: false
  contains_private_prompt_body: false
  contains_sensitive_raw_material: false
```

## Usage

## Verification

## Custody

## Caveats

Use `operator_handling_seconds` to prove the pilot's per-run handling ceiling.
Set unavailable provider usage counters to `null`; never estimate them.
