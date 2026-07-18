# ManualHandoff

```yaml
schema_version: "1.0"
outcome_type: ManualHandoff
request_id:
selected_profile: pro_research
preservation_tier:
external_transmission:
status: ready
project_name: Limen Research
launch_url: https://www.perplexity.ai/
prompt_ref:
standing_instructions_ref:
required_export_format: markdown
execution_timeout_seconds: 3600
ingest_destination:
operator_actions:
  - Open the attended Limen Research Project or Space.
  - Select Research mode and submit the rendered prompt.
  - Export the completed Session answer as Markdown.
  - Place the export at the declared ingest destination.
resume_predicate:
```

## Operator action

Open the attended Project or Space, select Research mode, submit the rendered
prompt, export the completed Session answer as Markdown, and place it at the
ingest destination. Do not schedule, share publicly, connect apps, purchase
credits, use private connected sources, or perform outward actions. Complete
the attended execution within `execution_timeout_seconds`.

## Resume predicate

Copy that predicate into `resume_predicate`: the Markdown export exists at the
declared preservation-appropriate destination.
