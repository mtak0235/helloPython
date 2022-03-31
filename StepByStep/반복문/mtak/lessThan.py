import sys
(n, x) = map(int, sys.stdin.readline().split())
datas = list(map(int, sys.stdin.readline().split()))
for i in datas:
    if i < x:
        print(str(i), end=' ')
print()