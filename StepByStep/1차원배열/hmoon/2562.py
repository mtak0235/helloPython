import sys

solves = []

for i in range(0, 9):
    solves.append(int(sys.stdin.readline()))

print(max(solves))
print(int(solves.index(max(solves)) + 1))
