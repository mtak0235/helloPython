# 3052

import sys

n = []
for i in range(10):
	n.append(int(sys.stdin.readline()))
	n[i] = n[i] % 42
changeN = set(n)
print(len(changeN))