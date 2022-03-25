import sys
n, m = map(int, sys.stdin.readline().split())
_map = list()
for r in range(n):
	_map.append(list(sys.stdin.readline()))
_mod = list()
_colorSet = ['W', 'B']
for h in range(n - 7):
	for v in range(m - 7):
		_oneSetCnt = [0, 0]
		for _unitStart in range(2):
			_start = _unitStart
			for r in range(h, h + 8):
				_flag = _start
				for c in range(v, v + 8):
					if _map[r][c] != _colorSet[_flag]:
						_oneSetCnt[_unitStart] +=1
					_flag ^= 1
				_start ^= 1
		_mod.append(min(_oneSetCnt[0], _oneSetCnt[1]))

print(min(_mod))
