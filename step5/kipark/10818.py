import sys

T = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().split()))
number.sort()

print(number[0], number[T-1])