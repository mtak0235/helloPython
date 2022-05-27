# 별 찍기 - 10
# 재귀

import sys

N = int(sys.stdin.readline())
Map = [[0] * N for _ in range(N)]

def printStar(n):
    global Map

    if n == 3:
        Map[0][:3] = Map[2][:3] = [1] * 3
        Map[1][:3] = [1, 0, 1]
        return
    
    a = n // 3
    printStar(a)    # 재귀

    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1: continue
            for k in range(a):
                Map[a * i + k][a * j:a * (j + 1)] = Map[k][:a]
    
printStar(N)

# 출력
for i in range(N):
    for j in range(N):
        if Map[i][j]:
            print('*', end='')
        else:
            print(' ', end='')
    print()