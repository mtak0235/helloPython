import math

N = int(input()) # 테스트케이스 수

array = [True for _ in range(10000 + 1)] # 소수인지 판별
for i in range(10000 + 1):
	for j in range(2, int(math.sqrt(i)) + 1):
		if i % j == 0:
			array[i] = False
			break

for _ in range(N):
	num = int(input()) # 주어진 숫자
	a, b = num//2, num//2
	while a > 0:
		if array[a] and array[b]:
			print(a, b)
			break
		else:
			a -= 1
			b += 1
