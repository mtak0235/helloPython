#
#
#

import sys
from collections import deque


def bfs(_G, _V):
	q = deque()
	trace = []

	visit = [False] * 1001
	q.append(_V)
	while len(q) != 0:
		_from = q.popleft()
		if visit[_from]:
			continue
		visit[_from] = True 
		trace.append(str(_from))
		for _next in _G[_from]:
			if visit[_next]:
				continue
			q.append(_next)
	print(" ".join(trace))


def dfs(_G, _V):
	stack = deque()
	trace = []

	visit = [False] * 1001
	stack.append(_V)
	trace.append(str(_V))
	visit[_V] = True

	while len(stack) != 0:
		_from = stack[-1]
		flag = False
		for _next in _G[_from]:
			if visit[_next]:
				continue
			stack.append(_next)
			trace.append(str(_next))
			visit[_next] = True
			flag = True
			break
		if not flag:
			stack.pop()
	print(" ".join(trace))


N, M, V = map(int, sys.stdin.readline().strip().split())
visit_s = [0] * 1001

G = [list() for i in range(0, N + 1)]

for i in range(M):
	v1, v2 = map(int, sys.stdin.readline().strip().split())
	G[v1].append(v2)
	G[v2].append(v1)

for i in range(1, N + 1):
	G[i] = sorted(G[i])

dfs(G, V)
bfs(G, V)


