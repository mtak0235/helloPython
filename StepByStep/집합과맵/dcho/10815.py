# 10815

import sys

def binary_search(arr, value):
	left, right = 0, len(arr) - 1

	while left <= right:
		mid = (left + right) // 2
		if arr[mid] == value:
			return mid
		if arr[mid] > value:
			right = mid - 1
		else:
			left = mid + 1
	return -1

n:int = sys.stdin.readline()
nlist: list = sorted(list(map(int, sys.stdin.readline().split())))

m:int = sys.stdin.readline()
mlist: list = list(map(int, sys.stdin.readline().split()))

for index, num in enumerate(mlist):
	if binary_search(nlist, num) >= 0:
		mlist[index] = 1
	else:
		mlist[index] = 0

for i in mlist:
	print(i, end=' ')
