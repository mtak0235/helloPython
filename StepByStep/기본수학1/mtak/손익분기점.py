import sys
import math
a,b,c = map(int, sys.stdin.readline().split())
if b >= c:
    _ret = -1
else:
	_ret = math.floor(a/(c - b)) + 1
print(_ret)