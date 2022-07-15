import sys

input = sys.stdin.readline
n = int(input())
def count(num, factor):
	c = 0
	divider = factor
	while (quote := num // divider):
		if not quote:
			break
		c += quote
		divider *= factor 
	return c
t, f = count(n, 2), count(n, 5)
print(min(t, f))