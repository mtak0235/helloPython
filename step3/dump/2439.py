import sys

T = int(sys.stdin.readline())

for i in range(1, T + 1):
    str = ""
    for j in range(0, i):
        str += "*"
    print(str.rjust(T))