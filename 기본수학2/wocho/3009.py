prev_a = prev_b = a = b = 0
for _ in range(3):
	x, y = map(int, input().split())
	if a == 0:
		a = x
	elif a == x:
		if prev_a:
			a = prev_a
	else:
		if prev_a != x:
			prev_a = a
			a = x
	if b == 0:
		b = y
	elif b == y:
		if prev_b:
			b = prev_b
	else:
		if prev_b != y:
			prev_b = b
			b = y

print(a, b)