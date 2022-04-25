# 2941

import sys

croatia: list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

alpha: str = sys.stdin.readline().strip()

for i in croatia:
	alpha = alpha.replace(i, '*')

print(len(alpha))
