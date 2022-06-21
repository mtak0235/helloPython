# 나이순 정렬
# 정렬

import sys

inp = sys.stdin.readline

N = int(inp())
A = []
for i in range(N):
    a = inp().split()
    A.append(a)

A.sort(key=lambda x: int(x[0]))    # 이미 순서대로 정렬은 되어있음

for x in A:
    print(x[0], x[1])
