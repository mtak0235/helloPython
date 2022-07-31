import sys
from collections import defaultdict
from functools import reduce

input = sys.stdin.readline
n = int(input())
for _ in range(n):
	m = int(input())
	d = defaultdict(int)
	for _ in range(m):
		v, k = input().strip().split()
		d[k] += 1
	print(reduce(lambda x, y: x * (y + 1), d.values(), 1) - 1)