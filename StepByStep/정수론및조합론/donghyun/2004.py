import sys

input = sys.stdin.readline
n, m = map(int, input().split())
def count(num, factor):
	c = 0
	divider = factor
	while (quote := num // divider):
		if not quote:
			break
		c += quote
		divider *= factor 
	return c
t = count(n, 2) - count(m, 2) - count(n - m, 2)
f = count(n, 5) - count(m, 5) - count(n - m, 5)
print(min(t, f))