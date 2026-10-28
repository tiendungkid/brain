---
tags: [shopify-platform, ai-engineering]
sources: [PHP Laravel - Kinh nghiệm code.md, Senior developer experience.md]
created: 2026-10-27
updated: 2026-10-28
---

# Shopify App Security Checks

Công cụ kiểm tra bảo mật cho Shopify app, thuộc Shopify AI Toolkit. Được khuyến nghị dùng kèm khi code cùng AI agent, xem [[ai-generated-code-pitfalls|AI Generated Code Pitfalls]].

- Link: <https://shopify.dev/docs/apps/build/security/app-security-checks>

## Quy trình sau khi scan

Shopify yêu cầu app dùng công cụ này scan toàn bộ project. Kết quả là danh sách tính năng dính lỗi, dev fix theo báo cáo. Vì báo cáo viết bằng ngôn ngữ kỹ thuật, cần một [[qa-quick-checklist|QA Quick Checklist]] để QA biết Shopify yêu cầu gì, dev đã làm gì và cần test gì.

Nguồn: [[php-laravel-kinh-nghiem-code|PHP Laravel - Kinh Nghiệm Code]], [[senior-developer-experience|Senior Developer Experience]].
