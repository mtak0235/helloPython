import sys
def bubbleSort(l):
    for edge in range(len(l) - 1, 0, -1):
        for idx in range(edge):
            if l[idx] < l[idx + 1]:
                tmp = l[idx]
                l[idx] = l[idx + 1]
                l[idx + 1] = tmp
    return l

_list = [int(i) for i in sys.stdin.readline().strip()]
_list = bubbleSort(_list)
for i in _list:
    print(i, end ="")
