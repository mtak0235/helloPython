# 1065

import sys

def solve(n: int) -> int:
	ans: int = 0
	for i in range(1, n + 1):
		if (i // 10 < 10): ans += 1
		elif (i // 10 < 100):
			a: int = i // 100
			b: int = i // 10 % 10
			c: int = i % 10
			if (c - b) == (b - a): ans += 1
	return ans

n = int(sys.stdin.readline())
print(solve(n))
