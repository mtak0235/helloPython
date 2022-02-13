# 10818

import sys

n = map(int, sys.stdin.readline().split())
onelist = [int(x) for x in input().split()]
print('{a} {b}'.format(a = min(onelist), b = max(onelist)))