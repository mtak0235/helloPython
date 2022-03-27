#[10870] step10, 피보나치의 수5 kipark
import sys

def fibo(n):
	if(n == 1):
		return (1)
	if(n == 0):
		return (0)
	return fibo(n-1) + fibo(n-2)

n = int(input())
print(fibo(n))