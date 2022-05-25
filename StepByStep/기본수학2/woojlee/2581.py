# 소수
# 에라스토체

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

A = [True] * (10000 + 1)
A[1] = False
for i in range(10000 + 1):
    if A[i] is True:
        for j in range(2, 10000 + 1):
            if i * j > 10000: break
            A[i * j] = False

# 확인
sum, m = 0, 10000 + 1
for i in range(N, M + 1):
    if A[i] is True:
        sum += i
        m = min(m, i)

if m == 10000 + 1:
    print(-1)
else:
    print(sum)
    print(m)