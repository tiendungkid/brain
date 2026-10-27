---
tags: [engineering-practices, ai-engineering, laravel]
sources: [PHP Laravel - Kinh nghiệm code.md]
created: 2026-10-27
updated: 2026-10-27
---

# PHP Laravel - Kinh Nghiệm Code

**Source:** PHP Laravel - Kinh nghiệm code.md
**Date ingested:** 2026-10-27
**Type:** notes

## Summary

Ghi chú cá nhân tổng hợp những điểm thường phải sửa khi code PHP/[[laravel|Laravel]] cùng AI agent. Mỗi điểm có ví dụ "Bad" / "Good" minh hoạ; code mẫu mang tính ý nghĩa, không nhằm đúng tuyệt đối. Ví dụ xoay quanh việc kiểm tra `signature` bằng secret của Shopify app.

1. **Casting variable** — không ép kiểu ở chỗ dùng (`(string) config(...)`), ép kiểu một lần trong file config (`(string) env(...)` trong `services.php`).
2. **Comment** — để tên biến/hàm tự biểu đạt nhiệm vụ, không comment từng dòng; gộp các điều kiện chặn cùng mục đích (`if (! $secret || ! $signature)`).
3. **Lồng nhiều hàm vào một câu điều kiện** — AI agent hay gói nhiều lời gọi hàm vào một biểu thức `return`; đúng nhưng khó đọc. Tách từng phần ra biến có tên rồi mới ghép lại.
4. **Tools** — skill `php-pro` của [[claude-skills|Claude Skills]] và [[shopify-app-security-checks|Shopify App Security Checks]].

## Key Claims

- Ép kiểu giá trị config nên đặt trong file config, không rải ở code nghiệp vụ.
- Tên biến/hàm rõ nghĩa thay thế cho comment mô tả từng dòng.
- Biểu thức lồng nhiều hàm nên tách thành biến trung gian có tên trước khi kết hợp.
- AI agent viết code đúng nhưng thường mắc các lỗi về khả năng đọc ở trên.

## Entities Mentioned

- [[laravel|Laravel]] — framework của các ví dụ (`config()`, `env()`, `services.php`)
- [[claude-skills|Claude Skills]] — skill `php-pro` được khuyến nghị
- [[shopify-app-security-checks|Shopify App Security Checks]] — công cụ kiểm tra bảo mật app

## Concepts Covered

- [[ai-generated-code-pitfalls|AI Generated Code Pitfalls]] — bối cảnh chung của ghi chú
- [[config-level-casting|Config Level Casting]] — điểm 1
- [[self-documenting-code|Self Documenting Code]] — điểm 2
- [[explaining-variables|Explaining Variables]] — điểm 3
