# 11021

import sys

number = int(sys.stdin.readline())

for	i in range(0, number):
	a, b = map(int, sys.stdin.readline().split())
	if ((a > 0 and a < 10) and (b > 0 and b < 10)):
		print('Case #{index}: {res}'.format(index = i + 1, res = a + b))