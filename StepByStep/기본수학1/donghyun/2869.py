import sys

input = sys.stdin.readline
a, b, v = map(int, input().split())
print(1-(a-v)//(a-b))