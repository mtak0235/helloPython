# 스도쿠

board = [list(map(int, input().split())) for _ in range(9)]
blank = []
for i in range(9):
  for j in range(9):
    if board[i][j] == 0:
      blank.append((i, j))

def candidating(x, y):
  numbers = [i+1 for i in range(9)]
  for j in range(9):
    if board[x][j] in numbers:
      numbers.remove(board[x][j])
    if board[j][y] in numbers:
      numbers.remove(board[j][y])
  x = x//3
  y = y//3
  for i in range(x*3, (x+1)*3):
    for j in range(x*3, (x+1)*3):
      if board[i][j] in numbers:
        numbers.remove(board[i][j])
  return numbers

def dfs(cnt):
  if cnt == len(blank):
    for row in board:
      print(*row)
    return
  (i, j) = blank[cnt]
  candi = candidating(i, j)
  for num in candi:
    board[i][j] = num
    dfs(cnt+1)
    board[i][j] = 0

dfs(0)