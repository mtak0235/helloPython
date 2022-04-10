# 2525

import sys


a, b = map(int, sys.stdin.readline().split())
cook: int = int(sys.stdin.readline())

res: int = a * 60 + b + cook

a = res // 60
b = res % 60
if a > 23:
	a = a - 24

print(a, b)
