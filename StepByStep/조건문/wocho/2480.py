a, b, c = map(int, input().split())

prize = 0
if a == b and b == c:
	prize += 10000 + a * 1000
elif a == b or b == c or a == c:
	prize += 1000 + 100 * (a if a == b else c)
else:
	prize += max(max(a, b), c) * 100

print(prize)