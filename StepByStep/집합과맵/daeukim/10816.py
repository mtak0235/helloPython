# 숫자카드2
import sys
input = sys.stdin.readline
import collections

n = int(input())
card = list(map(int, input().split()))
m = int(input())
board = list(map(int, input().split()))
dic = dict(collections.Counter(card))
for i in board:
  if i in dic.keys():
    print(dic[i], end=" ")
  else:
    print(0, end=" ")