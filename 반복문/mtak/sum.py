import sys

def accumulate(n):
    if n == 0:
        return 0
    return n + accumulate(n - 1)
sys.setrecursionlimit(10000)
n = int(input())
print(accumulate(n))