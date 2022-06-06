# 10871

import sys

n, x = map(int, sys.stdin.readline().split())

if ((n >= 1 and n <= 10000) and (x >= 1 and x <= 10000)):
	inlist = [int(i) for i in input().strip().split()]
	res = []
	for	i in range(0, n):
		if (inlist[i] < x):
			res.append(inlist[i])
	for i in res:
		print(i, end=' ')