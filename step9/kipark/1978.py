#[1978] step9, 소수 찾기 kipark
import sys

era = [False, False] + [True] * 1001

for i in range(2, 1001):
    if era[i]:
        for j in range(2*i, 1001, i):
            era[j] = False

n = int(input())
ret = 0
numbers = list(map(int, sys.stdin.readline().split()))
for num in numbers:
    if era[num] == True:
        ret += 1
print(ret)