import sys

input = sys.stdin.readline
n = int(input())
l1 = [int(input())]
for _ in range(n-1):
	l2 = list(map(int, input().split()))
	for i, j in enumerate(l2):
		if i == 0:
			l2[i] += l1[i]
		elif i == len(l2) - 1:
			l2[i] += l1[-1]
		else:
			l2[i] += max(l1[i-1], l1[i])
	l1 = l2
print(max(l1))