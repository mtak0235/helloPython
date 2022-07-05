import sys
import math
input = sys.stdin.readline
case = int(input())
s  = [0] * 501
dp = [[0 for j in range(501)] for i in range(501) ] 
while case:
    case-=1
    cnt = int(input())
    a = list(map(int, input().split()))
    for i in range(1, cnt + 1):
        s[i] = s[i - 1] + a[i - 1]
    for i in range(1, cnt + 1):
        for j in range(1, cnt - i + 1):
            dp[j][i + j] = math.inf
            for k in range(j, i + j):
                dp[j][j + i] = min(dp[j][i + j], dp[j][k] + dp[k + 1][i + j] + s[i + j] - s[j - 1])
    print(dp[1][cnt])
