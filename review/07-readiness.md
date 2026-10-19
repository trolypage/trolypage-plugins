# Requirements before submission

**REVIEW DRAFT.** Source, archives and copy are prepared. No directory upload or submission has been made. Local validation does not replace a platform scan or review.

## Shared requirements

| Item | Status / next step |
| --- | --- |
| Listing, contact, countries, commerce, logo | Owner decisions recorded; contact person Alex Nguyen |
| OpenAI identity | Verified; Business — Trolypage selectable in the upload dialog |
| Metadata / 5+3 cases / release notes | Included in the English-only OpenAI candidate |
| Mobile icon | Original and derived sizes supplied; review appearance at 32/64 px |
| Endpoint/discovery | Public status and OAuth metadata accessible; full OAuth flow not tested |
| Reviewer account | Received privately; browser access verified for TrolyPage Reviewer, Scale, Owner. Owner completed Cloudflare; independent external-reviewer sign-in remains unverified |
| Demo workspace | No products/orders or test fixtures; only the default support contact. MCP UI shows Full / Direct execution applied, no OAuth apps/API keys and no successful read-only call. Configuration unchanged |
| Authenticated tool tests | All 270 tools and all five positive/three negative cases remain Not run |
| Video | Script prepared; real recording and accessible URL missing |
| Published policy identity | Privacy section 13 and mobile support still name SkyNet Solution; privacy lists 9243 Quail Creek Ln, Boulder, US, while the footer names TROLYPAGE COMPANY LIMITED in Hanoi. Confirm the legal relationship or correct the published text |
| MCP guide | Refers to seven focused servers despite 11 routes; calls analytics fully read-only despite export-report; overstates Hybrid approval coverage. Synchronize production copy |
| Data processing | Owner confirmation needed for processors, actual retention, secondary-use restrictions and security escalation contact |

## Engineering findings for the submitted catalog

1. **OpenAI annotations:** every one of the 270 locally serialized tools lacks at least one explicit boolean among readOnlyHint, destructiveHint and openWorldHint. Fix serialization/attributes using the actual behavior of each tool, then verify production `tools/list`. Adding false values to a document does not fix the server. See annotation-gaps.csv.
2. **Claude image generation:** the unified endpoint exposes `generate-social-image`. Enforce a compatible catalog/profile and retest before submission. Bundled skills do not restrict remote tools.
3. **Claude operation dispatcher:** `execute-integration-operation` declares only openWorldHint and may execute configured HTTP operations. Assess a read/write split and correct annotations, or exclude it. Do not bypass media or financial restrictions through this tool.
4. **Muse read-only access:** discovery advertises `mcp:use`; the inspected read-only filter applies to API-token `mcp:read`. Resolve OAuth read-only behavior before claiming support. Do not replace required OpenAI OAuth with an API key in the submission form.
5. **Schema extraction:** 267/270 input schemas serialized in an isolated container without .env/DB. Inspect the remaining three at runtime. This extraction limit is not proof of a production failure; authenticated wire annotations remain unverified.

The application server has not been changed in this distribution repository. These findings remain a product/engineering backlog to resolve before final submission.

## Platform-specific work

- **OpenAI:** domain challenge, OAuth, scans, reviewer access, video and final attestations remain pending. The draft ZIP can be reviewed locally but is not submission-ready.
- **Claude:** catalog policy, tool tests and reviewer access remain pending. The bundle additionally needs an owner-selected license and portal validation. Public source: https://github.com/trolypage/trolypage-plugins. Do not upload the application backend.
- **Muse:** verify the payment-category definition for external payment. Later technical/review form steps, processing questionnaire, test access, host approvals and terms remain incomplete.

## Next preparation steps

Confirm independent sign-in and OAuth, populate synthetic fixtures and record approval mode for each test round. Full / Direct execution does not mean every write enters a queue. Select the bundle license and demo hosting destination; record real fixture IDs. Resolve findings for the intended catalog, run tests and record a real video. Add its verified URL, rebuild, inspect validation and hashes, and only then finalize an authorized draft upload.
