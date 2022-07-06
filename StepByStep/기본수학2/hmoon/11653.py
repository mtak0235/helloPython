import sys

N = int(sys.stdin.readline())
i = 2

while (N != 1) :
    if N % i == 0:
        N = N / i
        print(i)
    else : i += 1
