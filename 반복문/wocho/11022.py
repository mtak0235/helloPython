import sys

input = sys.stdin.readline

N = int(input())

lst = []
for i in range(N):
	a, b = map(int, input().split())
	lst.append(f'Case #{i + 1}: {a} + {b} = {a + b}')
print('\n'.join(lst))