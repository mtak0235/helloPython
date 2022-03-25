import sys

_cnt = int(sys.stdin.readline())
_list = [0] * 10001
for i in range(_cnt):
    _get = int(sys.stdin.readline())
    _list [_get- 1] += 1
for i in range(10001):
    if _list[i]:
        for j in range(_list[i]):
            sys.stdout.write(str(i + 1) + "\n")