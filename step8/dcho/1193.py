# 1193

import sys

x: int = int(sys.stdin.readline())
num: int = 0
cnt: int = 1

while x > num :
	num += cnt
	cnt += 1

b = x - (num - (cnt - 1))

if cnt % 2 == 0:
	print(str(cnt-b) + '/' + str(b))
else:
	print(str(b) + '/' + str(cnt-b))
