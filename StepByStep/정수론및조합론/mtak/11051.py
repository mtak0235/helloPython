import sys
input = sys.stdin.readline
n, k = map(int, input().split())
p = 10007
res = 1
dp = [[0 for _ in range(1001)] for __ in range(1001)]
for r in range(1, n + 1):
    for c in range(0, n + 1):
        if r == c or c == 0:
            dp[r][c] = 1
        else:
            dp[r][c] = (dp[r - 1][c - 1] + dp[r - 1][c]) % p
print(dp[r][k])