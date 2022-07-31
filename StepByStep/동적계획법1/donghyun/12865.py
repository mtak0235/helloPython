import sys

input = sys.stdin.readline
n, k = map(int, input().split())
dp = [[0]*(k+1) for _ in range(n+1)]
for i in range(1, n+1):
	w, v = map(int, input().split())
	for j in range(1, k+1):
		if j < w:
			dp[i][j] = dp[i-1][j]
		else:
			dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
print(dp[n][k])