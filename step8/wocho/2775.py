import sys

input = sys.stdin.readline

N = int(input())

lst = []
for i in range(N):
	floor = int(input()) + 1
	door = int(input())

	matrix = [[0] * door for _ in range(floor)]
	for j in range(door):
		matrix[0][j] = j + 1
	
	for j in range(1, floor):
		for k in range(door):
			sum = 0
			for l in range(k + 1):
				sum += matrix[j - 1][l]
			matrix[j][k] = sum
	
	lst.append(str(matrix[floor - 1][door - 1]))

print('\n'.join(lst))