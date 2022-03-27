import sys
n = int(sys.stdin.readline())
arr = [0]*n

for i in range(n):
	arr[i] = list(map(int, sys.stdin.readline().split()))

for j in range(1, n):
	arr[j][0] = arr[j][0] + arr[j-1][0]
	arr[j][j] = arr[j][j] + arr[j-1][j-1]
	for k in range(1, j):
		arr[j][k] = max(arr[j-1][k], arr[j-1][k-1]) + arr[j][k]
print(max(arr[n-1]))