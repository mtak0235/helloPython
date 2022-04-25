# 10870

import sys

n = int(sys.stdin.readline())
def Fibonacci(n: int) -> int:
	if n == 0:
		return 0
	if n == 1:
		return 1
	return Fibonacci(n - 1) + Fibonacci(n - 2)

print(Fibonacci(n))
