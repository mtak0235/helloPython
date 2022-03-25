import sys
_input = [sys.stdin.readline().strip() for i in range(10)]
_res = 0
for i in _input:
	_res |= 2**(int(i) % 42)
cnt = 0 
for i in range(42):
	if (_res & 2**i):
		cnt += 1
print(cnt)