import sys

input = sys.stdin.readline
cnt = int(input())
_list = [int(input()) for _ in range(cnt)]
s = [0] *cnt

def merge(li, l, mid, r):
	global s
	i = l # 앞 리스트 일짱
	j = mid +1 # 뒤 리스트 일짱
	k = l # 타겟 일짱
	while i <= mid and j <= r:
		if li[i] <= li[j]:
			s[k] = li[i]
			i += 1
		else:
			s[k] = li[j]
			j += 1
		k += 1
	if i > mid:
		for t in range(j, r + 1):
			s[k] = li[t]
			k += 1
	else:
		for t in range(i, mid + 1):
			s[k] = li[t]
			k += 1
	for t in range(l, r + 1):
		li[t] = s[t]

def merge_sort(li, l, r):
	mid = 0
	if (l < r):
		mid = (l + r) // 2 #분힐
		merge_sort(li, l, mid) #앞쪽 정복
		merge_sort(li, mid +1, r) # 뒤쪽 정복
		merge(li, l, mid, r) # 두 정렬 병힙

merge_sort(_list, 0, cnt - 1)
for p in _list:
	print(p)

