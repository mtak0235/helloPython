#[15649] 백트래킹, n과 m(1) kipark
import sys
N, M = map(int, input().split())
visited = [False] * N
number = []

def dfs(depth, N, M):
	if depth == M:
		for i in number:
			print(i, end=' ')
		print()
		return
	for i in range(len(visited)):
		if(visited[i] == False):
			visited[i] = True
			number.append(i+1)
			dfs(depth+1, N, M)
			visited[i] = False
			number.pop()
dfs(0, N, M)	
