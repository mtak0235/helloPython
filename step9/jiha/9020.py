t = int(input())

def is_prime(x:int) -> bool:
	if x == 2:
		return True
	for i in range(2, int(x**(1/2)) + 1):
		if x % i == 0:
			return False
	return True

is_prime_TF = [False] * 10001
is_prime_TF[2] = True

for i in range(3, 10001):
	is_prime_TF[i] = is_prime(i)

for _ in range(t):
	n = int(input())
	for j in range(int(n/2), 1, -1):
		if is_prime_TF[j] and is_prime_TF[n - j]:
			print(j, n-j, sep=' ')
			break