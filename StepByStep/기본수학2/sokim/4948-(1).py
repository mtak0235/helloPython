import math
import sys

def	is_prime_number(num):
	if num == 2 or num == 3:
		return True
	for i in range(2, int(math.sqrt(num)) + 1):
		if num % i == 0:
			return False
	return True

prime = list()
for i in range(2, 123456 * 2 + 1):
	if is_prime_number(i):
		prime.append(i)

while True:
	N = int(sys.stdin.readline().rstrip())
	if N == 0:
		break
	cnt = 0 # 정답
	for i in range(N + 1, 2 * N + 1):
		if i in prime:
			cnt += 1
	print(cnt)
