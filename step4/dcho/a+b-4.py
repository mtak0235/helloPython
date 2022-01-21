# 10951

import sys

i = 0
while i < 5:
	a, b = map(int, sys.stdin.readline().split())
	if (a < 0 or a > 10 or b < 0 or b > 10):
		break
	print(a + b)
	i += 1