import sys
_input = int(sys.stdin.readline())
_ret = 1
_cnt = 1
while _cnt < _input:
    _cnt += 6 * _ret
    _ret+=1
print(_ret)
