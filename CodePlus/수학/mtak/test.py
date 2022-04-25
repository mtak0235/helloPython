import sys
input = sys.stdin.readline

def dfs(n):
	if n == 4:
		print("E:%d"% n)
		return 
	print("B:%d"% n)
	dfs(n + 1)
	print("A:%d"% n)

dfs(0)