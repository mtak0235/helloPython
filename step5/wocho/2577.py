import sys

input = sys.stdin.buffer.read

a, b, c = map(int, input().split())

lst = [0] * 10

mul = a * b * c
if mul == 0:
	lst[0] += 1	
while mul != 0:
	lst[mul % 10] += 1
	mul //= 10

for i in range(len(lst)):
	lst[i] = str(lst[i])

print('\n'.join(lst))