# 2775

import sys

t: int = int(sys.stdin.readline())
ans: list = []
for i in range(t):
	num: int = 0
	k = int(sys.stdin.readline())
	n = int(sys.stdin.readline())
	if n == 1:
		num += 1
	else:
		for j in range(k + 1):
			for k in range(1, n + 1):
	ans.append(num)

for i in ans:
	print(i)
