---
tags: [engineering-practices, ai-engineering, laravel]
sources: [PHP Laravel experience.md, Senior developer experience.md]
created: 2026-10-29
updated: 2026-10-29
---

# PhpStorm

IDE PHP của JetBrains. Bộ **inspection** của nó (phân tích tĩnh chạy ngay trong editor) được dùng làm chuẩn code cho AI agent.

## Inspection làm coding convention

Theo [[senior-developer-experience|Senior Developer Experience]], JetBrains inspection giúp AI agent:
- đặt tên biến tốt hơn;
- viết khối code dài dòng thành gọn;
- phát hiện các lỗi cơ bản;
- gợi ý cú pháp mới nhanh và gọn hơn, ví dụ closure → arrow function có khai báo type:

```php
// Bad
$calculator = function ($a, $b) {
	return $a + $b;
}

// Good
$calculator = fn (int $a, int $b): int => $a + $b;
```

## Inspect CLI

PhpStorm có lệnh `inspect` (`bin/inspect.bat` / `inspect.sh`) để chạy cùng bộ inspection đó từ CLI, dùng license PhpStorm sẵn có. Theo [[php-laravel-experience|PHP Laravel Experience]]:
- rule cấu hình bằng file inspection profile XML, cùng format với profile export từ IDE;
- quét theo file thay đổi chưa commit (`-changes`), theo thư mục (`-d <dir>`) hoặc toàn project;
- output gom thành mỗi lỗi một dòng `[SEVERITY] file:line InspectionId - message` để agent đọc.

Cách agent dùng tool này trong quy trình: [[agent-self-inspection|Agent Self Inspection]].

Nguồn: [[php-laravel-experience|PHP Laravel Experience]], [[senior-developer-experience|Senior Developer Experience]].
