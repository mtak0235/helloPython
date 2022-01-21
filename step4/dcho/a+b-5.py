# 10952

import sys

while True:
	a, b = map(int, sys.stdin.readline().split())
	if ((a < 0 and a > 10) and (b < 0 and b > 10) or (a == 0 or b == 0)):
		break
	print(a + b)