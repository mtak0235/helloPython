import sys

n = int(sys.stdin.readline())
dp = [0, 0]
for i in range(2, n + 1):
	if i % 6 == 0:
		dp.append(min(dp[i-1]+1, dp[i//2]+1, dp[i//3]+1))
	elif i % 2 == 0:
		dp.append(min(dp[i-1]+1, dp[i//2]+1))
	elif i % 3 == 0:
		dp.append(min(dp[i-1]+1, dp[i//3]+1))
	else:
		dp.append(dp[i-1]+1)
print(dp[n])