import math
t = int(input())

for _ in range(t):
	x1, y1, r1, x2, y2, r2 = map(int, input().split())
	r_sq = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
	if r_sq == 0 and r1 == r2:
		print(-1)
	elif r1 + r2 == r_sq or abs(r1 - r2) == r_sq:
		print(1)
	elif (r1 + r2) > r_sq > abs(r1 - r2):
		print(2)
	else:
		print(0)