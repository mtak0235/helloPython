import sys

def threeSixExist(n):
    strN = str(n)
    i = 0
    while i < len(strN) - 2:
        if strN[i] == "6":
            if strN[i + 1] == "6" and strN[i +2] == "6":
                return True
        i+=1
    return False

_idx = int(sys.stdin.readline())
_start = 665
while _idx > 0 :
    _start+=1
    if threeSixExist(_start):
        _idx-= 1
print(_start)
