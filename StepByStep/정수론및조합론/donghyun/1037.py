import sys

input = sys.stdin.readline
input()
l = list(map(int, input().split()))
print(max(l) * min(l))