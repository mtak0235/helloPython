import math

# 범위: M 이상 N 이하
M = int(input())
N = int(input())

prime = list() # 소수 리스트
for i in range(M, N + 1):
	if i == 1:
		continue
	elif i == 2 or i == 3:
		prime.append(i)
		continue
	flag = True # 소수 판별 플래그
	for j in range(2, int(math.sqrt(i)) + 1):
		if i % j == 0:
			flag = False
	if flag == True:
		prime.append(i)

if not prime:
	print(-1)
else:
	print(sum(prime))
	print(min(prime))
