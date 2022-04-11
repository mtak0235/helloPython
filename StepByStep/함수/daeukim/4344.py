# 평균은 넘겠지
import sys

n = int(input())
for i in range(n):
  s_list = list(map(int, sys.stdin.readline().split()))
  s_num = s_list.pop(0)
  s_mean = sum(s_list) / s_num
  cnt = 0
  for j in range(s_num):
    if s_list[j] > s_mean:
      cnt += 1
  print("{:.3f}%".format(cnt / s_num * 100))