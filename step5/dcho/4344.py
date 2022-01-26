# 4344

import sys

n = int(sys.stdin.readline())
doublelist = []
averagelist = [0 for i in range(n)]

for i in range(n):
	doublelist.append(list(map(float, sys.stdin.readline().split())))
	# averagelist[i] += float(x) for x in range(len(doublelist[i]) - 1)
	print(len(doublelist[i]) - 1)
	for j in range(len(doublelist[i]) - 1):
		doublelist[j + 1]

print(averagelist)
