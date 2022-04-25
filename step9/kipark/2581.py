#[2581] step9, 소수 kipark 재업
import sys

era = [False, False, True] + [True] * 10001

for i in range(2, 10001):
    if era[i]:
        for j in range(2*i, 10001, i):
            era[j] = False

M = int(input())
N = int(input())

result = 0
row_result = 10002
for nums in range(M, N+1):
    if era[nums] == True:
        result += nums
        row_result = nums if row_result > nums else row_result

if result > 0:
    print(result)
    print(row_result)
else:
    print(-1)
