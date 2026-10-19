# Claude MCP connector and plugin bundle

The owner requested both listing types under the same organization. The selected public repository is https://github.com/trolypage/trolypage-plugins. The owner selected Apache-2.0 for the original plugin skills and documentation.

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
| Website / privacy / terms | See 01-listing-and-copy.md; published Privacy Policy identity corrected and verified October 19, 2026 |
| Countries | All platform-supported countries, subject to provider restrictions |
| Reviewer access | Credentials received privately; workspace access, Claude OAuth and live catalog discovery verified October 19, 2026. Fixtures, tool-execution tests and independent sign-in remain unverified. Use secure review fields only |

### Blockers for the current unified endpoint

- Live discovery now confirms 270 tools, 12 prompts and 12 resources from TrolyPage Reviewer. The portal flags `save-integration-operation`: "Split this catch-all API tool into separate read and write tools." It also reports 275 suggestions, largely missing title/readOnlyHint annotations. Inspect the implementation before choosing a fix; saving an operation configuration and executing an operation are different behaviors. See evidence/claude-live-discovery-2026-10-19.json.
- The catalog includes `generate-social-image`. The connector criteria reviewed for this candidate exclude AI image/video/audio generation. Enforce restrictions in the server or a real OAuth profile, then verify `tools/list`. Removing a tool name from documentation does not restrict access.
- The connector's mandatory policy declarations also prohibit tool descriptions that instruct model behavior or refer to other tools or external instruction sources. Review the live descriptions against that requirement. No connector policy checkbox or all-tools-self-tested declaration has been accepted.
- `execute-integration-operation` declares openWorldHint without a clear read/write split. Inspect the HTTP methods configured operations can execute; separate read/write tools or exclude the dispatcher from the Claude catalog as needed. Do not use it to bypass excluded capabilities.
- If a different endpoint/profile is selected, use its verified deployment URL. Do not invent a path in the manifest.
- Test every exposed tool through MCP Inspector and a Claude custom connector. All 270 ledger entries remain Not run; the five positive and three negative cases are representative and do not replace catalog-wide verification.

## B. Plugin bundle

Source: `packages/claude/trolypage-mcp`. Local review archive: `archives/claude-trolypage-mcp-1.0.1-DRAFT.zip`. Claude Directory retrieves the bundle from GitHub rather than using this ZIP as an OpenAI-style submission.

The bundle retains nine existing TrolyPage skills, refreshed tool references, `.claude-plugin/plugin.json` and `.mcp.json`. It still connects to the real unified endpoint, with the blockers above. No Claude-specific server filter has been verified.

Repository: https://github.com/trolypage/trolypage-plugins. Plugin path: `packages/claude/trolypage-mcp`. Branch: `codex/submission-preparation`. Select the correct branch/path and verify the commit in the portal.

The bundle includes the Apache-2.0 LICENSE and NOTICE and declares Apache-2.0 in its manifest. This applies to the distributed skills and documentation, not the application backend.

The bundle was submitted for review on October 19, 2026 after the owner explicitly confirmed the organization and all four displayed legal/policy attestations. The portal confirmed receipt and showed the security-scan stage. Source validated at commit `5a53823`: seven checks passed, with the documented harmless privacyPolicyUrl warning. Nine skills and one MCP server were detected. Data handling declares reads and stores, no skill transmission outside declared connectors, retention longer than 30 days, and intended users under 18 (16–17 with guardian consent, as confirmed by the owner). Automatic publication is off; repository updates use scheduled checks. Submission is not approval or proof of successful tool tests.

The separate MCP connector has a browser draft populated through the compliance step: English listing, five relevant categories, three use cases, company/contact details, OAuth DCR, data-handling explanations and honest reviewer setup instructions. OAuth and live discovery succeeded for the correct reviewer workspace. Final connector submission remains blocked by unmet policy declarations and incomplete tool tests. The browser draft must be preserved; it is not a submitted directory record. Do not treat bundle receipt as connector approval or attest to unrun tests.

## Sources

- https://claude.com/docs/directory/publish
- https://claude.com/docs/plugins/pre-submission-checklist
- https://claude.com/docs/connectors/building/review-criteria
- https://claude.com/docs/connectors/building/submission
