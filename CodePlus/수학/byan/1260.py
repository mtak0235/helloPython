import sys
from collections import deque
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

n, m, v = map(int, input().split())
visit_dfs = [0] * (n + 1)
visit_bfs = [0] * (n + 1)
array = [[0] * (n + 1) for _ in range(n + 1)]

def dfs(togo):
	visit_dfs[togo] = 1
	print(togo, end = " ")
	for i in range(1, n + 1):
		if visit_dfs[i] == 0 and array[togo][i] == 1:
			dfs(i)

def bfs(togo):
	q = deque()
	q.append(togo)
	visit_bfs[togo] = 1
	while q:
		togo = q.popleft()
		print(togo, end = " ")
		for i in range(1, n + 1):
			if visit_bfs[i] == 0 and array[togo][i] == 1:
				q.append(i)
				visit_bfs[i] = 1

for _ in range(m):
	temp1, temp2 = map(int, input().split())
	array[temp1][temp2] = 1
	array[temp2][temp1] = 1

dfs(v)
print()
bfs(v)
