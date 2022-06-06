import sys
input = sys.stdin.readline
first = int(input())
f = set(map(int, input().split()))
second = int(input())
s = list(map(int, input().split()))
for i in s:
    if i in f:
        print(1, end = " ")
    else:
        print(0, end = " ")
print()
