# Tài khoản demo, kiểm thử và video

## Trạng thái

Chủ tài khoản sẽ tạo workspace demo và gửi thông tin sau. Hiện chưa có tài khoản reviewer, chưa chạy ca kiểm thử nghiệp vụ, chưa quay video và chưa có demo URL. Tệp test-cases.json là đặc tả; tất cả kết quả ở test-results.csv đang Not run. Không dùng tài khoản hoặc dữ liệu khách thật.

## Chuẩn bị workspace riêng

1. Tạo workspace demo tách biệt, user owner/admin riêng, gói có đủ module cho các ca đã khai. Ghi tên, URL đăng nhập và timezone vào fixture-map.json; không ghi mật khẩu ở đó.
2. Tạo customer `Review Customer A` với hội thoại tổng hợp chỉ gồm thông tin thử nghiệm. Không dùng số điện thoại/email khách thật.
3. Tạo sản phẩm `Review Mug`, SKU `TLP-REVIEW-MUG`, giá 100000 VND, tồn kho 20, active. Ghi ID thực được app cấp vào fixture-map.json; không tự đặt ID. Chuẩn bị dữ liệu đơn demo trong hai khoảng so sánh báo cáo.
4. Đặt và ghi nhận approval mode cho từng lần chạy. Không kết nối ngân hàng/carrier gửi thật. Tránh auto-fulfillment, notification và workflow có thể kích hoạt từ fixture order/note; kiểm tra chúng trước khi test.
5. Nếu review module social, nối một Page/tài khoản thử nghiệm do bạn quản lý. Thử lưu nháp không có scheduled_at; không publish. Những tools cần provider thật phải có sandbox/fixture và hướng dẫn riêng.
6. Cấp quyền đủ cho reviewer nhưng chỉ trong workspace demo. Tài khoản cần đăng nhập độc lập, không chờ điện thoại, mã email hoặc phê duyệt từ bạn. Nhập credentials qua trường bảo mật của từng portal, không Git/chat/listing.

## Bộ ca đại diện

test-cases.json chứa đúng 5 positive và 3 negative theo format OpenAI, có setup, prompt, tool names và điều kiện pass. Dùng cùng kịch bản để review Claude/Muse sau khi điều chỉnh đúng catalog. Năm ca dương: đọc khách/hội thoại, tra cứu catalog, đơn chờ shop duyệt, báo cáo so sánh, ghi chú CRM nội bộ. Ba ca âm: chuyển tiền, truy cập workspace trái phép, lấy secrets.

Chạy hai vòng cho writes: vòng thông thường và vòng phải chờ MCP approval. Chỉ operator demo phê duyệt. Ghi host, package hash, timestamp, tool arguments đã loại secrets, returned IDs/states và evidence vào test-results.csv. Đối chiếu expected behavior trước khi đổi Not run sang Passed/Failed/Blocked.

## Bổ sung kiểm thử khi expose toàn bộ catalog

| Module | Kịch bản bổ sung |
| --- | --- |
| Social | Resolve account, lưu draft, get-social-post xác nhận chưa đăng; schedule/publish chỉ trong test provider với approval thật |
| Marketing | Tạo broadcast draft và preview audience; submit vào pending_review không đồng nghĩa đã gửi |
| Knowledge | Search approved fact, import sample document, kiểm tra ingestion readiness; đề xuất fact không thành approved fact |
| Agents | Read setup, tạo inactive draft, preflight; không gọi live-delivery check là bằng chứng khách nhận tin |
| Assets | Upload bytes fixture, poll verification, inspect real asset; không đưa local path giả cho server |
| Automation | Save draft, check, simulate, review returned state; publish có thể bắt đầu tác vụ thật |
| Integrations | Dedicated test endpoint; secret entry in app; check before enable; inspect execution trước retry/replay |
| Commerce | Inventory/idempotency boundaries, cancellation/status, quote expiry, no duplicate shipment/payment request |

full-tool-test-ledger.csv có toàn bộ 270 tools với module và Not run. Các tác vụ generate media hiện không được đưa vào catalog Claude cho tới khi policy/phạm vi phù hợp.

## Kịch bản quay demo thật — khoảng 5 phút

| Thời gian gợi ý | Thao tác thật và kết quả phải thấy |
| --- | --- |
| 0:00–0:25 | Hiện host đang dùng và bản plugin 1.0.1; nêu demo workspace, phạm vi quyền và endpoint |
| 0:25–1:00 | Prompt P1; thấy tên customer và tóm tắt đúng đoạn hội thoại |
| 1:00–1:35 | Prompt P2; thấy SKU, giá và tồn kho thực |
| 1:35–2:35 | Prompt P3; thấy approval nếu có, sau đó order pending_review; không trả tiền hay tạo shipping |
| 2:35–3:15 | Prompt P4; thấy hai khoảng ngày và số liệu từ server |
| 3:15–4:00 | Prompt P5; sau write/re-read có note nội bộ, không gửi tin |
| 4:00–4:30 | Một negative prompt; thấy giới hạn và không có hành động trái phép |
| 4:30–5:00 | Nêu support, payment ngoài host, trạng thái pending khác completed |

Rehearse trước. Khi tài khoản demo đã sẵn sàng, có thể dùng phiên cài phát triển sẵn có để quay; không cần upload draft submission chỉ để bắt đầu. Dùng screen recorder thật, không dùng mockup hay ghép kết quả giả. Che mật khẩu, tokens, mailbox và các workspace khác. Xem lại video để kiểm tra đọc được prompt/kết quả, đủ các ca và không lộ secrets. Host ở nơi reviewer mở/play được, kiểm tra bằng phiên chưa đăng nhập rồi mới thêm URL vào manifest. Chưa có nơi host được chọn trong lượt chuẩn bị này.

## Mẫu nội dung reviewer access — chỉ nhập qua dashboard bảo mật

Login URL, demo workspace name, username, password/sign-in method, account permissions and plan, fixture setup, expected approval steps, instructions for testing without real charges. Đây là checklist trường cần điền; không chép credentials vào repo. Test account phải tiếp tục hoạt động khi review hoặc re-review.
