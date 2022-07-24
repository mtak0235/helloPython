import sys
input = sys.stdin.readline
case = int(input())
dp = [[0 for _ in range(31)] for _ in range(31)]
while (case):
    case-=1
    n,m = map(int, input().split())
    for r in range(1, m + 1):
        for c in range(0, m + 1):
            if dp[r][c] != 0:
                continue
            if (r == c or c == 0):
                dp[r][c] = 1
            else:
                dp[r][c] = dp[r - 1][c -1] + dp[r - 1][c]
    print(dp[m][n])
