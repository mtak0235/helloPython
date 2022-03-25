import sys
_test_cnt = int(sys.stdin.readline())
_result = [0 for i in range(_test_cnt)]
for i in range(_test_cnt):
    _added = 0
    for data in sys.stdin.readline():
        if (data == "O"):
            _result[i] += (_added + 1)
            _added += 1
        else:
            _added = 0
[print(data) for data in _result]