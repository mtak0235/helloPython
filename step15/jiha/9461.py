import sys

n = int(sys.stdin.readline())

arr = [0]*101
arr[1] = 1
arr[2] = 1
arr[3] = 1
arr[4] = 2
arr[5] = 2
for _ in range(n):
	x = int(sys.stdin.readline())
	if arr[x] == 0:
		for i in range(6, x+1):
			arr[i] = arr[i-1] + arr[i-5]
	print(arr[x])