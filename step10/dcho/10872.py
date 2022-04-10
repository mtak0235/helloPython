# 10872

import sys

def Factorial(n: int) -> int:
	if n == 0 or n == 1:
		return 1
	return Factorial(n - 1) * n

n = int(sys.stdin.readline())
print(Factorial(n))
