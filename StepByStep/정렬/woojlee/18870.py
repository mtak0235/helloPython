# 문자열 압축
# 정렬

import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = sorted(list(set(A)))
S = dict()

for i in range(len(B)):
    if B[i] not in S:
        S[B[i]] = i

# dic 생성 방법2
# S = {B[i] : i for i in range(len(B))}

for x in A:
    print(S[x], end=' ')
