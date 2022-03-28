import sys

input = sys.stdin.readline

N = int(input())

lst = []
for i in range(N):
	h, w, n = map(int, input().split())
	lst.append(str((((n - 1) % h) + 1) * 100 + (n - 1) // h + 1))

print('\n'.join(lst))