# 18870

import sys

n = int(sys.stdin.readline())
nums: list = list(map(int,sys.stdin.readline().split()))
merge = sorted(list(set(nums)))

dic: dict = {merge[i] : i for i in range(len(merge))}
for i in nums:
	print(dic[i], end=' ')
