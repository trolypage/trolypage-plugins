# Source register — checked 2026-10-19

## SEO and discovery review added

- Public Features EN/VI, robots and sitemap metadata → evidence/features-seo.json. These were read with unauthenticated HTTP after browser navigation timed out; no performance or visual score is inferred.
- https://trolypage.com/features
- https://trolypage.com/vi/tinh-nang
- https://developers.openai.com/plugins/guides/optimize-metadata
- https://developers.google.com/search/docs/appearance/title-link
- https://developers.google.com/search/docs/appearance/snippet
- Contact person Alex Nguyen confirmed directly by the owner; verified business publisher remains Trolypage.

## Platform documentation

- OpenAI upload/review/publication: https://developers.openai.com/plugins/deploy/submission
- OpenAI package/auth format: https://developers.openai.com/plugins/build/plugins
- OpenAI validation errors: https://developers.openai.com/plugins/deploy/submission-errors
- Claude submission types/ownership: https://claude.com/docs/directory/publish
- Claude bundle checks/license: https://claude.com/docs/plugins/pre-submission-checklist
- Claude tool/policy criteria: https://claude.com/docs/connectors/building/review-criteria
- Claude connector workflow: https://claude.com/docs/connectors/building/submission
- Muse connector requirements: https://platform.muse.ai/docs

## TrolyPage evidence

Public pages were read in the user's logged-in Edge browser without transmitting forms. Source paths refer to the separate application checkout and are not copied as backend code into either plugin archive.

- https://trolypage.com/mcp → evidence/live-guide.txt
- https://trolypage.com/mcp/status → evidence/live-status.json
- https://trolypage.com/.well-known/oauth-authorization-server → evidence/live-oauth.json
- https://trolypage.com/privacy-policy → evidence/live-privacy.txt
- https://trolypage.com/terms-of-service → evidence/live-terms.txt
- https://trolypage.com/mobile/support → evidence/live-support.txt
- app/Mcp/Servers/*::TOOLS; Tool::toArray() → evidence/local-tool-catalog.json (270 tools, 3 isolated schema failures; no handle() calls)
- routes/ai.php; McpOAuthMetadataController.php; EnsureMcpWorkspaceAdmin.php; McpCredentialPermissions.php; McpPolicy.php; config/mcp.php; config/data_deletion.php
- trolypage-mobile/app.json selects assets/brand/app-icon.png; copied to assets with SHA-256 recorded in owner-decisions.json

Production public readiness is a self-report; isolated local schema extraction is not a security audit or an authenticated production test. No review test has been marked passed in this preparation.
