# Requirements before submission

**REVIEW CANDIDATE.** Source, archives and copy are prepared. The Claude bundle was submitted for review. An OpenAI draft has been uploaded. Muse intake, integration credentials and business verification are complete. No platform approval has been received. Local validation does not replace a platform scan or review.

**Directory profile update, October 19:** `/mcp/claude` is deployed with a 180-tool allowlist enforced at discovery and execution, English descriptions and complete annotation serialization. The full endpoint retains Gen AI. Claude candidate 1.0.2 contains eight matching skills. OAuth for the new directory connection succeeded with TrolyPage Reviewer. Backend MCP regressions passed 248 tests, followed by seven targeted tests after the final fix; local packaging passed 68 checks. Historical full-endpoint findings below do not describe a fresh directory scan. All-tool authenticated business testing, a demo and platform-specific outstanding requirements remain pending. See `evidence/claude-directory-release-20261019.md`.

## Shared requirements

| Item | Status / next step |
| --- | --- |
| Listing, contact, countries, commerce, logo | Owner decisions recorded; contact person Alex Nguyen |
| OpenAI identity / domain | Business — Trolypage verified; MCP domain challenge now verified in the saved draft |
| Metadata / 5+3 cases / release notes | Imported into the English-only OpenAI draft; all nine skill checks passed |
| Mobile icon | Original and derived sizes supplied; review appearance at 32/64 px |
| Endpoint/discovery | Claude directory OAuth and 180-tool live discovery verified; four advisory documentation suggestions remain. OpenAI OAuth remains unverified |
| Reviewer account | Received privately; browser access verified for TrolyPage Reviewer, Scale, Owner. Owner completed Cloudflare; independent external-reviewer sign-in remains unverified |
| Demo workspace | Three agents, no connected channels/senders, no products and no matching Review Customer A. Five read-only calls succeeded through Claude. Full / Direct execution policy unchanged; populated review workflows remain pending |
| Authenticated tool tests | Five directory read-only smoke calls passed; 175 directory tools and populated positive/negative business cases remain unrun. Separate directory ledger provided |
| Video | Script prepared; real recording and accessible URL missing |
| Published policy identity | Owner confirmed TROLYPAGE COMPANY LIMITED, Hanoi. Privacy introduction and section 13 corrected on production and the public English page verified October 19, 2026; both privacy source templates updated with private backups. Legacy Vietnamese privacy URL redirected to the English canonical page during this check. Mobile support and unrelated partner/store-publisher references were not changed |
| MCP guide | Refers to seven focused servers despite 11 routes; calls analytics fully read-only despite export-report; overstates Hybrid approval coverage. Synchronize production copy |
| Data processing | Owner confirmation needed for processors, actual retention, secondary-use restrictions and security escalation contact |

## Engineering validation and remaining gaps

1. Tool serialization now supplies explicit readOnlyHint, destructiveHint and openWorldHint booleans and a title. Conservative defaults apply when a tool has not declared a more specific hint. Directory live discovery confirmed the annotation fixes; OpenAI's own scan remains pending.
2. The dedicated Claude catalog enforces its allowlist at discovery and execution, excludes AI media and arbitrary dispatchers, and provides English metadata. The full endpoint retains Gen AI. The previous Claude catch-all flag no longer appears; four advisory documentation suggestions remain.
3. Final local MCP feature/unit regressions passed **249 tests / 36,085 assertions**. A live smoke test found internal product pagination URLs; the controller-dispatch request now preserves the public MCP request URL, with eight commerce tests passing and a real Claude retest confirming public URLs. These tests do not replace all-tool authenticated business execution.
4. Muse OAuth read-only behavior and its exact callback/origin still require verification before claiming support. No permissive redirect wildcard or environment change was introduced.
5. The published MCP guide still needs synchronization with actual module routes, export writes and approval behavior.

Production changes now include the dedicated directory server, annotation/schema corrections, a read-only broadcast sender lookup and the pagination fix, with private rollback copies. No Gen AI handlers or environment variables were changed. Earlier identity/contact and domain-verification changes remain in place.

## Platform-specific work

- **OpenAI:** domain challenge is verified. OAuth, tool scans, reviewer access, video and final attestations remain pending. The draft ZIP can be reviewed locally but is not submission-ready.
- **Claude bundle:** 1.0.2 at `4ac9cfa` passed format, directory-policy and security scans. Publish requested; waiting for an Anthropic reviewer, not live. The separate connector draft uses the new profile and remains incomplete because all-tool testing and its own policy declarations have not been completed. Public source: https://github.com/trolypage/trolypage-plugins.
- **Muse:** intake submitted with payments accepted and external payment explicitly disclosed; the owner confirmed the displayed terms. DCR/PKCE integration credentials and reviewer access were submitted securely. Business verification is complete. The overview shows 2/3 follow-up requirements complete; data-processing questionnaire, fixtures, end-to-end tests and any further reviewer requirements remain pending.

## Next preparation steps

Confirm independent sign-in and OAuth, populate synthetic fixtures and record approval mode for each test round. Full / Direct execution does not mean every write enters a queue. The bundle license is Apache-2.0. Select the demo hosting destination and record real fixture IDs. Resolve findings for the intended catalog, run tests and record a real video. Add its verified URL, rebuild, inspect validation and hashes, and only then finalize an authorized draft upload.

## Production environment check

On October 19, 2026, the owner authorized server file-manager access for verification setup and an environment check. The OpenAI challenge file was added under public/.well-known and the portal verified the domain. Only non-secret MCP configuration fields were inspected from .env and bootstrap/cache/config.php. MCP is enabled and the OAuth issuer is configured. Both allowed_origins and redirect_domains currently omit Muse hosts. No allowlist was broadened: the exact Muse OAuth callback/origin must be obtained and verified before adding narrowly scoped entries. Absence of a MUSE-prefixed variable alone does not mean generic DCR/PKCE is unsupported. No secret environment values or reviewer credentials are included here.
