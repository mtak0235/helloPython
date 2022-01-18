import sys

number = int(sys.stdin.readline())

for	i in range(0, number):
	a, b = map(int, sys.stdin.readline().split())
	print(a + b)