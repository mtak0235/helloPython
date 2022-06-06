# 7568

import sys

n:int = int(sys.stdin.readline())
store:list = []
res:list = []

for i in range(n):
	A, B = map(int, sys.stdin.readline().split())
	store.append([A, B])

for i in range(n):
	cnt: int = 1
	for j in range(n):
		if i != j:
			if (store[i][0] < store [j][0]) and (store[i][1] < store[j][1]):
				cnt += 1
	res.append(cnt)

for i in res:
	print(i, end=' ')
