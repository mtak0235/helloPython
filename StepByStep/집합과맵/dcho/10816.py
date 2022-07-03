# 10816

import sys
import collections

n:int = sys.stdin.readline()
nlist: list = list(map(int, sys.stdin.readline().split()))

m:int = sys.stdin.readline()
mlist: list = list(map(int, sys.stdin.readline().split()))

answer = collections.Counter(nlist)

for i in mlist:
	print(answer[i], end=' ')
