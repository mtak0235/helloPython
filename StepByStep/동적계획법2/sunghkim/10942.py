import sys

N = int(sys.stdin.readline())
num = list(sys.stdin.readline().split())
M = int(sys.stdin.readline())
DP = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    DP[i][i] = 1
for i in range (N - 1):
    if num[i] == num[i + 1]:
        DP[i][i + 1] = 1
for i in range(2, N):
    for j in range(N - i):
        if num[j] == num[j + i] and DP[j + 1][j + i - 1] == 1:
            DP[j][j + i] = 1
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(DP[a - 1][b - 1])
