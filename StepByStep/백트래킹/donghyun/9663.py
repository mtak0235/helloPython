n = int(input())

def check(i, j):
	for x in range(i):
		if dfs.b[x][j] == 1:
			return False
		if j - (1+x) >= 0 and dfs.b[i-(1+x)][j-(1+x)]:
			return False
		if j + (1+x) < n and dfs.b[i-(1+x)][j+(1+x)]:
			return False
	return True

def dfs(i):
	if i == n:
		dfs.c += 1
		return
	for j in range(n):
		if not dfs.a[j] and check(i ,j):
			dfs.b[i][j] = dfs.a[j] = 1
			dfs(i + 1)
			dfs.b[i][j] = dfs.a[j] = 0

dfs.a = [0]*n
dfs.b = [[0]*n for i in range(n)]
dfs.c = 0
dfs(0)
print(dfs.c)