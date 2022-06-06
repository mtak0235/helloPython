import sys

def add(x, y):
    return x + y

if __name__ == '__main__':
    x, y = map(int, input().split())
    print (add(x, y))
