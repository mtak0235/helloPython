# 1 ---------------------------------------------
from re import I


t = int(input())
r = []
s = []

for i in range(t):
    x, y = input().split()
    r.append(x)
    s.append(y)

for i in range(t):
    for c in s[i]:
        for _ in range(int(r[i])):
            print(c, end='')
    print("")

