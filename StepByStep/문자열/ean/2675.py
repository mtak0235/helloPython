import sys

P = int(sys.stdin.readline())
for i in range(P):
    data = sys.stdin.readline().rstrip().split()
    R = int(data[0])
    S = list(data[1])
    for c in S:
        print(c * R, end='')
    print()
