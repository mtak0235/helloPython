import sys

N, K = map(int,sys.stdin.readline().split())
num = list(map(int,sys.stdin.readline().split()))
DP = [0] * N
MAX = sum(num[:K])
tmp = MAX
for i in range(N - K):
    tmp = tmp - num[i] + num[i + K]
    MAX = max(MAX, tmp)
print(MAX)
