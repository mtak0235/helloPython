import sys
from collections import deque
input = sys.stdin.readline
g = int(input())
for _ in range(g):
	n, m = map(int,input().split())
	a = deque(list(map(int, input().split())))
	aa = list(a)
	cnt = 0
	pos = m
	while True:
		if a[0] == max(a):
			cnt += 1
			if 0 == pos:
				print(cnt)
				break
			pos -= 1
			a.popleft()
			continue
		t = a.popleft()
		a.append(t)
		if pos != 0:
			pos -= 1
		else:
			pos += (len(a) - 1)
