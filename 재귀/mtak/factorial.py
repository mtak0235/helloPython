import sys

def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n

_input = int(sys.stdin.readline())
print(factorial(_input))
