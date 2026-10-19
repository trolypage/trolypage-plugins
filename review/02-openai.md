# OpenAI submission preparation

## Package

`archives/openai-trolypage-mcp-1.0.1-DRAFT.zip` is a review candidate, not a submission-ready release. It contains one plugin at the archive root: `plugin.json`, `mcp.json`, `skills/`, `assets/` and README.

Public metadata is in `extensions.com.openai.interface`; the five positive and three negative cases are in `extensions.com.openai.review.test_cases`. Commerce is declared as true. `countries=[]` represents the owner's choice of all platform-permitted countries. Listing and review text are in English; no optional localized overrides are included. The package excludes private app bindings, `.app.json`, hooks, tokens and passwords.

## Steps after the review draft is complete

1. Resolve the readiness findings, populate the existing demo account and run the tests. Record and review a real demo, then add its verified URL to the manifest.
2. Rebuild and inspect `validation-report.json` and the ZIP hash. Open https://platform.openai.com/plugins under TroLyPage and select `Business — Trolypage`.
3. Upload the ZIP to create a draft. Uploading is separate from submitting for review and receiving approval.
4. Verify imported metadata, countries, commerce disclosure, test cases and release notes. Complete the exact domain challenge supplied by the portal. Select OAuth authentication, use discovery/DCR and scope `mcp:use`, then scan the tools. Keep standard transport/URL configuration in mcp.json; do not add client secrets or unsupported authentication overrides.
5. Enter reviewer credentials only in the dashboard's secure review fields. Exclude them from the ZIP, Git and listing. Repeat the tests against the exact saved draft.
6. The authorized owner must read and confirm policy attestations before submitting for review. Publishing is a separate step after approval.

## Verified and pending

On October 19, 2026, the organization showed Verified status and the upload dialog offered Business — Trolypage. Developer identity verification and MCP domain verification are separate. The draft domain challenge and scans have not been completed.

## Sources

- https://developers.openai.com/plugins/deploy/submission
- https://developers.openai.com/plugins/build/plugins
- https://developers.openai.com/plugins/deploy/submission-errors
