import sys

_cnt = int(sys.stdin.readline())
_get = [list(map(int, sys.stdin.readline().split())) for _ in range(_cnt)]
_ret = [ [0 for col in range(2)]for row in range(_cnt)]

def _merge(l, m, middle, n):
	global _ret
	i = m
	j = middle + 1
	k = m
	while (i <= middle and j <= n):
		if (l[i][0] < l[j][0]):
			_ret[k] = l[i]
			i+=1
		elif l[i][0] == l[j][0]:
			if l[i][1] <= l[j][1]:
				_ret[k] = l[i]
				i += 1
			else :
				_ret[k] = l[j]
				j += 1
		else :
			_ret[k] = l[j]
			j+=1
		k+=1
	if i > middle:
		while j <= n:
			_ret[k] = l[j]
			k+=1
			j += 1
	else :
		while i <= middle :
			_ret[k] = l[i]
			k+=1
			i += 1
	for t in range(m,n + 1):
		l[t] = _ret[t]

def _mergeSort(l, m, n):
	if m < n:
		middle = (m + n) // 2
		_mergeSort(l, m, middle)
		_mergeSort(l, middle + 1, n)
		_merge(l, m, middle, n)

_mergeSort(_get, 0, len(_get) - 1)
for j in range(len(_get)):
	print(_get[j][0], _get[j][1])

