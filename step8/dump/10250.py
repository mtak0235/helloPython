#[10250] step8, ACM 호텔 kipark
import sys
import math
import string

t = int(input())
for i in range(t):
	h, w, n = map(int, input().split())
	xx_str = str(math.ceil((n/h))).zfill(2)
	yy_str = str(h) if (n % h) == 0 else str(n % h)
	print(yy_str+xx_str)
