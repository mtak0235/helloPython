import sys

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr = sorted(arr, key=lambda x: (x[1], x[0]))

for i in arr:
    print(i[0], i[1])