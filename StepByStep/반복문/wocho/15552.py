import sys

input = sys.stdin.readline

N = int(input())

lst = []
for _ in range(N):
	a, b = map(int, input().split())
	lst.append(str(a + b))

print('\n'.join(lst))