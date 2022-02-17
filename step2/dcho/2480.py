# 2525

import sys


a, b, c  = map(int, sys.stdin.readline().split())

res: int = 0

if a == b == c:
	res = 10000 + a * 1000
elif a == b or a == c:
	res = 1000 + a * 100
elif b == c:
	res = 1000 + b * 100
else:
	maxValue: int = 0
	res = max(maxValue, a, b, c) * 100

print(res)
