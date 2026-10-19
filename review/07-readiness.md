# Những mục cần hoàn tất trước khi nộp

Trạng thái bộ hồ sơ: **REVIEW DRAFT**. Đã chuẩn bị source/ZIP/nội dung; chưa upload hay submit ở bất kỳ portal nào. Kiểm tra cấu trúc local không thay thế scan hoặc review của nền tảng.

## Chung

| Mục | Tình trạng / bước tiếp theo |
| --- | --- |
| Tên listing, email, quốc gia, commerce, logo | Đã có lựa chọn của chủ tài khoản; người phụ trách: Alex Nguyen |
| Danh tính OpenAI | Verified; Business — Trolypage chọn được trong hộp upload |
| Metadata / 5+3 cases / release / VI translation | Đã đưa vào OpenAI ZIP candidate |
| Logo mobile | Đã copy bản gốc và tạo bản kích thước phù hợp; cần review hình và ảnh hưởng ở 32/64 px |
| Endpoint/discovery | Public status và OAuth metadata mở được; chưa kiểm thử đăng nhập OAuth đầy đủ |
| Reviewer account | Chủ tài khoản sẽ tạo sau |
| Authenticated tool tests | 270 tools chưa chạy; 5+3 ca đại diện chưa chạy |
| Video | Mới có kịch bản và hướng dẫn quay; chưa có bản ghi/URL thực |
| Live policy identity | Privacy section 13 và mobile support còn SkyNet Solution; Privacy còn địa chỉ 9243 Quail Creek Ln, Boulder, US, khác footer TROLYPAGE COMPANY LIMITED/Hà Nội. Xác nhận quan hệ pháp nhân hoặc sửa bản đã xuất bản. Không tự coi đây là đã sửa |
| MCP guide | Còn mô tả "seven focused servers" dù status có 11 routes; nói analytics 100% read-only nhưng có export-report là write; mô tả Hybrid quá rộng. Cần đồng bộ production copy |
| Data processing | Owner xác nhận subprocessors, retention thực, secondary-use restrictions và security escalation contact |

## Engineering findings cần giải quyết theo catalog định gửi

1. **Annotations OpenAI:** snapshot `toArray()` của cả 270 tools thiếu ít nhất một trong ba boolean readOnlyHint, destructiveHint, openWorldHint. Không tự điền giá trị false vào tài liệu rồi coi server đã sửa. Cần sửa annotation serialization/attributes dựa trên hành vi từng tool, review semantics và kiểm tra tools/list production sau deploy. File annotation-gaps.csv nêu từng trường thiếu.
2. **Claude image generation:** endpoint chung có generate-social-image. Không submit nguyên catalog như đã đạt policy; cần filter enforce thật và re-test. Bundled skills không tự giới hạn remote tools.
3. **Claude operation dispatcher:** execute-integration-operation chỉ có openWorldHint, có thể thực thi configured HTTP operation. Cần đánh giá split read/write và annotation phù hợp, hoặc loại khỏi profile Claude. Không gọi tool này để vòng qua media/financial restrictions.
4. **Muse Read Only:** source OAuth hiện chỉ công bố mcp:use; read-only catalog filtering chỉ thấy với API token mcp:read. Xem xét cung cấp lựa chọn read-only OAuth nơi khả thi. Không khai đã hỗ trợ rồi dùng API key để thay OAuth trong form OpenAI.
5. **Schema extraction:** 267/270 tools serialize input schema trong container cô lập không nạp .env/DB. Ba schema còn thiếu cần runtime inspection; đây là hạn chế kiểm tra, không phải chứng minh lỗi server. Chưa có authenticated tools/list snapshot để xác nhận wire annotations.

Không sửa server ứng dụng trong repo chuẩn bị hồ sơ này. Các finding được giữ thành backlog review để chủ sản phẩm quyết định và triển khai trước khi chốt public submission.

## Riêng từng nơi

- OpenAI: domain challenge, OAuth connection, scans, reviewer access, video, final attestations còn pending. ZIP DRAFT có thể đọc review; chưa được gắn nhãn ready for review submission.
- Claude connector: policy catalog, tool tests và reviewer access còn pending. Bundle còn cần license do owner chọn và portal validation; repo public đã tạo tại https://github.com/trolypage/trolypage-plugins. Không upload backend monorepo.
- Muse: Payments category cần đối chiếu định nghĩa external payment; tech/review form bước sau chưa được thao tác; questionnaire, test account, host approvals và terms do owner hoàn tất.

## Khi bạn gửi tài khoản demo

Người phụ trách đã xác nhận là Alex Nguyen. Xác nhận tên/URL workspace, license và nơi host demo; điền fixture IDs thực. Hoàn tất các engineering/policy finding theo phạm vi gửi duyệt. Chạy test, quay video thật, thêm URL, build lại và đọc validation report cùng SHA-256. Khi đó mới chốt upload draft và review thông tin đã import.
