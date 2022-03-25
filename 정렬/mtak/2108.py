import sys

_cnt = int(sys.stdin.readline())
_4cnt = [[0, 0] for _ in range(8001)]
_get = list()
_size = 0
for _ in range(_cnt):
    tmp = int(sys.stdin.readline())
    _get.append(tmp)
    _4cnt[tmp + 4000][0] += 1
    if _4cnt[tmp + 4000][1] == 0:
        _4cnt[tmp + 4000][1] = tmp
        _size += 1
        
_ret = [0 for row in range(_cnt)]

def _merge(l, m, middle, n):
	global _ret
	i = m
	j = middle + 1
	k = m
	while (i <= middle and j <= n):
		if (l[i] < l[j]):
			_ret[k] = l[i]
			i+=1
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
_summary = 0
for j in _get:
	_summary += j
print(round(_summary / _cnt))
print(_get[len(_get) // 2])
_ret = [[0, 0] for _ in range(8001)]
_mergeSort(_4cnt, 0, len(_4cnt) - 1)
for idx, data in enumerate(_4cnt):
    if data[0] == _4cnt[-1][0]:
        if idx < 8000 and _4cnt[idx][0] == _4cnt[idx + 1][0]:
            print(_4cnt[idx + 1][1])
        else :
            print(_4cnt[idx][1])
        break
        
print((_get[0] - _get[-1]) * (-1))
