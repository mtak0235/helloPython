import sys
input = sys.stdin.readline
case = int(input())
while case:
    case-=1
    cnt = int(input())
    s  = [0 for _ in range(cnt + 1)]
    a = [0] + list(map(int, input().split()))
    for i in range(1, cnt + 1):
        s[i] = s[i - 1] + a[i]
    dp = [[0 for j in range(cnt + 1)] for i in range(cnt + 1) ] 
    for i in range(2, cnt + 1):
        for j in range(1, cnt - i + 2):
            dp[j][j + i - 1] = min([dp[j][j + k] + dp[j + k + 1][j + i - 1]for k in range(i - 1)]) + s[j + i - 1] - s[j - 1]
    print(dp[1][cnt])
