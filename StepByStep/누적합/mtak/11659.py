import sys
input = sys.stdin.readline

c,cc = map(int, input().split()) 
l = list(map(int, input().split()))
dp = [0] * (c + 1)
for _ in range(c):
    dp[_+ 1] = dp[_] + l[_]
for _ in range(cc):
    a,b = map(int, input().split())
    print(dp[b] - dp[a - 1])
