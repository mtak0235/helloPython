import sys

X = int(sys.stdin.readline())
Y = int(sys.stdin.readline())

def checkQuadrant(X, Y):
    if X < 0 and Y < 0:
        return 3
    elif X < 0 and Y > 0:
        return 2
    elif X > 0 and Y < 0:
        return 4
    else:
        return 1

print(checkQuadrant(X,Y))