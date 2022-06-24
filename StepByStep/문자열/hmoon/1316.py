import sys

cnt = 0

for _ in range(int(sys.stdin.readline().strip())):
    _input = list(map(str, sys.stdin.readline().strip()))
    for i in range(len(_input) - 1):
        if _input[i] != _input [i + 1]:
            temp = _input[i + 1:]
            if _input[i] in temp:
                cnt -= 1
                break
    cnt += 1
print(cnt)
