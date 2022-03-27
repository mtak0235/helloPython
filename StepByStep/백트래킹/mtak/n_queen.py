import sys

_n  = int(sys.stdin.readline())
_ways = 0
_board = [0 for _ in range(15)]

def promising(row):
    for i in range(row):
        if _board[row] == _board[i] or row - i == abs(_board[row] - _board[i]):
            return False
    return True

def queen(row):
    global _ways
    if row == _n:
        _ways += 1
        return ;
    for i in range(_n):
        _board[row] = i
        if promising(row):
            queen(row + 1)

queen(0)
print(_ways)
