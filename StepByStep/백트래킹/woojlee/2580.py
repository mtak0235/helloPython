# 스도쿠
# 백트래킹

import sys

input = sys.stdin.readline
Map = [list(map(int, input().split())) for _ in range(9)]

target = []
for i in range(9):
    for j in range(9):
        if Map[i][j] == 0:
            target.append((i, j))

def print_Map():
    for m in Map:
        print(' '.join(list(map(str, m))))

def find_candidate(i, j):
    candi = [_ + 1 for _ in range(9)]
    for k in range(9):
        if Map[i][k] in candi:
            candi.remove(Map[i][k])
        if Map[k][j] in candi:
            candi.remove(Map[k][j])
    
    i, j = i // 3, j // 3
    for r in range(i * 3, i * 3 + 3):
        for c in range(j * 3, j * 3 + 3):
            if Map[r][c] in candi:
                candi.remove(Map[r][c])
    return candi

def dfs(L):
    if L == len(target):
        print_Map()
        sys.exit()
    i, j = target[L]
    candi = find_candidate(i, j)
    for v in candi:
        Map[i][j] = v
        dfs(L + 1)
        Map[i][j] = 0
        
dfs(0)