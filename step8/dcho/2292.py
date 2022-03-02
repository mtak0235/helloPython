# 2292

import sys

n: int = int(sys.stdin.readline())
nums:int = 1
cnt: int = 1
while n > nums :
	nums += 6 * cnt
	cnt += 1
print(cnt)
