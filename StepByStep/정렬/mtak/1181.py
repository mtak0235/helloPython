import sys
def _merge(l, m, middle, n):
    global _ret
    i = m
    j = middle + 1
    k = m
    while i <= middle and j <= n:
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
        middle = (m + n)//2
        _mergeSort(l, m, middle)
        _mergeSort(l, middle + 1, n)
        _merge(l, m, middle, n)

_cnt = int(sys.stdin.readline())
_list = list()
_ret = [ [0 for col in range(2)]for row in range(_cnt)]
for _ in range(_cnt):
    _get = sys.stdin.readline().strip()
    _list.append([len(_get), _get])
_mergeSort(_list, 0, len(_list) - 1)
for idx, i in enumerate(_list):
    if idx != _cnt - 1 and i[1] != _list[idx + 1][1]:
        print(i[1])
print(_list[_cnt - 1][1])