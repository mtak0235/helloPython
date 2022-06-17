import sys
input = sys.stdin.readline
n, k = map(int, input().split())
p = 1000000007
def factorial_m(x):
	ret = 1
	for i in range(2, x + 1):
		ret = (ret * i) % p
	return ret

def square_m(b, e):
	if e == 0:
		return 1
	if e == 1:
		return b
	t = square_m(b, e // 2)
	if e % 2:
		return t * t * b % p
	else:
		return t * t % p

denominator = factorial_m(n)
numerator = factorial_m(n - k) * factorial_m(k)%p
print(denominator * square_m(numerator, p -2) % p)
