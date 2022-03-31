import sys

n, m = map(int, sys.stdin.readline().split())
a = [i for i in range(1, n + 1)]
toPrint = list()
check = [0] * m

def printList():
    for i in toPrint:
        print(i, end=' ')
    print()

def dfs(circle):
    if circle == m:
        printList()
        return
    for i in a:
        toPrint.append(i)
        dfs(circle + 1)
        toPrint.pop()

dfs(0)