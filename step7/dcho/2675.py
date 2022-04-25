# 2675

import sys

n = int(sys.stdin.readline())
for i in range(n):
	a, b = input().split()
	a = int(a)
	ans = ""
	for value in b:
		for j in range(a): ans += value
	print(ans)
