import sys

cnt = int(input())
while (cnt > 0):
	A, B = map(int, sys.stdin.readline().rstrip().split())
	print(A + B)
	cnt -= 1
