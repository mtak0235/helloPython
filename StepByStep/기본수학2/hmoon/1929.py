import sys

M, N = map(int, sys.stdin.readline().strip().split())

a = [False, False] + [True] * (N - 1)
primes = []

for i in range(2, N + 1):
    if a[i]:
        primes.append(i)
        for j in range(2 * i, N + 1, i):
            a[j] = False

for item in primes:
    if (item >= M):
        print(item)
