import sys

input = sys.stdin.readline
n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))
c = [1] * len(l)
for i, (x, y) in enumerate(l):
    for j, (p, q) in enumerate(l):
        if p > x and q > y:
            c[i] += 1
print(*c)