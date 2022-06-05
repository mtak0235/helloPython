# 수 정렬하기 3
import sys

input = sys.stdin.readline
n = int(input())
num = [0] * 10001
for _ in range(n):
	num[int(input())] += 1

for i in range(10001):
	if num[i] != 0:
		for j in range(num[i]):
			print(i)