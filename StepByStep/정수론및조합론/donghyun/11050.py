import sys

input = sys.stdin.readline
n, k = map(int, input().split())
a = 1
for _ in range(k):
	a *= n
	n -= 1
for i in range(k, 0 , -1):
	a //= i
print(a)