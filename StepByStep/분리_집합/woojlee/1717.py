# 집합의 표현
# 분리_집합
# 유니온 파인드

import sys
sys.setrecursionlimit(10 ** 6)  # n은 1000,000 : 최대 10^6

def union(n1, n2):
    a = find(n1)
    b = find(n2)
    if a == b: return
    if a < b:
        par[b] = a
    else:
        par[a] = b

def find(n):
    if par[n] == n:
        return n    
    p = find(par[n])
    par[n] = p
    return par[n]

inp = sys.stdin.readline
n, m = map(int, inp().split())

par = [-1] * (n + 1)
for i in range(n + 1):
    par[i] = i

for _ in range(m):
    c, n1, n2 = map(int, inp().split())
    if c == 0:
        union(n1, n2)
    else:
        if find(n1) == find(n2):
            print('YES')
        else:
            print('NO')
