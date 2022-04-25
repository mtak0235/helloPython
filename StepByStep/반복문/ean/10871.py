import sys

n, x = map(int, sys.stdin.readline().split())
t = map(int, sys.stdin.readline().split())

for i in t:
    if i < x:
        sys.stdout.write(f"{i} ")
