import math
import sys

M, N = map(int, sys.stdin.readline().rstrip().split()) # M 이상 N 이하

for i in range(M, N + 1):
	if i == 1:
		continue
	if i == 2 or i == 3:
		print(i)
		continue
	flag = True # 소수 판별 플래그
	for j in range(2, int(math.sqrt(i)) + 1):
		if i % j == 0:
			flag = False
			break
	if flag == True:
		print(i)
