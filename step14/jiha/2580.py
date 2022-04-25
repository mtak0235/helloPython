import sys
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
graph = []
for i in range(9):
	for j in range(9):
		if arr[i][j] == 0:
			graph.append((i, j))

def veri(x, y, n)-> bool:
	# box 검사
	for l in range(3*(x//3), 3*((x//3)+1)):
		for m in range(3*(y//3), 3*((y//3)+1)):
			if arr[l][m] == n:
				return False
	# row, col 검사
	for i in range(9):
		if arr[i][y] == n or arr[x][i] == n:
			return False
	return True

def sudoku(k):
	if k == len(graph):
		for list in arr:
			print(*list)
		# return은 함수를 종료, exit는 프로세스(프로그램)를 종료
		exit(0)
	x, y = graph[k]
	for i in range(1,10):
		if veri(x, y, i):
			arr[x][y] = i
			sudoku(k+1)
			arr[x][y] = 0
sudoku(0)