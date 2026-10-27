Đây là tất cả các kinh nghiệm khi code trong php/laravel tôi có khi làm việc với các AI agent mà cần sửa.

#### 1. Casting variable

Không castings biến ở phần coding, trong khi có thể casting trong file config

```php
// Bad
$secret = (string) config('services.shopify.secret');

// Good services.php
'shopify' => [
	'secret' => (string) env('SHOPIFY_API_SECRET', ''),
],
```


#### 2. Comment

Hãy để tên các biến, hàm tự biểu đạt nhiệm vụ của nó, đừng mỗi dòng là 1 comment để biểu diễn nó làm gì.
```php

// bad
$s = config('services.shopify.secret');
$s = $query['signature'][0] ?? null;

if (! $secret) {
	return false;
}

if (! $signature) {
	return false;
}

// God

$secret = config('services.shopify.secret');
$signature = $query['signature'][0] ?? null;

if (! $secret || ! $signature) {
	return false;
}
```


#### 3. Lồng ghép nhiều hàm vào 1 câu điều kiện

Đôi khi AI agents sẽ kiểm tra toàn bộ các điều kiện trong 1 hàm bọc rất nhiều hàm khác vào 1, code thì đúng nhưng cực kỳ khó đọc. Thay vào đó hãy tách từng câu điều kiện ra 1 biến, đặt tên nhiệm vụ của nó rồi mới bắt đầu ghép chúng lại thành 1 câu điều kiện hoàn chỉnh

```php

// Bad
function validSignature(): bool {
	$message = 'Example' // calculated
	return hash_equals(
		hash_hmac(
			'sha256',
			$message, 
			config('services.shopify.secret')
		),
		$query['signature'][0] ?? null
	);
}

// Ok
function validSignature(array $query): bool {
	$secret = config('services.shopify.secret');
	$signature = $query['signature'][0] ?? null;
	
	if (! $secret || ! $signature) {
		return false;
	}
	
	$message = '' // calculated
	return hash_equals(hash_hmac('sha256', $message, $secret), $signature);
}
```

#### 4. Tools

Sử dụng các công cụ sau để phục vụ cho việc code tốt hơn:
1. Claude skills: https://github.com/Jeffallan/claude-skills/blob/main/skills/php-pro/SKILL.md
2. Shopify Security Check - AI Toolkit: https://shopify.dev/docs/apps/build/security/app-security-checks