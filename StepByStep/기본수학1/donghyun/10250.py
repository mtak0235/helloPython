import sys

input = sys.stdin.readline
i = int(input())
for _ in range(i):
    h, w, n = map(int, input().split())
    print((h-(-n%h))*100-(-n//h))