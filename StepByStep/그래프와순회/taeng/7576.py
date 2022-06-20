#
#
#

import sys
from collections import deque


def bfs(N:int, M:int, zero_cnt: int, Map: list, visit: list, q: deque) -> int:
	turn = 0
	dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
	while len(q) > 0:
		turn += 1
		size = len(q)
		for _ in (rg := range(size)):
			n, m = q.popleft()
			for dir_n, dir_m in dirs:
				next_n, next_m = n + dir_n, m + dir_m
				if next_n < 0 or next_n >= N or next_m < 0 or next_m >= M:
					continue
				if Map[next_n][next_m] != 0:
					continue
				if visit[next_n][next_m] == 1:
					continue
				zero_cnt -= 1
				if zero_cnt == 0:
					return turn
				visit[next_n][next_m] = True
				Map[next_n][next_m] = 1
				q.append((next_n, next_m))

	return -1


def solve():
	M, N = map(int, sys.stdin.readline().strip().split())
	Map = [[] for j in range(N + 1)]
	visit = [[False for i in range(M + 1)] for j in range(N + 1)]
	q = deque()
	zero_cnt = 0
	for n in range(N):
		Map[n] = list(map(int, sys.stdin.readline().strip().split()))
		for m in range(M):
			if Map[n][m] == 1:
				visit[n][m] = True
				q.append((n, m))
			elif Map[n][m] == 0:
				zero_cnt += 1
	if zero_cnt == 0:
		print(0)
	else:
		print(bfs(N, M, zero_cnt, Map, visit, q))


if __name__ == "__main__":
	solve()

