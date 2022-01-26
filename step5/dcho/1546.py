# 1546

import sys

n = int(sys.stdin.readline())
onelist = list(map(float, sys.stdin.readline().split()))
maxValue = max(onelist)
for index, value in enumerate(onelist):
	onelist[index] = value / maxValue * 100
print(sum(onelist) / n)
