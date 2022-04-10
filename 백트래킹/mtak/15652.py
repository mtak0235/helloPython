import sys

n, m = map(int, sys.stdin.readline().split())
a = [i for i in range(1, n + 1)]
_list2Print = []
_check = [[False]*n for _ in range(m)]

def printAll():
        for i in _list2Print:
                print(i, end = " ")
        print()

def dfs(c, s):
    if c == m:
        printAll()
        return
    for i in range(s, n):
        if _check[c][i]:
                continue
        _check[c][i] = True
        _list2Print.append(a[i])
        dfs(c + 1, i)
        _list2Print.pop()
        _check[c][i] = False
        
dfs(0, 0)
