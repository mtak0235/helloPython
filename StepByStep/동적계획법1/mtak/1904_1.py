import sys
n = int(input())
dp = [0, 1, 2] + [None for _ in range(n - 2)]
for i in range(3, n + 1):
    dp[i] = (dp[i - 2] + dp[i - 1]) % 15746
print(dp[n])
