from __future__ import print_function
import sys

A, B = map(int, sys.stdin.readline().split())
print(A+B, A-B, A*B, A/B, A%B, sep='\n')