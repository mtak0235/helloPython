import sys
from collections import defaultdict
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

MAX = 1000000
dp = [0] * (MAX + 1)
sum = [0] * (MAX + 1)

for i in range(1, MAX + 1) :
	j = 1
	while i * j <= MAX:
		dp[i * j] += i
		j += 1
	sum[i] = sum[i - 1] + dp[i]

t = int(input())
for _ in range(t):
    a = int(input())
    print("%d\n" % sum[a])