import sys
input = sys.stdin.readline

N = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

min_cost = float("inf")
dp = [0] * (N + 1)
for i in range(1, N):
    min_cost = min(min_cost, cost[i - 1])
    dp[i] = dp[i - 1] + dist[i - 1] * min_cost

print(dp[N - 1])
