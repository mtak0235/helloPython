import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())

lst = [0] * 10001
for _ in range(N):
    lst[int(input())] += 1

for i in range(1, 10001):
    for _ in range(lst[i]):
        print("%d\n" %i)
