# 2869

import sys


a, b, v = map(int, sys.stdin.readline().split());

day: int = 0;
day = (v - a) // (a - b);
if a - b == 1:
	print(v - a + 1)
else :
	cur_h: int = day * (a - b);
	while (cur_h < v):
		cur_h += a;
		if (cur_h < v):
			cur_h -= b;
		day += 1;
	print(day)


#n: int = 1;
#while ((a - b) * n < v):
#		n += 1;

#if ((a - b) * n == v):
#	n -= 1;
#print(n);


