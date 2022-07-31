import sys

input = sys.stdin.readline
_, n = map(int, input().split())
l = list(map(int, input().split()))
m = s = sum(l[:n])
for i, j in enumerate(l):
	if i >= n:
		s = s - l[i - n] + l[i]
		m = max(m, s)
print(m)