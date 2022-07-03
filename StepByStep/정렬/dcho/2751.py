# 2751

import sys

n = int(sys.stdin.readline())
nums: list = []
for i in range(n):
	nums.append(int(sys.stdin.readline()))

nums.sort()

for i in nums:
	print(i)
