# 동전 0
# 그리디 알고리즘

import sys

input = sys.stdin.readline
N, K = map(int, input().split())


coin = []
MaxIdx = -1
for i in range(N):
    c = int(input())
    coin.append(c)
    if c <= K:
        MaxIdx = i 

answer = 0
while K:
    mod = K // coin[MaxIdx]
    K -= mod * coin[MaxIdx]
    MaxIdx -= 1
    answer += mod
print(answer)