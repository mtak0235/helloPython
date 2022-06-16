# 1427

import sys

n = int(sys.stdin.readline())
list: list = []
for i in str(n):
	 list.append(i)
list.sort(reverse=True)
s = "".join(list)
print(s)
