# 4344

import sys

n = int(sys.stdin.readline())
doublelist = []
averagelist = [0 for i in range(n)]
studentRate = [0 for i in range(n)]

for i in range(n):

	doublelist.append(list(map(float, sys.stdin.readline().split())))
	for j in range(len(doublelist[i]) - 1):
		averagelist[i] += doublelist[i][j + 1]
	averagelist[i] = averagelist[i] / doublelist[i][0]
	for j in range(len(doublelist[i]) - 1):
		if averagelist[i] < doublelist[i][j + 1]:
			studentRate[i] += 1
	studentRate[i] = studentRate[i] / doublelist[i][0] * 100
for i in studentRate:
	print('{i:.03f}%'.format(i = i))

