import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = set(input().split())
b = set(input().split())
ret = (a-b)|(b-a)
print(len(ret))
