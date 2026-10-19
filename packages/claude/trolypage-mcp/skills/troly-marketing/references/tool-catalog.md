# Current source tool reference

Human-readable source descriptions have been translated into English. Tool identifiers and contracts are unchanged; live server wording may differ.

Source snapshot: 2026-10-19. Tools are filtered by the connected workspace. A listed capability is not proof of entitlement or successful execution.

| Tool | Module | Declared annotation(s) | Description |
| --- | --- | --- | --- |
| `list-strategies` | marketing | readOnlyHint=true | List workspace marketing strategies. |
| `get-strategy` | marketing | readOnlyHint=true | Marketing strategy details: objectives, channel mix, value proposition and child campaigns. |
| `create-strategy` | marketing | destructiveHint=true, openWorldHint=true | Create a draft marketing strategy. Other tools can create its campaigns and broadcasts. |
| `list-campaigns` | marketing | readOnlyHint=true | List workspace campaigns, optionally filtered by strategy. |
| `create-campaign` | marketing | destructiveHint=true, openWorldHint=true | Create a draft/planned campaign within a strategy. |
| `list-broadcasts` | marketing | readOnlyHint=true | List workspace broadcasts and approval states. |
| `create-broadcast` | marketing | destructiveHint=true, openWorldHint=true | Compose a draft broadcast with an estimated audience size. Actual sending requires submit-broadcast and shop-owner approval in the app. |
| `submit-broadcast` | marketing | destructiveHint=true, openWorldHint=true | Submit a composed broadcast for preparation and review (draft -> preparing -> pending_review). Actual sending requires shop-owner approval in TrolyPage; the AI does not autonomously send bulk messages. |
| `broadcast-stats` | marketing | readOnlyHint=true | Broadcast statistics: sent, delivered and failed counts. |
| `list-nurture-sequences` | marketing | readOnlyHint=true | List workspace nurture sequences for automated multistep customer care. |
| `create-nurture-sequence` | marketing | destructiveHint=true, openWorldHint=true | Create a draft nurture sequence triggered by events such as new tags, new customers or birthdays. |
| `list-followups` | marketing | readOnlyHint=true | List workspace follow-ups for customers who have not completed a purchase. |
| `create-followup-suggestion` | marketing | destructiveHint=true, openWorldHint=true | Propose a customer follow-up; requires approval before activation. |
| `cancel-broadcast` | marketing | destructiveHint=true | cancel broadcast |
| `delete-broadcast` | marketing | destructiveHint=true | delete broadcast |
| `delete-campaign` | marketing | destructiveHint=true | delete campaign |
| `delete-nurture` | marketing | destructiveHint=true | delete nurture |
| `delete-strategy` | marketing | destructiveHint=true | delete strategy |
| `get-broadcast` | marketing | readOnlyHint=true | get broadcast |
| `get-campaign-goals` | marketing | readOnlyHint=true | get campaign goals |
| `get-campaign` | marketing | readOnlyHint=true | get campaign |
| `get-followup` | marketing | readOnlyHint=true | get followup |
| `get-nurture` | marketing | readOnlyHint=true | get nurture |
| `list-audience-tags` | marketing | readOnlyHint=true | list audience tags |
| `pause-followup` | marketing | destructiveHint=true | pause followup |
| `pause-nurture` | marketing | destructiveHint=true | pause nurture |
| `preview-broadcast-audience` | marketing | readOnlyHint=true | preview broadcast audience |
| `resume-followup` | marketing | destructiveHint=true | resume followup |
| `resume-nurture` | marketing | destructiveHint=true | resume nurture |
| `retry-followup` | marketing | destructiveHint=true | retry followup |
| `skip-next-followup` | marketing | destructiveHint=true | skip next followup |
| `update-broadcast` | marketing | destructiveHint=true | update broadcast |
| `update-campaign` | marketing | destructiveHint=true | update campaign |
| `update-followup` | marketing | destructiveHint=true | update followup |
| `update-nurture` | marketing | destructiveHint=true | update nurture |
| `update-strategy` | marketing | destructiveHint=true | update strategy |
