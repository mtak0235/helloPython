import sys

def _add(x, y):
    return (x + y)

def _minus(x, y):
    return (x - y)

def _multiple(x, y):
    return (x * y)

def _quotient(x, y):
    return (x // y)

def _remainder(x, y):
    return (x % y)

if __name__ == '__main__':
    x, y = map(int, input().split())
    print(_add(x, y))
    print(_minus(x, y))
    print(_multiple(x, y))
    print(_quotient(x, y))
    print(_remainder(x, y))
