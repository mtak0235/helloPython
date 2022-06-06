import sys

h, m = map(int, sys.stdin.readline().split())
if m < 45:
    h = (h + 24 - 1) % 24
m = (m + 60 - 45) % 60
print(h, m)
