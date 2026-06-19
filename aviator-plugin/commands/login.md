---
description: Check Aviator authentication status
---

# Aviator Login

Authentication is handled automatically by Claude Code using OAuth 2.1.

## How It Works

When you use any Aviator tool (like `/aviator runbook`), Claude Code will:

1. Detect that authentication is needed
2. Open your browser to authorize with Aviator
3. Securely store and refresh tokens automatically

**You don't need to manually log in!** Just use the tools and authentication happens automatically.

## Checking Status

To verify your connection to Aviator, try listing available tools:

The MCP server at `https://app.aviator.co/mcp` provides tools for:
- Creating runbooks from your session
- Querying pull requests and merge queue status
- Managing workflows

## Troubleshooting

**If authentication fails:**
- Make sure you have an Aviator account at https://app.aviator.co
- Check that you're allowing the OAuth authorization in the browser
- Try signing out and back into Claude Code to clear cached tokens

**If the browser doesn't open:**
- Check your default browser settings
- The authorization URL will be shown in the terminal - you can copy and open it manually

## Logout

To remove stored credentials, sign out of Claude Code or clear the plugin's cached tokens in Claude Code settings.
