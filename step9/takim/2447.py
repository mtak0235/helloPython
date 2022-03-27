n = int(input())

buffer=[[None] * (n+1) for _ in range(n)]
for i in range(n - 1):
	buffer[i][n] = "\n"
buffer[n-1][n] = ""

def recur(n, row, col, flag):
	if flag == 0:
		for i in range(row, n + row):
			for j in range(col, n + col):
				buffer[i][j] = " "
		return 
	if n == 1:
		buffer[row][col] = "*"
	else:
		for i in range(3):
			for j in range(3):
				if (i == 1 and j == 1):
					recur(n//3, row + (n//3)*i, col + (n//3)*j, 0)
				else:
					recur(n//3, row + (n//3)*i, col + (n//3)*j, 1)

recur(n, 0, 0, 1)
for i in range(n):
	print("".join(buffer[i]), end="")

