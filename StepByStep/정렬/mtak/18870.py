from heapq import heapify
import sys
import copy

input = sys.stdin.readline
num = int(input())
origin = list(map(int, input().split()))
sorted = copy.deepcopy(origin)
rankingMap = {}

for i in range(1, num):
    c = i
    while True:
        root = (c - 1)//2
        if sorted[root] < sorted[c]:
            sorted[root], sorted[c] = sorted[c], sorted[root]
        c = root
        if c == 0: break

for i in range(num - 1, -1, -1):
    sorted[0], sorted[i] = sorted[i], sorted[0]
    root = 0
    c = 1
    while True:
        c =2*root + 1
        if c < i - 1 and sorted[c] < sorted[c + 1]:
            c+=1
        if c < i and sorted[root] < sorted[c]:
            sorted[root], sorted[c] = sorted[c], sorted[root]
        root = c
        if c >= i: break

rank = 0
for i in sorted:
    if i not in rankingMap.keys():
        rankingMap[i] = rank
        rank += 1
for i in origin:
    print(rankingMap[i], end=" ")
