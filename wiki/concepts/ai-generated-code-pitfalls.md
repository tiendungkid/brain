---
tags: [ai-engineering, engineering-practices]
sources: [PHP Laravel experience.md, Senior developer experience.md]
created: 2026-10-27
updated: 2026-10-29
---

# AI Generated Code Pitfalls

Những lỗi lặp lại khi để AI agent viết code: code thường **chạy đúng** nhưng khó đọc, khó bảo trì. Dùng làm checklist khi review code do AI sinh ra.

## Checklist (PHP/Laravel)

Theo [[php-laravel-experience|PHP Laravel Experience]]:

- Ép kiểu rải rác ở chỗ dùng → chuyển về config, xem [[config-level-casting|Config Level Casting]].
- Tên biến tắt (`$s`) kèm comment từng dòng → đặt tên tự giải thích, xem [[self-documenting-code|Self Documenting Code]].
- Nhiều điều kiện chặn tách rời nhưng cùng kết quả → gộp lại.
- Một biểu thức lồng nhiều lời gọi hàm → tách biến trung gian, xem [[explaining-variables|Explaining Variables]].
- Lỗi IDE bắt được ngay (method không tồn tại, sai type, biến không dùng, code chết) → agent tự chạy inspect trước khi báo xong, xem [[agent-self-inspection|Agent Self Inspection]].

Theo [[senior-developer-experience|Senior Developer Experience]]:

- Closure dài dòng không khai báo type → arrow function có type (`fn (int $a, int $b): int => $a + $b`).

## Công cụ hỗ trợ

- [[claude-skills|Claude Skills]] (`php-pro`) — đưa chuẩn code PHP vào agent.
- [[shopify-app-security-checks|Shopify App Security Checks]] — kiểm tra bảo mật cho Shopify app.
- [[phpstorm|PhpStorm]] Inspect CLI — chạy inspection của IDE từ CLI để agent tự bắt các lỗi trên.
