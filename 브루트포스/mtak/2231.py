import sys

def sumOfseat(n):
	if n // 10 == 0:
		return n;
	return n % 10 + sumOfseat(n // 10)

_input = int(sys.stdin.readline())
_ret = 0
for i in range(1, _input):
	if i + sumOfseat(i) == _input:
		_ret = i
		break
print(_ret)