import sys

input = sys.stdin.readline
l = [1 for _ in range(123456 * 2 + 1)]
for i in range(2, 123456 * 2 + 1):
	for j in range(2, -(-len(l)//i)):
		l[i * j] = 0
while a := int(input()):
	print(sum(l[a+1:2*a+1]))