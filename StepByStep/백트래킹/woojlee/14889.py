# 스타트와 링크
# 백트래킹

from itertools import combinations
import sys

input = sys.stdin.readline
N = int(input())


Map = []
total = 0
for _ in range(N):
    li = list(map(int, input().split()))
    total += sum(li)
    Map.append(list(li))

answer = 2000
for starT in combinations(range(N), N // 2):
    star, link = 0, 0
    linkT = []
    for i in range(N):
        if i in starT:
            continue
        linkT.append(i)
    for y in combinations(starT, 2):
        star += Map[y[0]][y[1]] + Map[y[1]][y[0]]
    for y in combinations(linkT, 2):
        link += Map[y[0]][y[1]] + Map[y[1]][y[0]]
    answer = min(answer, abs(star - link))

print(answer)

