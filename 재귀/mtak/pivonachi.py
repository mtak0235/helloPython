import sys

def pivonachi(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return pivonachi(n - 2) + pivonachi(n - 1)

_input = int(sys.stdin.readline())
print(pivonachi(_input))
