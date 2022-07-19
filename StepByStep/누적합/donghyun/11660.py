import sys

n, m = map(int, input().split())
l = [[0] * (n + 1) for _ in range(n + 1)]
x = 1
for _ in range(n):
	y = 1
	for i in map(int, input().split()):
		l[x][y] = i + l[x-1][y] + l[x][y-1] - l[x-1][y-1]
		y += 1
	x += 1
for _ in range(m):
	x1, y1, x2, y2 = map(int, input().split())
	print(l[x2][y2]-l[x1-1][y2]-l[x2][y1-1]+l[x1-1][y1-1])