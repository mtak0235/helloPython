import sys

n, m = map(int, sys.stdin.readline().split())
visited = [False] * n
list2print = list()
a = [i for i in range(1, n + 1)]
cnt = 0

def printList():
    for i in list2print:
        print(i, end=' ')
    print("")

def dfs(c):
    if c == m:
        printList()
        return
    for i in range(n):
        if visited[i]:
            continue
        if list2print and a[i] < max(list2print):
            continue
        visited[i] = True
        list2print.append(a[i])
        dfs(c + 1)
        list2print.pop()
        visited[i] = False

dfs(0)