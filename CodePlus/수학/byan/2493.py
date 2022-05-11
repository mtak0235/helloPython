import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

n = int(input())
s = []
ans = [0] * n
tower = list(map(int, input().split()))
for i in range(n):
	t = tower[i]
	while s and tower[s[-1]] < t:
		s.pop()
	if s:
		ans[i] = s[-1] + 1
	s.append(i)

print(" ".join(map(str, ans)))