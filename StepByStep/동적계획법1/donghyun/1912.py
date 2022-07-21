import sys
from functools import lru_cache

input = sys.stdin.readline
n = int(input())
l = list(map(int, input().split()))
for i in range(1, n):
	l[i] = max(l[i], l[i-1] + l[i])
print(max(l))
