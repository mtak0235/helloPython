# 2231

import sys

n: int = int(sys.stdin.readline());
constructor: int = 0;

for i in range(1, n + 1):
	sum: int = 0;
	for j in range(len(str(i))):
		sum += int(str(i)[j]);
	if n == sum + i:
		constructor = i;
		break;

print(constructor);
