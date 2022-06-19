# 9020

import math
import sys

def checkPrimeNumber(num: int):
	allList: list = [True] * (num + 1);

	for i in range(2, int(math.sqrt(num)) + 1):
		if allList[i] == True:
			for j in range(i * 2,  num + 1, i):
				allList[j] = False;
	return allList;

iter: int = int(sys.stdin.readline());
for i in range(iter):
	n: int = int(sys.stdin.readline());
	primeList = checkPrimeNumber(n);

	for i in range(n // 2 - 1):
		left: int = n // 2 - i;
		right: int = n - left;
		if (primeList[left] and primeList[right]):
			print(left, right);
			break;

