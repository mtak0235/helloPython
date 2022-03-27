import sys
_hour, _min = map(int, sys.stdin.readline().split())
_work = int(sys.stdin.readline())
_min = _work + _min
_hour += (_min // 60)
_hour %= 24
_min %= 60
print(_hour, _min)
