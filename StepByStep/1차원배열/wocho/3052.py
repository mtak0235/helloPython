import sys

input = sys.stdin.buffer.read

lst = list(map(int, input().split()))
for i in range(len(lst)):
	lst[i] = lst[i] % 42

print(len(set(lst)))