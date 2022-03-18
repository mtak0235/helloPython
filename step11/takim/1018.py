import sys

def compare(rightChess, row, col):
	dif = 0

	for colIdx in range(col, col + 8):
		if (board[row][colIdx] != rightChess[colIdx - col]):
			dif+=1
	return dif

m, n = map(int, sys.stdin.readline().rstrip().split())
board = [None] * m
rightChesses = [[(j + i) % 2 for j in range(8)]for i in range(2)]
for row in range(m):
	board[row] = list(map(lambda ch : 1 if ch=='B' else 0, list(sys.stdin.readline().rstrip())))

rowComp = [[0] * (n - 7) for _ in range(m)]
for row in range(m):
	for col in range(n - 7):
		temp = []
		temp.append(compare(rightChesses[0], row, col))
		temp.append(compare(rightChesses[1], row, col))
		rowComp[row][col] = temp

result = 1e9
for row in range(m - 7):
	for col  in range(n - 7):
		for flag in range(2):
			summation = 0
			for i in range(row, row + 8):
				summation += rowComp[i][col][(flag + i)%2]
			if summation < result:
				result = summation

print(result)