import sys

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
DP = [0] * N
DP[0] = num[0]
for i in range(1, N):
    DP[i] = DP[i - 1] + num[i]
for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    if (start == 1):
        print(DP[end - 1])
    else:
        print(DP[end - 1] - DP[start - 2])
