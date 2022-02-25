import sys
input = sys.stdin.readline

arr = []
n = int(input())
for _ in range(n):
    age, name = map(str, input().split())
    arr.append((int(age), name))

arr = sorted(arr, key=lambda x: x[0])

for i in arr:
    print(i[0], i[1])