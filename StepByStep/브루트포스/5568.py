# 카드 놓기
# 브루트포스
# 순열

from itertools import permutations
import sys

inp = sys.stdin.readline

n = int(inp())
k = int(inp())

A = [inp().strip() for _ in range(n)]
S = set()

for x in permutations(A, k):
    s = ''.join(x)
    S.add(s)

print(len(S))
