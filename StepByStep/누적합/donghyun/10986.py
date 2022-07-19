import sys
from itertools import accumulate

input = sys.stdin.readline
n, m = map(int, input().split())
l = accumulate(map(int, input().split()))
c = [0] * m
ans = 0
for i in l:
	c[i % m] += 1
for v in c:
	ans += v * (v - 1) // 2
print(ans + c[0])