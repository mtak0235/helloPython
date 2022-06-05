# 2775

import sys

t: int = int(sys.stdin.readline())

for i in range (t):
	ans: int = 0
	k: int = int(sys.stdin.readline())
	n: int = int(sys.stdin.readline())
	key: list = [x for x in range(1, n+1)]
	for j in range(k):
		for k in range(1, n):
			key[k] += key[k-1]
	print(key[-1])
