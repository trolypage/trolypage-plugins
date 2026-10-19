# Claude MCP connector and plugin bundle

The owner requested both listing types under the same organization. The selected public repository is https://github.com/trolypage/trolypage-plugins. The bundle license remains undecided.

## A. MCP connector

| Field | Draft value |
| --- | --- |
| Name | TrolyPage |
| Description | Use 01-listing-and-copy.md, limited to capabilities actually exposed by the Claude catalog |
| Existing server URL | https://trolypage.com/mcp/troly |
| Transport | Streamable HTTP |
| Authentication | OAuth authorization code with PKCE S256; public DCR client |
| Discovery | https://trolypage.com/.well-known/oauth-authorization-server |
| Scope | mcp:use |
| Publisher | Trolypage; verify the selected organization before submission |
| Contact person | Alex Nguyen |
| Contact email | support.mcp@trolypage.com |
| Support | support@trolypage.com; https://trolypage.com/mcp#errors |
| Website / privacy / terms | See 01-listing-and-copy.md; correct the published privacy identity first |
| Countries | All platform-supported countries, subject to provider restrictions |
| Reviewer access | Credentials received privately and workspace access verified; OAuth, fixtures and independent sign-in remain unverified. Use secure review fields only |

### Blockers for the current unified endpoint

- The catalog includes `generate-social-image`. The connector criteria reviewed for this candidate exclude AI image/video/audio generation. Enforce restrictions in the server or a real OAuth profile, then verify `tools/list`. Removing a tool name from documentation does not restrict access.
- `execute-integration-operation` declares openWorldHint without a clear read/write split. Inspect the HTTP methods configured operations can execute; separate read/write tools or exclude the dispatcher from the Claude catalog as needed. Do not use it to bypass excluded capabilities.
- If a different endpoint/profile is selected, use its verified deployment URL. Do not invent a path in the manifest.
- Test every exposed tool through MCP Inspector and a Claude custom connector. All 270 ledger entries remain Not run; the five positive and three negative cases are representative and do not replace catalog-wide verification.

## B. Plugin bundle

Source: `packages/claude/trolypage-mcp`. Local review archive: `archives/claude-trolypage-mcp-1.0.1-DRAFT.zip`. Claude Directory retrieves the bundle from GitHub rather than using this ZIP as an OpenAI-style submission.

The bundle retains nine existing TrolyPage skills, refreshed tool references, `.claude-plugin/plugin.json` and `.mcp.json`. It still connects to the real unified endpoint, with the blockers above. No Claude-specific server filter has been verified.

Repository: https://github.com/trolypage/trolypage-plugins. Plugin path: `packages/claude/trolypage-mcp`. Branch: `codex/submission-preparation`. Select the correct branch/path and verify the commit in the portal.

The owner must choose a license for the skills bundle. No LICENSE or license value has been assigned; this remains a listing blocker. Publishing the application backend is not required by this preparation.

After resolving the blockers, use https://claude.ai/directory/manage to submit the connector and bundle under the same organization, validate the repository and verify how the two listings are paired. Do not attest to tests that have not run.

## Sources

- https://claude.com/docs/directory/publish
- https://claude.com/docs/plugins/pre-submission-checklist
- https://claude.com/docs/connectors/building/review-criteria
- https://claude.com/docs/connectors/building/submission
