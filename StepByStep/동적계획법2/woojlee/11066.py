# 파일 합치기
# 동적계획법

import sys

input = sys.stdin.readline

def solve():
    N = int(input())
    A = [0] + list(map(int, input().split()))
    
    sum = [0] * (N + 1)
    for i in range(N + 1):
        sum[i] = sum[i - 1] + A[i]
    
    DP = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(2, N + 1):
        for j in range(1, N + 2 - i):
            DP[j][j+i-1] = min(DP[j][j+k] + DP[j+k+1][j+i-1] for k in range(i-1)) + sum[j+i-1] - sum[j-1]
            
    print(DP[1][N])

T = int(input())
for _ in range(T):
    solve()