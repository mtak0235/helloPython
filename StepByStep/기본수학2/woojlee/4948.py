# 베르트랑 공준

import math
import sys

n = 123456

# 에라스토체로 소수 구해놓기
prime = [False, False] + [True] * (2 * n - 1)
for i in range(2 * n + 1):
    if prime[i] is True:
        for j in range(2, 2 * n + 1):
            if i * j > 2 * n: break
            prime[i * j] = False

while True:
    num = int(sys.stdin.readline())
    if num == 0: break
    primeNums = [i for i in range(num + 1, 2 * num + 1) if i <= 2 * n and prime[i] is True]
    print(len(primeNums))

# 빠른 방법
"""
2 ~ sqrt까지 나누어 소수의 개수를 파악하는 함수를 만든다.
2n까지의 소수의 개수 - n까지의 소수의 개수
"""