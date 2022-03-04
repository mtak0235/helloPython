# 4153

import sys

while True:
	point = list(map(float, sys.stdin.readline().split()))
	if any(point) == False:
		break
	maxValue = max(point)
	point.remove(maxValue)
	if maxValue ** 2 == point[0] ** 2 + point[1] ** 2:
		print("right")
	else:
		print("wrong")
