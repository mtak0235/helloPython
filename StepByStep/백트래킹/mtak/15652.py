from random import randrange
import sys

n, m = map(int, sys.stdin.readline().split())
a = [i for i in range(1, n + 1)]
toPrint = list()

def printList():
    for i in toPrint:
        print(i, end=' ')
    print()

def dfs(start):
    if len(toPrint) == m:
        print(" ".join(map(str, toPrint)))
        return
    for i in range(start, n + 1):
        toPrint.append(i)
        dfs(i)
        toPrint.pop()

dfs(1)