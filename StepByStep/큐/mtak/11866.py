import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
target= deque([_ for _ in range(1, n + 1)])
print("<", end="")
while (len(target) != 0):
	for _ in range(k - 1):
		t = target.popleft()
		target.append(t)
	if (len(target) == 1):
		print(target.popleft(), end="")
		break
	print(target.popleft(), end =", ")
print(">")
