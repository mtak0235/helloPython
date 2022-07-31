from itertools import product

n, m = map(int, input().split())
l = [range(1, n+1)]*m
for i in product(*l):
	print(*i)