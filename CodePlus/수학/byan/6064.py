import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

def num(m, n, x, y):
	while x <= m * n:
		if (x - y) % n == 0:
			return x
		x += m
	return -1

t = int(input())
for i in range(t):
	m, n, x, y = map(int, input().split())
	print(num(m, n, x, y))