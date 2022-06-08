# 4948

import math
import sys

def checkPrimeNumber(num: int):
	cnt: int = 0
	allList: list = [True] * (2 * num + 1);

	for i in range(2, int(math.sqrt(2 * num)) + 1):
		if allList[i] == True:
			for j in range(i * 2,  2 * num + 1, i):
				allList[j] = False;

	for i in range (num + 1, 2 * num + 1):
		if allList[i] == True:
			cnt += 1
	return cnt


while (True):
	n: int = int(sys.stdin.readline());
	if (n == 0):
		break;

	print(checkPrimeNumber(n));





