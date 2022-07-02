import sys

for _ in range(int(sys.stdin.readline())):
    H, W, N = map(int, sys.stdin.readline().strip().split())
    f = N % H
    l = (N // H) + 1
    if f == 0:
        f = H
        l -= 1
    print(f * 100 + l)
