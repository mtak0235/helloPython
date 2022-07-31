import sys

input = sys.stdin.readline
a, b = map(int, input().split())
l = list(range(b + 1))
for i in range(2, b + 1):
	if i >= a and l[i]:
		print(i)
	for j in range(2, -(-len(l)//i)):
		l[i * j] = 0