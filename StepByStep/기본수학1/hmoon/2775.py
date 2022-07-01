import sys

t = int(input())
for _ in range(t):
    floor = int(sys.stdin.readline())
    step = int(sys.stdin.readline())
    solve = [x for x in range(1, step + 1)]
    for i in range(floor):
        for j in range(1, step):
            solve[j] += solve[j - 1]
    print(solve[-1])
