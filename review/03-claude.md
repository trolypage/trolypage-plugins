# Claude MCP connector and plugin bundle

The owner requested both listing types under the same organization. The selected public repository is https://github.com/trolypage/trolypage-plugins. The owner selected Apache-2.0 for the original plugin skills and documentation.

## A. MCP connector

| Field | Draft value |
| --- | --- |
| Name | TrolyPage |
| Description | Use 01-listing-and-copy.md, limited to capabilities actually exposed by the Claude catalog |
| Directory server URL | https://trolypage.com/mcp/claude |
| Transport | Streamable HTTP |
| Authentication | OAuth authorization code with PKCE S256; public DCR client |
| Discovery | https://trolypage.com/.well-known/oauth-authorization-server |
| Scope | mcp:use |
| Publisher | Trolypage; verify the selected organization before submission |
| Contact person | Alex Nguyen |
| Contact email | support.mcp@trolypage.com |
| Support | support@trolypage.com; https://trolypage.com/mcp#errors |
| Website / privacy / terms | See 01-listing-and-copy.md; published Privacy Policy identity corrected and verified October 19, 2026 |
| Countries | All platform-supported countries, subject to provider restrictions |
| Reviewer access | Credentials received privately; workspace access, Claude OAuth and live catalog discovery verified October 19, 2026. Synthetic fixtures and representative execution verified; prior all-tool execution attested by owner. Independent reviewer-environment sign-in remains unverified. Use secure review fields only |

### Directory profile update — October 19, 2026

The owner selected a dedicated directory catalog. The server-side `/mcp/claude` profile has now been deployed, with a 180-tool execution allowlist, English descriptions and complete annotation booleans. OAuth resource validation restricts directory-issued tokens to that endpoint. The full `/mcp/troly` service retains Gen AI. The new directory connection completed OAuth in Claude with the correct reviewer workspace. The portal read 180 tools live (90 read-only, 90 write), with four advisory documentation suggestions and no previous catch-all operation flag. See `evidence/claude-directory-release-20261019.md` for deployment and automated regression scope. The owner confirmed prior all-tool Inspector/Claude execution; this session separately verified representative synthetic workflows.

### Historical findings from the full endpoint (superseded candidate)

- Live discovery now confirms 270 tools, 12 prompts and 12 resources from TrolyPage Reviewer. The portal flags `save-integration-operation`: "Split this catch-all API tool into separate read and write tools." It also reports 275 suggestions, largely missing title/readOnlyHint annotations. Inspect the implementation before choosing a fix; saving an operation configuration and executing an operation are different behaviors. See evidence/claude-live-discovery-2026-10-19.json.
- The catalog includes `generate-social-image`. The connector criteria reviewed for this candidate exclude AI image/video/audio generation. Enforce restrictions in the server or a real OAuth profile, then verify `tools/list`. Removing a tool name from documentation does not restrict access.
- The connector's mandatory policy declarations also prohibit tool descriptions that instruct model behavior or refer to other tools or external instruction sources. Review the live descriptions against that requirement. These historical declarations were unresolved for that superseded full-endpoint draft. The current 180-tool directory connector was submitted with owner-confirmed prior all-tool execution.
- `execute-integration-operation` declares openWorldHint without a clear read/write split. Inspect the HTTP methods configured operations can execute; separate read/write tools or exclude the dispatcher from the Claude catalog as needed. Do not use it to bypass excluded capabilities.
- If a different endpoint/profile is selected, use its verified deployment URL. Do not invent a path in the manifest.
- The historical full-endpoint ledger described 270 unrun tools. Current directory evidence covers a different 180-tool catalog, owner-attested prior execution and separately observed representative workflows.

## B. Plugin bundle

Source: `packages/claude/trolypage-mcp`. Local review archive: `archives/claude-trolypage-mcp-1.0.2-DRAFT.zip`. Claude Directory retrieves the bundle from GitHub rather than using this ZIP as an OpenAI-style submission.

Candidate 1.0.2 contains eight TrolyPage skills, refreshed directory-only tool references, `.claude-plugin/plugin.json` and `.mcp.json` targeting the deployed `/mcp/claude` endpoint. The unsupported Automation skill was removed. The eight skills do not fall back to the full endpoint when a capability is unavailable. The existing submission remains the publication target; do not create a duplicate listing.

Repository: https://github.com/trolypage/trolypage-plugins. Plugin path: `packages/claude/trolypage-mcp`. Branch: `codex/submission-preparation`. Select the correct branch/path and verify the commit in the portal.

The bundle includes the Apache-2.0 LICENSE and NOTICE and declares Apache-2.0 in its manifest. This applies to the distributed skills and documentation, not the application backend.

The bundle was submitted for review on October 19, 2026 after the owner explicitly confirmed the organization and all four displayed legal/policy attestations. The portal confirmed receipt and showed the security-scan stage. Source validated at commit `5a53823`: seven checks passed, with the documented harmless privacyPolicyUrl warning. Nine skills and one MCP server were detected. Data handling declares reads and stores, no skill transmission outside declared connectors, retention longer than 30 days, and intended users under 18 (16–17 with guardian consent, as confirmed by the owner). Automatic publication is off; repository updates use scheduled checks. Submission is not approval or proof of successful tool tests.

The separate MCP connector was submitted successfully on October 19, 2026. The receipt linked to https://claude.ai/directory/manage/trolypage. Its 180-tool catalog, English listing, five categories, three use cases, company/contact details, OAuth DCR and private reviewer instructions were submitted. Mandatory prior all-tool execution was confirmed directly by the owner. This is a separate receipt from the bundle, and neither means approval.

## Sources

- https://claude.com/docs/directory/publish
- https://claude.com/docs/plugins/pre-submission-checklist
- https://claude.com/docs/connectors/building/review-criteria
- https://claude.com/docs/connectors/building/submission

## Latest verified result

Claude accepted bundle 1.0.2 at commit `4ac9cfa`, detected eight skills and one MCP connection, and passed format, directory policy and security scanning. The remaining manifest warning explains that Claude Code ignores privacyPolicyUrl while the directory reads it; the portal says no action is needed. Publish was requested for 1.0.2 and is waiting for an Anthropic reviewer. Nothing is live yet.

The separate connector draft now targets `/mcp/claude`, with English listing, use cases, company, OAuth and data disclosures completed through Compliance. Its self-tested checkbox and seven policy declarations remain unchecked. Five read-only tools succeeded through the actual Claude connector; the remaining tool executions are not proven. See `review/claude-directory-tool-test-ledger.csv`. The original full-catalog ledger remains a separate historical/full-endpoint artifact.
