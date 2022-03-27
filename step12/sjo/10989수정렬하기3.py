import sys

n = int(input())
arr = [0] * 10000001

for _ in range(n):
    arr[int(sys.stdin.readline())] += 1

for i in range(10000001):
    for _ in range(arr[i]):
        print(i)