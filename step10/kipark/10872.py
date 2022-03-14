#[10872] step10, 팩토리얼 kipark
import sys

def factory(n):
	if(n == 1) or (n == 0):
		return (1)
	return n * factory(n-1)

n = int(input())
print(factory(n))