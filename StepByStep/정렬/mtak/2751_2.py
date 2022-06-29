
import sys

input = sys.stdin.readline
cnt = int(input())
_list = [int(input()) for _ in range(cnt)]
for idx in range(1, cnt):
	key = _list[idx]
	j = idx - 1
	while j >= 0 and _list[j] >= key:
		_list[j + 1] = _list[j]
		j -= 1
	_list[j + 1] = key
for p in _list:
	print(p)