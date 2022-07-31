import sys

input = sys.stdin.readline

def check(x, y, n):
	xx, yy = x//3*3, y//3*3
	k = 0
	for i in range(3):
		for j in range(3):
			if dfs.board[x][k] == n or dfs.board[k][y] == n:
				return False
			k += 1
			if dfs.board[xx+i][yy+j] == n:
				return False
	return True

def dfs(i):
	if i == len(dfs.q):
		for i in range(9):
			print(*dfs.board[i])
		exit(0)
	for j in range(1, 10):
		x, y = dfs.q[i]
		if check(x, y, j):
			dfs.board[x][y] = j
			dfs(i+1)
			dfs.board[x][y] = 0

dfs.board = [list(map(int, input().split())) for _ in range(9)]
dfs.q = [(i,j) for i in range(9) for j in range(9) if dfs.board[i][j]==0]
dfs(0)