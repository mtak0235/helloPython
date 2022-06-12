import sys
input = sys.stdin.readline
a , b, c = map(int, input().split())

def ff(C, n):
	if n == 1:
		return C % c
	else:
		x = ff(C, n//2)
		if n % 2 == 0:
			return x * x % c
		else:
			return x * x * C % c

def f(C, n):
	res = 1
	while n > 0:
		if n & 1:
			res *= C
		C *= C;
		n >>= 1
	return res % c

print(f(a, b))
print(ff(a, b))
