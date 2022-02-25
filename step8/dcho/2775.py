# 2775

import sys

t: int = int(sys.stdin.readline())
ans: list = []
for i in range(t):
	k = int(sys.stdin.readline())
	n = int(sys.stdin.readline())
	key: list = [x for x in range(1, n+1)]
	for j in range(k + 1):
		for k in range(1, n):
			key[k] += key[k-1]
	print(key[-1])
