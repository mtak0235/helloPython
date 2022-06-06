import sys
from collections import deque
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

m, n, h = map(int, input().split())
visit = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
box = [[]for _ in range(h)]
q = deque()
max_num = -1
check = 0

def bfs():
	while q:
		a, b, c = q.popleft()
		for i in range(6):
			x = a + dx[i]
			y = b + dy[i]
			z = c + dz[i]
			if (0 <= x < n and 0 <= y < m and 0 <= z < h 
			and box[z][x][y] == 0 and visit[z][x][y] == 0):
				q.append([x, y, z])
				box[z][x][y] = box[c][a][b] + 1
				visit[z][x][y] = 1

for i in range(h):
	for j in range(n):
		box[i].append(list(map(int, input().split())))

for z in range(h):
	for x in range(n):
		for y in range(m):
			if box[z][x][y] == 1:
				q.append([x, y, z])

bfs()

for z in range(h):
	for x in range(n):
		for y in range(m):
			max_num = max(max_num, box[z][x][y])
			if box[z][x][y] == 0:
				check = 1

if check == 1:
	print(-1)
elif max_num == -1:
	print(0)
else:
	print(max_num - 1)