import sys

input = sys.stdin.buffer.read

lst = list(map(int, input().split()))

mi = 1
m = lst[0]
for i in range(1, len(lst)):
	if lst[i] > m:
		m = lst[i]
		mi = i + 1

print("{0}\n{1}".format(m, mi))