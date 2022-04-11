# 평균
import sys

n = int(input())
num = list(map(int, sys.stdin.readline().split()))

max_num = max(num)
sum_num = 0.0
for i in range(n):
  sum_num += num[i] / max_num * 100
print(sum_num / n)