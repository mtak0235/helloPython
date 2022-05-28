# 상근이의 여행
# MST

import sys

input = sys.stdin.readline

def union(par, n1, n2):
    a = par[n1]
    b = par[n2]
    if a < b:
        par[b] = a
    else:
        par[a] = b

def find(par, n):
    if par[n] == n:
        return n
    par[n] = find(par, par[n])
    return par[n]

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    par = [i for i in range(N + 1)]
    answer = 0
    for _ in range(M):
        n1, n2 = map(int, input().split())
        if find(par, n1) != find(par, n2):
            answer +=1
            union(par, n1, n2)
    print(answer)


