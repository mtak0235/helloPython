import sys
input = sys.stdin.readline

board = []
for _ in range(9):
    board.append(list(map(int, input().split())))

row = [[True] * 10 for _ in range(9)]
col = [[True] * 10 for _ in range(9)]
square = [[True] * 10 for _ in range(9)]
zero = []

for i in range(9):
    for j in range(9):
        row[i][board[i][j]] = False
        col[i][board[j][i]] = False
        square[3 * (i // 3) + j // 3][board[i][j]] = False
        if board[i][j] == 0:
            zero.append((i, j))


def visit(i, r, c, s):
    board[r][c] = i
    row[r][i] = False
    col[c][i] = False
    square[s][i] = False


def unvisit(i, r, c, s):
    board[r][c] = 0
    row[r][i] = True
    col[c][i] = True
    square[s][i] = True


def recur(idx):
    if idx == len(zero):
        for i in range(9):
            print(*board[i])
        return True
    point = zero[idx]
    r = point[0]
    c = point[1]
    s = 3 * (r // 3) + c // 3
    for i in range(1, 10):
        if row[r][i] and col[c][i] and square[s][i]:
            visit(i, r, c, s)
            if recur(idx + 1):
                return True
            unvisit(i, r, c, s)
    return False


recur(0)
