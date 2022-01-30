import sys
_cnt = int(sys.stdin.readline())
while _cnt:
    _cnt -= 1
    _n, _str = map(str,sys.stdin.readline().split(" "))
    for i in range(len(_str) - 1):
        for j in range(int(_n)):
            print(_str[i], end='')
    print("")
