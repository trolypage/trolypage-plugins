# Current source tool reference

Source snapshot: 2026-10-19. Tools are filtered by the connected workspace. A listed capability is not proof of entitlement or successful execution.

| Tool | Module | Declared annotation(s) | Description |
| --- | --- | --- | --- |
| `get-automation-catalog` | automation | readOnlyHint=true | List permitted automation actions and event schemas. |
| `list-automation-templates` | automation | readOnlyHint=true | List built-in workflow templates. |
| `get-automation-template` | automation | readOnlyHint=true | Get one workflow template definition. |
| `get-automation-options` | automation | readOnlyHint=true | Search workspace resources for workflow configuration. |
| `list-automation-workflows` | automation | readOnlyHint=true | List workspace workflows. |
| `get-automation-workflow` | automation | readOnlyHint=true | Get a workflow draft and status. |
| `save-automation-workflow` | automation | destructiveHint=true | Save a workflow draft using its revision. |
| `check-automation-workflow` | automation | destructiveHint=true | Persist workflow validation and audience preview. |
| `simulate-automation-workflow` | automation | readOnlyHint=true | Simulate workflow steps without side effects. |
| `publish-automation-workflow` | automation | destructiveHint=true, openWorldHint=true | Publish a checked workflow revision. |
| `pause-automation-workflow` | automation | destructiveHint=true | Pause a published workflow. |
| `resume-automation-workflow` | automation | destructiveHint=true | Resume a published workflow. |
| `preview-automation-audience` | automation | readOnlyHint=true | Preview eligible recipients without contacting providers. |
| `review-automation-phones` | automation | destructiveHint=true, openWorldHint=true | Resolve Zalo phone recipients without sending messages. |
| `list-automation-runs` | automation | readOnlyHint=true | List workflow runs. |
| `get-automation-run` | automation | readOnlyHint=true | Get run steps and outcomes. |
| `cancel-automation-run` | automation | destructiveHint=true | Cancel remaining workflow steps. |
| `retry-automation-run` | automation | destructiveHint=true | Retry a failed or denied action when allowed. |
| `list-automation-tasks` | automation | readOnlyHint=true | List automation tasks. |
| `update-automation-task` | automation | destructiveHint=true | Update an automation task status. |
