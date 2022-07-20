def fib(n):
	for i in range(3, n + 1):
		fib.count += 1
		fib.dp[i] = fib.dp[i - 1] + fib.dp[i - 2]
	return fib.dp[n]
fib.count = 0

n = int(input())
fib.dp = [1] * (1 + n)
print(fib(n), fib.count)