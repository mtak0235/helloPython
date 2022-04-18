import sys

N = int(sys.stdin.readline())
l = []

for i in range(N):
    x, y = sys.stdin.readline().split()
    l.append(f"{x}+{y}")

for s in l:
    print(eval(s))
