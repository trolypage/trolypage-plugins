# Directory profile tool reference

Source snapshot: 2026-10-19. The server enforces this catalog at discovery and execution. Workspace permissions and plan may further restrict it. A listed capability is not proof of successful end-to-end testing. Annotation details are authoritative in the live MCP response.

| Tool | Module | Description |
| --- | --- | --- |
| `list-strategies` | marketing | List workspace marketing strategies. |
| `get-strategy` | marketing | Marketing strategy details: objectives, channel mix, value proposition and child campaigns. |
| `create-strategy` | marketing | Creates a draft workspace marketing strategy. |
| `list-campaigns` | marketing | List workspace campaigns, optionally filtered by strategy. |
| `create-campaign` | marketing | Create a draft/planned campaign within a strategy. |
| `list-broadcasts` | marketing | List workspace broadcasts and approval states. |
| `create-broadcast` | marketing | Creates a broadcast draft with an estimated audience size. Real sending requires preparation and shop-owner approval in the TrolyPage application. |
| `submit-broadcast` | marketing | Submit a composed broadcast for preparation and review (draft -> preparing -> pending_review). Actual sending requires shop-owner approval in TrolyPage; the AI does not autonomously send bulk messages. |
| `broadcast-stats` | marketing | Broadcast statistics: sent, delivered and failed counts. |
| `list-nurture-sequences` | marketing | List workspace nurture sequences for automated multistep customer care. |
| `create-nurture-sequence` | marketing | Create a draft nurture sequence triggered by events such as new tags, new customers or birthdays. |
| `list-followups` | marketing | List workspace follow-ups for customers who have not completed a purchase. |
| `create-followup-suggestion` | marketing | Propose a customer follow-up; requires approval before activation. |
| `cancel-broadcast` | marketing | Cancels an eligible workspace broadcast. |
| `delete-broadcast` | marketing | Removes a workspace broadcast through its deletion workflow. |
| `delete-campaign` | marketing | Removes a workspace campaign through its deletion workflow. |
| `delete-nurture` | marketing | Removes a workspace nurture through its deletion workflow. |
| `delete-strategy` | marketing | Removes a workspace strategy through its deletion workflow. |
| `get-broadcast` | marketing | Returns workspace broadcast details. |
| `get-campaign-goals` | marketing | Returns workspace campaign goals details. |
| `get-campaign` | marketing | Returns workspace campaign details. |
| `get-followup` | marketing | Returns workspace followup details. |
| `get-nurture` | marketing | Returns workspace nurture details. |
| `list-audience-tags` | marketing | Returns paginated workspace audience tags records. |
| `pause-followup` | marketing | Pauses an existing workspace followup. |
| `pause-nurture` | marketing | Pauses an existing workspace nurture. |
| `preview-broadcast-audience` | marketing | Preview broadcast audience. |
| `resume-followup` | marketing | Resumes an existing workspace followup. |
| `resume-nurture` | marketing | Resumes an existing workspace nurture. |
| `retry-followup` | marketing | Retries an eligible workspace followup. |
| `skip-next-followup` | marketing | Skip next followup. |
| `update-broadcast` | marketing | Updates supplied fields of an existing workspace broadcast. |
| `update-campaign` | marketing | Updates supplied fields of an existing workspace campaign. |
| `update-followup` | marketing | Updates supplied fields of an existing workspace followup. |
| `update-nurture` | marketing | Updates supplied fields of an existing workspace nurture. |
| `update-strategy` | marketing | Updates supplied fields of an existing workspace strategy. |
