import sys

input = sys.stdin.readline
l = list(range(10000 * 2 + 1))
for i in range(2, 10000 * 2 + 1):
	for j in range(2, -(-len(l)//i)):
		l[i * j] = 0
n = int(input())
for _ in range(n):
	a = int(input())
	i = 0
	while not (l[a//2-i] and l[a//2+i]):
		i += 1
	print(a//2-i, a//2+i)