import sys

def hanoi(n, f, t, s):
    if n == 1:
        print(f, t)
        return ;
    hanoi(n - 1, f, s, t)
    print(f, t)
    hanoi(n - 1 , s, t, f)

_plateCnt = int(sys.stdin.readline())
print(2 ** _plateCnt - 1)
hanoi(_plateCnt, 1, 3, 2)
