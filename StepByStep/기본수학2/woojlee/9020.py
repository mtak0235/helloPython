# 골드바흐의 추측
# 소수, 에라스토체, 정수론

import sys

input = sys.stdin.readline    

T = int(input())
N = []  # n을 담을 배열

for _ in range(T):
    N.append(int(input()))

m = max(N)

# 가장 큰 값으로 에라스토체
isPrime = [False, False] + [True] * (m - 1) # m >= 4
for n in range(2, int(m ** 0.5) + 1):
    if isPrime[n] is True:
        for i in range(2, m + 1):
            if i * n > m: break
            isPrime[i * n] = False

for n in N:
    n1, n2 = n // 2, n // 2
    while(isPrime[n1] is False or isPrime[n2] is False):
        n1 -= 1
        n2 += 1
    print(n1, n2)
