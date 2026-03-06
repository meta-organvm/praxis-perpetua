# Fix Gemini CLI MCP Server / Tooling Errors

## Context

Gemini CLI encounters three MCP errors in the `organvm-pactvm` project:

1. **Blender MCP**: "Error during discovery for MCP server 'blender': fetch failed"
2. **Sequential Thinking MCP**: `sequentialthinking` "Tool execution denied by policy"
3. **Filesystem MCP**: `read_multiple_files` "Tool execution denied by policy"

Built-in `ReadFile` works fine - only MCP server extension tools are blocked.

---

## Root Causes

### Blender: "fetch failed"
- `~/.gemini/extensions/blender-mcp/gemini-extension.json` connects to `http://localhost:9876`
- Blender isn't running, so HTTP fetch fails at discovery

### Sequential Thinking & Filesystem: "denied by policy"
- Both come from the `gemini-flow` extension
- `~/.gemini/policies/auto-saved.toml` only has rules for `run_shell_command`
- No policy rules exist for MCP tools (`sequentialthinking`, `read_multiple_files`, etc.)
- `tools.autoAccept: true` in settings.json appears to apply only to built-in tools

### Bonus: Conflicting Filesystem paths across 3 config files
- `gemini-extension.json`: `/Users/4jp` (correct)
- `.mcp-config.json`: `/workspaces` (wrong - container path)
- `.mcp.json`: `/Users/chrisdukes/Desktop` (wrong - upstream author's path)

---

## Fixes

### 1. Disable Blender MCP by Default

**File**: `~/.gemini/extensions/extension-enablement.json`

Change blender-mcp override from `/Users/4jp/*` to `!/Users/4jp/*`:
```json
"blender-mcp": {
  "overrides": ["!/Users/4jp/*"]
}
```

### 2. Add MCP Tool Policy Rules

**File**: `~/.gemini/policies/auto-saved.toml`

Append rules for all MCP tools from gemini-flow that should be auto-allowed:

```toml
# Sequential Thinking
[[rule]]
toolName = "sequentialthinking"
decision = "allow"
priority = 100

# Filesystem tools
[[rule]]
toolName = "read_file"
decision = "allow"
priority = 100

[[rule]]
toolName = "read_multiple_files"
decision = "allow"
priority = 100

[[rule]]
toolName = "write_file"
decision = "allow"
priority = 100

[[rule]]
toolName = "edit_file"
decision = "allow"
priority = 100

[[rule]]
toolName = "list_directory"
decision = "allow"
priority = 100

[[rule]]
toolName = "directory_tree"
decision = "allow"
priority = 100

[[rule]]
toolName = "search_files"
decision = "allow"
priority = 100

[[rule]]
toolName = "create_directory"
decision = "allow"
priority = 100

[[rule]]
toolName = "move_file"
decision = "allow"
priority = 100

[[rule]]
toolName = "get_file_info"
decision = "allow"
priority = 100

[[rule]]
toolName = "list_allowed_directories"
decision = "allow"
priority = 100
```

### 3. Fix Filesystem Paths in Secondary Configs

**File**: `~/.gemini/extensions/gemini-flow/.mcp-config.json`
- Change Filesystem args from `"/workspaces"` to `"/Users/4jp"`

**File**: `~/.gemini/extensions/gemini-flow/.mcp.json`
- Change Filesystem args from `"/Users/chrisdukes/Desktop"` to `"/Users/4jp"`

### 4. Remove Redis and Supabase MCP Servers

**File**: `~/.gemini/extensions/gemini-flow/gemini-extension.json`

Remove the `"Redis"` and `"Supabase"` entries from the `mcpServers` object. Both require external services (Redis on localhost:6379, Supabase access token) and add unnecessary startup overhead.

Also remove from `.mcp-config.json` and `.mcp.json` for consistency.

**Servers kept**: Sequential Thinking, Filesystem, GitHub, Git Tools, Puppeteer, Mem0 Memory, Omnisearch (7 servers).

---

## Files to Modify

| # | File | Change |
|---|------|--------|
| 1 | `~/.gemini/extensions/extension-enablement.json` | Disable blender-mcp by default |
| 2 | `~/.gemini/policies/auto-saved.toml` | Add allow rules for MCP tools |
| 3 | `~/.gemini/extensions/gemini-flow/.mcp-config.json` | Fix Filesystem path, remove Redis/Supabase |
| 4 | `~/.gemini/extensions/gemini-flow/.mcp.json` | Fix Filesystem path, remove Redis/Supabase |
| 5 | `~/.gemini/extensions/gemini-flow/gemini-extension.json` | Remove Redis/Supabase servers |

---

## Verification

1. Run `gemini` in the organvm-pactvm directory
2. Confirm no "fetch failed" for blender
3. Ask Gemini to use `sequentialthinking` - should succeed
4. Ask Gemini to `read_multiple_files` - should succeed
5. If still denied: Gemini CLI may prefix tool names with server name (e.g. `Sequential Thinking_sequentialthinking`). If so, adjust TOML rules or approve once interactively and let Gemini auto-save the rule
6. Fallback: try `gemini --sandbox=none` to bypass policy restrictions entirely
