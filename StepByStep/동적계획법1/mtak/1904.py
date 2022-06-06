import sys
input = sys.stdin.readline
mod = 15746
n = int(input())
dp = [0, 1, 2] + [0] * (n - 1)
for i in range(3, n + 1):
    dp[i] = (dp[i - 2] + dp[i -1]) % mod
print(dp[n])