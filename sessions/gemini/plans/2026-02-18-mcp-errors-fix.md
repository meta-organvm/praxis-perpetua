# Plan: Fix MCP Server Connection Errors

This plan addresses the "Connection closed" errors for `mcp_toolbox`, `autopm-agents`, and `autopm-pm`.

## Analysis of Errors
- **mcp_toolbox**: The `toolbox` binary is likely failing to execute.
- **autopm-agents / autopm-pm**: These Node.js servers are likely crashing due to missing dependencies, incompatible Node.js version, or runtime errors in the ES modules.

## Proposed Steps

### 1. Diagnose `mcp_toolbox`
- Check execution permissions for the `toolbox` file.
- Attempt to run the command manually: `~/.gemini/extensions/mcp-toolbox/toolbox --stdio`.
- Capture any error messages (e.g., missing libraries, architecture mismatch).

### 2. Diagnose `autopm-*`
- Verify the Node.js version meets the requirement (`>=20.0.0`).
- Check if `node_modules` is correctly installed in `~/.gemini/extensions/gemini-autopm`.
- Attempt to run the servers manually:
  - `node ~/.gemini/extensions/gemini-autopm/dist/servers/agents-server.js`
  - `node ~/.gemini/extensions/gemini-autopm/dist/servers/pm-server.js`
- Capture stack traces or error messages.

### 3. Implementation of Fixes
- **If permissions issue**: Fix with `chmod +x`.
- **If missing dependencies**: Run `npm install`.
- **If Node.js version issue**: Advise the user or attempt to use a compatible version if available via `mise` or `nvm`.
- **If `toolbox` architecture mismatch**: Check if a compatible binary is available.

## Verification
- Restart the Gemini CLI or trigger a re-discovery of MCP servers.
- Verify the servers are listed as CONNECTED.