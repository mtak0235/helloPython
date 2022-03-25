import sys
import copy
_check = 0
_cnt = int(sys.stdin.readline())
_res = _cnt
_input = list()
_set = list()
for i in range(_cnt):
    _input.append(sys.stdin.readline().strip())
    _set.append(set(_input[i]))
for i in range(_cnt):
    _check = 0
    for c in _set[i]:
        tmp = _set[i] - set(c)
        for t in tmp:
            if t in _input[i][_input[i].index(c):_input[i].rindex(c)]:
                _res -= 1
                _check = 1
                break
        if _check == 1 : break
print(_res)
