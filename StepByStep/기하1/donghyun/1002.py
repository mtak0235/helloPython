n, *l = open(0).read().strip().split("\n")
for i in range(int(n)):
	x1, y1, r1, x2, y2, r2 = map(int, l[i].split())
	d = ((x1-x2)**2+(y1-y2)**2)**0.5
	if x1 == x2 and y1 == y2 and r1 == r2:
		print(-1)
	elif max(r2-r1, r1-r2) < d < r1 + r2:
		print(2)
	elif d == r1 + r2 or d == max(r2-r1, r1-r2):
		print(1)
	else:
		print(0)