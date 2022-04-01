N = int(input())

def fibo(n):
	if n <= 1:
		return n
	if n not in memo:
		memo[n] = fibo(n - 1) + fibo(n - 2)
	return memo[n]

memo = dict()
print(fibo(N))