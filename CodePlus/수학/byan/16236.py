from collections import deque
from shutil import move
import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(now_x, now_y):
	visit = [[0] * size for _ in range(size)]
	distance = [[0] * size for _ in range(size)]
	visit[now_x][now_y] = 1
	eat = []
	q = deque()
	q.append([now_x, now_y])
	# q가 비어있지 않다면 루프
	while q:
		x, y = q.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0 <= nx < size and 0 <= ny < size and visit[nx][ny] == 0:
				if space[nx][ny] <= space[now_x][now_y] or space[nx][ny] == 0:
					q.append([nx, ny])
					visit[nx][ny] = 1
					distance[nx][ny] = distance[x][y] + 1
				if space[nx][ny] < space[now_x][now_y] and space[nx][ny] != 0:
					eat.append([nx, ny, distance[nx][ny]])
	# 먹을게 없으면 -1 리턴 후 종료
	if not eat:
		return -1, -1, -1
	eat.sort(key = lambda x : (x[2], x[0], x[1]))
	return eat[0][0], eat[0][1], eat[0][2]

size = int(input())
space = []
for i in range(size):
	temp_list = list(map(int, input().split()))
	space.append(temp_list)
	for j in range(size):
		if space[i][j] == 9:
			space[i][j] = 2
			start_x = i
			start_y = j

# start_xy == 상어 좌표
stack = 0
time = 0
while True:
	move_x, move_y, dist = bfs(start_x, start_y)
	if move_x == -1:
		break
	space[move_x][move_y] = space[start_x][start_y]
	space[start_x][start_y] = 0
	start_x = move_x
	start_y = move_y
	stack += 1
	if stack == space[move_x][move_y]:
		stack = 0
		space[move_x][move_y] += 1
	time += dist

print(time)