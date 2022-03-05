# 11653

import sys

n = int(sys.stdin.readline())

if n != 1:
	while n != 1:
		for i in range(2, n + 1):
			tuple_val = divmod(n , i)
			if tuple_val[1] ==  0:
				n = tuple_val[0]
				print(i)
				break
