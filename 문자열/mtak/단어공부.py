import sys
_input = sys.stdin.readline().strip().lower()
_biggest = 0
_ret = []
_p = _input[0]
for i in set(_input):
    if _input.count(i) > _biggest:
        _biggest = _input.count(i)
        _p = i
    _ret.append(_input.count(i))
if _ret.count(_biggest) > 1 and len(_input) > 1:
    print('?')
else:
	print(_p.upper())
