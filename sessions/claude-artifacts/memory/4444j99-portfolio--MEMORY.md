# Portfolio Project Memory

## Workflow Preferences
- Always push branches to origin immediately — user does not want local-only branches
- Merge feature branches into main and push when done — user wants one branch, not lingering feature branches
- Don't ask about PRs unless the user requests one — just merge and push

## RenderCV v2.x Path Resolution
- `--pdf-path`, `-md`, `-html`, `-png`, `-typ` flags resolve paths **relative to the YAML file's parent directory**, not the working directory
- If YAML is at `resume/foo.yaml` and you pass `--pdf-path resume/output/foo.pdf`, the actual output lands at `resume/resume/output/foo.pdf` (doubled prefix)
- Fix: use paths relative to the YAML's parent dir, e.g. `--pdf-path output/foo.pdf`
- The old `--output-folder-name` flag was removed in v2.x
