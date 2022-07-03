# 5a + 3b = N

import sys

def solve(N, temp):
    for i in range(1, (N // 3) + 1):
        j = 0
        for j in range(0, (N // 5) + 1):
            temp = (i * 3) + (j * 5)
            if (N == temp):
                return (i + j)
    return (-1)


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    temp = 0
    if (N % 5 == 0):
        print(N // 5)
    else:
        print(solve(N, temp))

