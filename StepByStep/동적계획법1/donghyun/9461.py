from functools import lru_cache
import sys

@lru_cache(maxsize=None)
def f(n):
	if n <= 3:
		return 1
	return f(n-3) + f(n-2)

input = sys.stdin.readline
for _ in range(int(input())):
	print(f(int(input())))
