---
description: Create an Aviator Runbook from the current Claude session
---

# Create Aviator Runbook

Create a Runbook in Aviator based on the current Claude Code session context.

## Arguments

$ARGUMENTS - Optional additional context or instructions for the runbook

## Steps

### Step 1: Detect Repository

Determine the current repository:
```bash
git remote get-url origin
```

Extract the repository name in `owner/repo` format from the git URL.

### Step 2: Generate Handoff Document

Based on the conversation history in this session, create a comprehensive handoff document that summarizes:

1. **User's Goal**: What the user was trying to accomplish
2. **Exploration & Findings**: What was explored, discovered, or researched during the session
3. **Key Technical Decisions**: Important decisions made about approach, architecture, or implementation
4. **Files/Modules Involved**: List the key files, directories, or modules that are relevant
5. **Constraints & Considerations**: Any constraints, requirements, or edge cases identified
6. **Recommended Approach**: If a solution approach was identified, summarize it clearly

If the user provided additional context via $ARGUMENTS, incorporate that into the handoff document.

Format this as a clear, actionable prompt that can be used to generate a runbook.

### Step 3: Create Runbook

Use the `createRunbook` MCP tool from the Aviator server with:
- `repo_name`: The repository in `owner/repo` format
- `handoff_document`: The generated handoff document

The tool will return the runbook URL.

### Step 4: Return Link

Provide the user with:
- The Runbook URL from the tool response
- A brief summary of what was included in the handoff

## Error Handling

- If authentication is required, Claude Code will automatically open a browser for OAuth login
- If the repository is not found in Aviator, suggest connecting it at https://app.aviator.co/github/connect
- If the API returns an error about credits, inform the user they may need to add runbook credits
