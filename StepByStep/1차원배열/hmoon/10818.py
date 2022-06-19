import sys

N = int(sys.stdin.readline())
solves = list(map(int, sys.stdin.readline().split()))

print(min(solves),max(solves))
