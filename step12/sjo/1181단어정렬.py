import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    arr.append(input().strip())

arr = set(arr)
arr = sorted(arr, key=lambda x:(len(x), x))

for i in arr:
    print(i)