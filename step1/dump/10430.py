from __future__ import print_function
import sys

A, B, C = map(int, sys.stdin.readline().split())
print((A+B)%C, ((A%C)+(B%C))%C, (A*B)%C, ((A%C)*(B%C))%C, sep='\n')