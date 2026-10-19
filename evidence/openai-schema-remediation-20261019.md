# OpenAI MCP schema and metadata remediation — October 19, 2026

This follow-up supersedes the current-status conclusions of the [original 31-finding audit](openai-findings-audit-20261019.md). The original audit remains a historical record.

## Deployed changes

- Added 17 individually discoverable social publication/comment tools, each with fixed server-side behavior and action-specific required fields. The caller cannot change the action selector. Existing controller validation, tenant checks, provider capability checks, receipts and workspace approval handling remain in force. The [actual exported schemas](explicit-social-tool-schemas-20261019.json) are included separately.
- Active Integration Hub API operations now have individually discoverable, workspace-scoped tools with a fixed operation/module and configuration fingerprint. Each publishes its actual HTTP method/destination and the named variables derived from the saved request template. Unlisted variables and operation switching are rejected. Whole-value template variables can accept JSON values; this is not a claim that the upstream API provides narrower field types.
- A changed operation or connection invalidates the old tool. The fingerprint survives queued MCP approval, and the HTTP executor checks configuration again before execution. Existing Integration Hub approval remains applicable.
- Corrected `update-agent-metadata` to describe upserting one stored subscriber field value rather than changing an extraction schema.
- Replaced vague knowledge, social capability/editor, Integration Hub and agent configuration/discovery descriptions with their actual inputs, persisted results and side effects. Configuration/listing/discovery are distinguished from remote execution.
- Clarified workflow draft saving, publishing, reactivation and retry. Publication/reactivation can enable real later business actions and messages; retry can queue an existing failed or denied action. These are not described as harmless simulations or proof of delivery.
- The full MCP retains Gen AI, live agent runtimes and compatibility dispatchers. The Claude directory remains its separately enforced 180-tool catalog. No feature was silently hidden only from discovery.

Private backend commits: `9f1414c72` and `f9da60738`. Backend source and deployment archives are excluded from this public distribution.

## Validation and deployment

- The isolated MCP feature/unit suite passed **268 tests / 36,337 assertions** after the behavioral changes. Its tests include fixed-action dispatch, schema validation, tenant isolation, read-only credentials, stale configuration and queued approval invalidation.
- The Integration/Automation Hub regression subset subsequently passed **15 tests / 137 assertions**. The final metadata-only changes passed PHP syntax validation for all 15 affected files.
- Production preflight compared normalized baseline hashes and checked staged PHP syntax. Deployment used private rollback copies and atomic file replacement; the HTTP and stream pools were refreshed separately. Horizon was refreshed after the behavioral update.
- These checks do not constitute a new real-provider run of every tool. No real customer message, social post, payment or shipment was sent for this remediation. The owner's earlier all-tool attestation is not extended to the 17 new wrappers.

## Portal follow-up

The first follow-up scan discovered **288 tools**, including the 17 new social tools. None of the original 22 description/capability findings appeared in that scan. It reported a new unclear description on `check-integration-configuration`, operation-exposure warnings on four workflow lifecycle tools, and four generic new-tool review notices. Each was inspected individually; the additional metadata changes above were then deployed.

The **final rescan discovered 288 tools and contains zero description/schema/operation-exposure findings**. Six remaining items each have only the notice “This new tool definition needs further review before it can be published”: `send-message`, `inspect-agent`, `apply-agent-tool-preset`, `clean-asset-image`, `get-automation-catalog` and `review-automation-phones`. All six detail panels were inspected. The exact mapping and observed state are recorded in [the final scan evidence](openai-rescan-20261019-final.json).

The old inventory and test ledgers remain the original 271-tool snapshot. The explicit-schema file records the 17-tool delta. Configured API operation tools are generated per eligible workspace configuration and can increase the tool count in other accounts.

The OpenAI plugin remains version **1.0.2**, with the same endpoint, connection and submission identity. The package ZIP has not been replaced and review has not been cancelled. A completed scan is not platform approval, publication, exhaustive execution testing or a guarantee of policy acceptance.
