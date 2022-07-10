import sys

input = sys.stdin.readline
input()
l = list(map(int, input().split()))
s = []
ans = [-1] * len(l)
last = -1
for i, n in enumerate(l):
	if n > last:
		while s:
			if not s:
				break
			if l[s[-1]] < n:
				ans[s[-1]] = n
				s.pop()
			else:
				break
	s.append(i)
print(*ans)