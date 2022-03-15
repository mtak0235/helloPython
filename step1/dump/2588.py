from __future__ import print_function
import sys

A = int(sys.stdin.readline())
B = sys.stdin.readline()
print(A*int(B[2]), A*int(B[1]), A*int(B[0]), A*int(B), sep='\n')