import sys

N = int(sys.stdin.readline())
number = [list(map(int,x.split())) for x in sys.stdin]
DP = [[0 for _ in range(x)] for x in range(1, N + 1)]
MAX = number[0][0]
DP[0][0] = number[0][0]
for i in range(1, N):
    tmp = -1
    for j in range(i + 1):
        if (j == 0):
            DP[i][j] = number[i][j] + DP[i - 1][j]
        elif (j == i):
            DP[i][j] = number[i][j] + DP[i - 1][j - 1]
        else:
            DP[i][j] = number[i][j] + max(DP[i - 1][j], DP[i - 1][j - 1])
        tmp = max(tmp, DP[i][j])
    MAX = tmp;
print(MAX)
