import sys

input = sys.stdin.readline
i = int(input())
for _ in range(i):
	k = int(input())
	n = int(input())
	l = list(range(1, n + 1))
	for _ in range(k):
		for i in range(n - 1):
			l[i + 1] += l[i]
	print(l[-1])