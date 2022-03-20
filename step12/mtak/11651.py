import sys
from webbrowser import get

_cnt = int(sys.stdin.readline())
_get = [list(map(int, sys.stdin.readline().split())) for _ in range(_cnt)]

for i in range(1, _cnt):
    c = i
    while c != 0:
        root = (c - 1) // 2
        if _get[root][1] < _get[c][1] or (_get[root][1] == _get[c][1] and _get[root][0] < _get[c][0]):
            tmp = _get[root]
            _get[root] = _get[c]
            _get[c] = tmp
        c = root

for j in range(_cnt - 1, -1, -1):
    tmp = _get[0]
    _get[0] = _get[j]
    _get[j] = tmp
    root = 0
    c = 1
    while (c < j):
        if (_get[c][1] < _get[c + 1][1] or (_get[c][1] == _get[c + 1][1] and _get[c][0] < _get[c + 1][0])) and c < j - 1:
            c += 1
        if (_get[root][1] < _get[c][1] or (_get[root][1] == _get[c][1] and _get[root][0] < _get[c][0])) and c < j :
            tmp = _get[root]
            _get[root] = _get[c]
            _get[c] = tmp
        root = c
        c = 2 * root + 1

for i in range(_cnt):
    print(_get[i][0], _get[i][1])