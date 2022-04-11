# X보다 작은 수
import sys

N, X = map(int, input().split())
num = list(map(int, sys.stdin.readline().split()))
result = []
for i in num:
  if i < X:
    result.append(i)
print(' '.join(map(str, result)))