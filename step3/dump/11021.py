import sys

T = int(sys.stdin.readline())

def printCaseSum(i):
    A, B = map(int, sys.stdin.readline().split())
    print("Case #%d: %d" %(i, A + B))

for i in range(0, T):
    printCaseSum(i + 1)