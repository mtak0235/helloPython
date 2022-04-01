import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coin = list()
for _ in range(N):
    coin.append(int(input()))

count = 0
for i in range(N - 1, -1, -1):
    if K >= coin[i]:
        count += K // coin[i]
        K -= (K // coin[i]) * coin[i]
    if K == 0:
        break

print(count)
