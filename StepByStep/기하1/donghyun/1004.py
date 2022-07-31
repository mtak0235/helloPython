import sys

input = sys.stdin.readline
n = int(input())
for _ in range(n):
	x, y, p, q = map(int, input().split())
	c = 0
	s = int(input())
	for _ in range(s):
		u, v, r = map(int, input().split())
		if ((x-u)**2+(y-v)**2<=r**2)^((p-u)**2+(q-v)**2<=r**2):
			c += 1
	print(c)