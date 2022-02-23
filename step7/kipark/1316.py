import sys

N = int(input())
arr = list()
result = 0

for i in range(N):
	arr.append(input())

for i in range(N):
	for j in range(len(arr[i])):
		