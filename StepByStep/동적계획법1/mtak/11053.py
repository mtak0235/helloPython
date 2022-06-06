import sys
input = sys.stdin.readline
cnt = int(input())
a = list(map(int, input().split()))
dp = [0] * cnt
ret = 0
for i in range(cnt):
    h = 0
    for j in range(i):
        if (a[j] < a[i]):
            h = max(dp[j], h)
    dp[i] = h + 1
    ret = max(ret ,dp[i])
print(ret)