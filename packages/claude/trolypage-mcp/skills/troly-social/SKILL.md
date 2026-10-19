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

Use existing or user-supplied media for posts. This directory connection does not generate or clean AI images, video or audio.

Do not retry successful targets, publish to an unconfirmed account, or imply AI timing/caption suggestions are measured facts.
