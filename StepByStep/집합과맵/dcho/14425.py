# 14425

import sys
n, m = map(int, sys.stdin.readline().split())
s = set([sys.stdin.readline().strip() for _ in range(n)])
cnt: int = 0
for _ in range(m):
	mStr = sys.stdin.readline().strip()
	if mStr in s:
		cnt += 1
print(cnt)
