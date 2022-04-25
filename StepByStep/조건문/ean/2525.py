import sys

h, m = map(int, sys.stdin.readline().split())
time = int(sys.stdin.readline())

h = (h + (m + time) // 60) % 24
m = (m + time % 60) % 60
print(h, m)
