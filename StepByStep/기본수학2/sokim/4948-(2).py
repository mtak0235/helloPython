import math
import sys

max = 123456 # 문제에서 제한한 입력값의 최대값

array = [True for _ in range(max * 2 + 1)]
array[0], array[1] = False, False

# 에라토스테네스의 채 공식
for i in range(2, max * 2 + 1):
	if array[i] is True:
		j = 2
		while i * j <= max * 2:
			array[i * j] = False
			j += 1

while True:
	N = int(sys.stdin.readline().rstrip())
	if N == 0:
		break
	cnt = 0 # 정답
	for i in range(N + 1, 2 * N + 1):
		if array[i] is True:
			cnt += 1
	print(cnt)
