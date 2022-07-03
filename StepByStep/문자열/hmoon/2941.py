import sys

find = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
_input = sys.stdin.readline().strip()
cnt = 0

for item in find:
    temp = _input.count(item)
    cnt += temp
    _input = _input.replace(item, " ", temp)
for c in _input:
    if c == " ":
        _input = _input.replace(" ", "")
print(len(_input) + cnt)
