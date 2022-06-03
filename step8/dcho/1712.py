# 1712

import sys

a, b, c = map(int, sys.stdin.readline().split());

if (c - b) <= 0:
	print(-1);
else:
	n:int = a // (c - b);
	print(n + 1);
