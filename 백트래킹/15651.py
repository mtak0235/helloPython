#[15650] 백트랙킹, n과m (3) kipark	
import sys

N, M = map(int, input().split())
number = []

def dfs(start):
	if len(number) == M:
		for i in number:
			print(i, end=' ')
		print()
		return
	for i in range(start, N + 1):
			number.append(i)
			dfs(1)
			number.pop()
dfs(1)	