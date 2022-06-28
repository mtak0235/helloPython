import sys

input = sys.stdin.readline
cnt = int(input())
_list = [int(input()) for _ in range(cnt)]

def bubble_sort(li, c):
	for i in range(c - 1, -1 ,-1):
		for j in range(i):
			if li[j] > li[j + 1]:
				t = li[j]
				li[j] = li[j + 1]
				li[j + 1] = t
bubble_sort(_list, cnt)
for p in _list:
	print(p)