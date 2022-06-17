import sys

N, X = map(int, sys.stdin.readline().rstrip().split())
num = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range (0, N):
	if num[i] < X:
		print(num[i], end=' ')
