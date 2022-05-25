# 소수 찾기
# 에라스토체 방법

import sys

input = sys.stdin.readline

N = int(input())
A = map(int, input().split())

primeNum = [True] * (1000 + 1)  # 1000 이하의 자연수까지만 판단
primeNum[1] = False # 1은 소수가 아님

for n in range(1000 + 1):
    if primeNum[n] is True:
        for i in range(2, 1000 + 1):
            if i * n > 1000: break
            primeNum[i * n] = False # 소수의 배수는 소수가 아님

# 확인
answer = 0
for a in A:
    if primeNum[a] is True: answer += 1
print(answer)