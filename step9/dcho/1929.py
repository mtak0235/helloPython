# 1929

import math
import sys

def checkPrimeNumber(num: int):
	for i in range(2, int(math.sqrt(num)) + 1):
		if num % i == 0:
			return False;
	return True;

m, n = map(int, sys.stdin.readline().split());

for i in range(m, n + 1):
	if (i < 2):
		continue;
	if checkPrimeNumber(i) == True:
		print(i);
