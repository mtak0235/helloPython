import sys
_Max = 0
_av = 0

_subject_cnt = int(sys.stdin.readline())
_scores = list(map(int, sys.stdin.readline().split()))
for i in _scores:
    if _Max < i:
        _Max = i
for i in _scores:
    _av += i / _Max * 100
_av /= _subject_cnt
print(_av)
