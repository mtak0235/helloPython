import sys

input = sys.stdin.readline
n = int(input())
l = [int(input()) for _ in range(n)]
if len(l) < 3:
	print(sum(l))
else:
	dp = [0] * n
	dp[0], dp[1], dp[2] = l[0], l[0]+l[1], max(l[0]+l[2], l[1]+l[2])
	for i in range(3, n):
		dp[i] = max(dp[i-3]+l[i-1]+l[i], dp[i-2]+l[i])
	print(dp[-1])