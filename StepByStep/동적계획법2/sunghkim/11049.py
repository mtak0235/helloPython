import sys

N = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
DP = [[0] * N for _ in range(N)]
for i in range(1, N):
    for j in range(N - i):
        DP[j][i + j] = 2 ** 32
        for k in range(i):
            DP[j][j + i] = min(DP[j][j + i], matrix[j][0] * matrix[j + k][1] * matrix[j + i][1] + DP[j + k + 1][j + i] + DP[j][k + j])
print(DP[0][-1])
