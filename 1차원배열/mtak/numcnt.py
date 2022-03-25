import sys
_res = 1
for i in range(3):
    _res *= int(sys.stdin.readline())
_res = str(_res)
_result = []
for i in range(10):
    _result.append(0)
for i in range(10):
    for c in _res:
        if c == str(i):
            _result[i] += 1
for i in _result:
    print(i)