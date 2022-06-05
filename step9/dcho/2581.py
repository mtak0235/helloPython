# 3009

import sys

primelist: list = []

m = int(sys.stdin.readline());
n = int(sys.stdin.readline());

for i in range(m, n + 1):
	if (i < 2):
		continue;
	cnt: int = 0;
	for j in range(2, i // 2 + 1):
		if (j * j > i):
			break;
		if (i % j == 0):
			cnt += 1;
	if (cnt == 0):
		primelist.append(i);

if (len(primelist) == 0):
	print(-1);
else:
	print(sum(primelist));
	print(primelist[0]);

