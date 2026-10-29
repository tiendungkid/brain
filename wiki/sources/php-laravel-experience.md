---
tags: [engineering-practices, ai-engineering, laravel]
sources: [PHP Laravel experience.md]
created: 2026-10-27
updated: 2026-10-29
---

# PHP Laravel Experience

**Source:** PHP Laravel experience.md (trước đây là PHP Laravel - Kinh nghiệm code.md)
**Date ingested:** 2026-10-27, cập nhật 2026-10-29
**Type:** notes

## Summary

Ghi chú cá nhân tổng hợp những điểm thường phải sửa khi code PHP/[[laravel|Laravel]] cùng AI agent. Mỗi điểm có ví dụ "Bad" / "Good" minh hoạ; code mẫu mang tính ý nghĩa, không nhằm đúng tuyệt đối. Ví dụ xoay quanh việc kiểm tra `signature` bằng secret của Shopify app.

1. **Casting variable** — không ép kiểu ở chỗ dùng (`(string) config(...)`), ép kiểu một lần trong file config (`(string) env(...)` trong `services.php`).
2. **Comment** — để tên biến/hàm tự biểu đạt nhiệm vụ, không comment từng dòng; gộp các điều kiện chặn cùng mục đích (`if (! $secret || ! $signature)`).
3. **Lồng nhiều hàm vào một câu điều kiện** — AI agent hay gói nhiều lời gọi hàm vào một biểu thức `return`; đúng nhưng khó đọc. Tách từng phần ra biến có tên rồi mới ghép lại.
4. **Tools** — skill `php-pro` của [[claude-skills|Claude Skills]], [[shopify-app-security-checks|Shopify App Security Checks]] và PhpStorm Inspect CLI của [[phpstorm|PhpStorm]].
5. **Chạy PhpStorm inspect trước khi báo xong** (thêm 2026-10-29):
   - Code AI viết thường chạy được nhưng vẫn dính lỗi PhpStorm bắt ngay: gọi method không tồn tại, sai type, biến không dùng, điều kiện luôn đúng/sai, code chết.
   - Sau khi sửa code PHP/Laravel, agent phải tự chạy inspect và sửa hết lỗi trước khi báo hoàn thành.
   - Rule nằm trong một file inspection profile XML, cùng format với profile của PhpStorm.
   - Ba chế độ quét: `-changes` (file có thay đổi chưa commit, mặc định; file mới phải `git add -N` trước), `-d <dir>` (một thư mục), không tham số (toàn project).
   - Output mỗi lỗi một dòng: `[SEVERITY] file:line InspectionId - message`.

## Key Claims

- Ép kiểu giá trị config nên đặt trong file config, không rải ở code nghiệp vụ.
- Tên biến/hàm rõ nghĩa thay thế cho comment mô tả từng dòng.
- Biểu thức lồng nhiều hàm nên tách thành biến trung gian có tên trước khi kết hợp.
- AI agent viết code đúng nhưng thường mắc các lỗi về khả năng đọc ở trên.
- Agent phải chạy PhpStorm inspect và sửa sạch lỗi trước khi báo xong. Quy tắc:
  1. Sửa toàn bộ `ERROR`, `WARNING` trong file mình vừa viết/sửa; `WEAK WARNING` chỉ sửa nếu nằm trong dòng mình vừa đụng tới.
  2. Không sửa lỗi cũ ở file không liên quan (ngoài scope, làm diff phình to).
  3. Không né lỗi bằng `@noinspection`, `@phpstan-ignore`, tắt inspection hay cast bừa; false positive thì để nguyên và ghi rõ lý do khi báo cáo.
  4. Chạy lại đến khi sạch, báo kết quả lần chạy cuối.
  5. Tool không chạy được (không tìm thấy PhpStorm, thiếu license) thì báo cho người dùng, không coi là đã pass.

## Entities Mentioned

- [[laravel|Laravel]] — framework của các ví dụ (`config()`, `env()`, `services.php`)
- [[claude-skills|Claude Skills]] — skill `php-pro` được khuyến nghị
- [[shopify-app-security-checks|Shopify App Security Checks]] — công cụ kiểm tra bảo mật app
- [[phpstorm|PhpStorm]] — Inspect CLI dùng để agent tự kiểm tra code

## Concepts Covered

- [[ai-generated-code-pitfalls|AI Generated Code Pitfalls]] — bối cảnh chung của ghi chú
- [[config-level-casting|Config Level Casting]] — điểm 1
- [[self-documenting-code|Self Documenting Code]] — điểm 2
- [[explaining-variables|Explaining Variables]] — điểm 3
- [[agent-self-inspection|Agent Self Inspection]] — điểm 5
