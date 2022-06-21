# N과 M(4)
# 백트래킹

from itertools import combinations_with_replacement
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = []

def dfs(L, now):
    if L == M:
        print(' '.join(map(str, A)))
        return
    else:
        for i in range(now, N + 1):
            A.append(i)
            dfs(L + 1, i)
            A.pop()

dfs(0, 1)

# 축약 풀이: combinations_with_replacement
N, M = map(int, input().split())
print("\n".join(map(" ".join, combinations_with_replacement(map(str, range(1, N+1)), M))))