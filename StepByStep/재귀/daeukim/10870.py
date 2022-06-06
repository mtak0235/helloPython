# 피보나치 수 5
n = int(input())
def fibo(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	return (fibo(n-1) + fibo(n-2))
print(fibo(n))