import sys
_input = sys.stdin.readline().strip()
_convert_lst = 'c=','c-', 'dz=', 'd-','lj','nj', 's=','z='
_ret = 0
for str in _convert_lst:
    while _input.find(str) != -1:
        _input = _input[:_input.find(str)] + " " + _input[_input.find(str) + len(str):]
        _ret+=1
for i in  _input:
    if i == " ":
        continue
    _ret += 1
print(_ret)