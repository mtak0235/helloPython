import sys
_testCase = int(sys.stdin.readline())
_printList = [[1, 0], [0, 1]] + [[-1, -1] for _ in range(39)]

def fibonacci(n) :
    if _printList[n][0] == -1:
        first = fibonacci(n-1)
        second = fibonacci(n - 2)
        _printList[n][0] = first[0] + second[0]
        _printList[n][1] = first[1] + second[1]
    return _printList[n]
    
max = 2

def fibo2(max, m):
    if m >= max:
        for i in range(max, m + 1):
                _printList[i][0] = _printList[i - 1][0] + _printList[i - 2][0]
                _printList[i][1] = _printList[i - 1][1] + _printList[i - 2][1]
        max = m

def printCnt():
    _get = int(sys.stdin.readline())    
    # fibonacci(_get)
    fibo2(max, _get)
    print(_printList[_get][0], _printList[_get][1])

for _ in range(_testCase):
    printCnt()
