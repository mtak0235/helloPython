import sys
_size = int(sys.stdin.readline())
_candidates = list(map(int, sys.stdin.readline().split()))
_max = _candidates[0]
_min = _candidates[0]
for i in _candidates:
    if i < _min:
        _min = i
    elif i > _max:
        _max = i
    _size -= 1
    if _size == 0:
        break
print(_min, end=" ")
print(_max)