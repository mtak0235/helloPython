import sys
input = sys.stdin.readline
side = int(input())
m = [list(map(int, list(input().rstrip())))for _ in range(side)]

def divide(x, y, N):
    global m
    nt = m[x][y]
    isBundle = True
    for i in range(x, x + N):
        for j in range(y, y + N):
            if m[i][j] != nt:
                isBundle = False
                break
        if isBundle == False:
            break
    if isBundle:
        print(nt, end='')
        return
    print("(", end='')
    divide(x, y, N//2)
    divide(x, y + N//2, N//2)
    divide(x + N//2, y, N//2)
    divide(x + N//2, y + N//2, N//2)
    print(")", end='')
	
divide(0, 0, side)
