import sys
from itertools import accumulate
from operator import mul

input = sys.stdin.readline
n, k = map(int, input().split())
dp = [1]
for i in accumulate(range(1, n + 1), mul):
	dp.append(i)
print(dp[n] // dp[k] // dp[n-k] % 10007)