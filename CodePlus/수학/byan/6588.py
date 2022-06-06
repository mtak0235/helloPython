import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

arr = [True for i in range(1000001)]

for i in range(2, 1001):
	if arr[i]:
		for k in range (i + i, 1000001, i):
			arr[k] = False

while True:
	n = int(input())
	if n == 0:
		break
	for i in range(3, len(arr)):
		if arr[i] and arr[n - i]:
			print(n, "=", i, "+", n - i)
			break