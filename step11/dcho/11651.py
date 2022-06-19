# 11650

import sys

n = int(sys.stdin.readline())
li: list = []

for i in range(n):
	x, y = map(int,sys.stdin.readline().split())
	li.append([x, y])

li.sort(key=lambda x:(x[1], x[0]))
for i in li:
	for j in i:
		print(j, end=' ')
	print()
