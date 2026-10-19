# Current source tool reference

Source snapshot: 2026-10-19. Tools are filtered by the connected workspace. A listed capability is not proof of entitlement or successful execution.

| Tool | Module | Declared annotation(s) | Description |
| --- | --- | --- | --- |
| `list-strategies` | marketing | readOnlyHint=true | Danh sách chiến lược marketing của workspace. |
| `get-strategy` | marketing | readOnlyHint=true | Chi tiết một chiến lược marketing: mục tiêu, channel mix, giá trị đề xuất, campaign con. |
| `create-strategy` | marketing | destructiveHint=true, openWorldHint=true | Tạo chiến lược marketing mới (draft). Từ strategy có thể sinh campaign, broadcast qua các tool khác. |
| `list-campaigns` | marketing | readOnlyHint=true | Danh sách chiến dịch của workspace (có thể lọc theo strategy). |
| `create-campaign` | marketing | destructiveHint=true, openWorldHint=true | Tạo chiến dịch mới trong một chiến lược (draft/planned). |
| `list-broadcasts` | marketing | readOnlyHint=true | Danh sách broadcast (tin nhắn hàng loạt) của workspace kèm trạng thái duyệt. |
| `create-broadcast` | marketing | destructiveHint=true, openWorldHint=true | Soạn broadcast mới (draft kèm ước tính số người nhận). Gửi thật là bước submit-broadcast → chủ shop duyệt trong app. |
| `submit-broadcast` | marketing | destructiveHint=true, openWorldHint=true | Gửi broadcast đã soạn vào hàng đợi chuẩn bị và duyệt (draft → preparing → pending_review). Chủ shop duyệt trong TrolyPage rồi broadcast mới được gửi thật — AI không bao giờ tự gửi hàng loạt. |
| `broadcast-stats` | marketing | readOnlyHint=true | Thống kê một broadcast: số đã gửi, giao thành công, thất bại. |
| `list-nurture-sequences` | marketing | readOnlyHint=true | Danh sách chuỗi nurture (chăm sóc khách tự động nhiều bước) của workspace. |
| `create-nurture-sequence` | marketing | destructiveHint=true, openWorldHint=true | Tạo chuỗi nurture mới (draft). Chuỗi tự động chăm sóc khách theo trigger (tag mới, khách mới, sinh nhật...). |
| `list-followups` | marketing | readOnlyHint=true | Danh sách follow-up (nhắc lại khách chưa chốt) của workspace. |
| `create-followup-suggestion` | marketing | destructiveHint=true, openWorldHint=true | Tạo đề xuất follow-up cho khách chưa chốt (chờ duyệt trước khi kích hoạt). |
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
