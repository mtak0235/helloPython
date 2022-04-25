import sys

a, b = sys.stdin.readline().split()

a = int(a[::-1])
b = int(b[::-1])
print(max(a, b))