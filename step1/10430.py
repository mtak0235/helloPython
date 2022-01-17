from __future__ import print_function
import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())

base = 10
tmp = B % base
while tmp != B:
    print(A * tmp)
    base *= 10
    tmp = B % base
print(A * tmp)

