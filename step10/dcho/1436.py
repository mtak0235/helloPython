# 1436

import sys

n:int = int(sys.stdin.readline())
i: int = 666
totalCnt: int = 1
series: list = [666]

while (True):
	breakFlag: int = 0
	for j in range(len(str(i)) - 2):
		if str(i)[j] == '6' and str(i)[j + 1] == '6' and str(i)[j + 2] == '6':
			if len(series) != 0 and series[-1] != i:
				totalCnt += 1
				series.append(i)
			if totalCnt == n:
				breakFlag = 1
				break;
	if breakFlag:
		print(series[-1])
		break;
	i += 1;
