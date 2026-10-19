---
name: troly-social
description: Operate TrolyPage social accounts and posts across drafting, scheduling, publishing, retrying, caption and hashtag generation, timing suggestions, and analytics. Use for social-media planning or execution.
---

# TrolyPage Social

Use only the `trolypage` MCP server. Read [tool-catalog.md](references/tool-catalog.md) to select the tools available for this workflow.

## Workflow

1. Call `list-social-accounts` to resolve real connected targets.
2. Inspect an existing post before update, cancellation, publish, or retry.
3. Separate content creation from publication: `create-social-post` makes a draft/schedule; `publish-social-post` performs the external effect.
4. Confirm target accounts, final copy, media, schedule/timezone, and publish mode before publishing.
5. Report queued or approval state without claiming publication succeeded; verify with `get-social-post`.

For user-requested cleanup of external images, upload/import the file into the media library first. Call `detect-asset-c2pa`, then `clean-asset-image` with the source `asset_id`, an `action` (`strip-c2pa` or `clear-synthid`) and an `idempotency_key`. Use the returned new `asset_id` in the post's `media_ids`; the original stays intact. Reuse the same key/arguments on retry. These tools require the assets module. C2PA scans are heuristic, and SynthID removal is not verified; never promise that an image will avoid AI labeling. Image cleanup does not apply to text captions.

Do not retry successful targets, publish to an unconfirmed account, or imply AI timing/caption suggestions are measured facts.
