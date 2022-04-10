import sys
max = 0
idx = 0
for i in range(9):
    _get = int(sys.stdin.readline())
    if _get > max:
        max = _get
        idx = i
print("%d\n%d"%(max, idx))
