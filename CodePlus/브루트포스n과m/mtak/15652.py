import sys
input = sys.stdin.readline
n, m = map(int, input().split())
toPrint = list()
a = list(map(int, input().split()))
a.sort()

def printList():
    for i in toPrint:
        print(i, end=' ')
    print()
    
def dfs(p):
    if p == m:
        printList()
        return
    for i in a:
        if i in toPrint:
            continue
        toPrint.append(i)
        dfs(p + 1)
        toPrint.pop()

dfs(0)
