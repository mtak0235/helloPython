# 참외밭
k = int(input())
board = [list(map(int, input().split())) for _ in range(6)]
w = 0
h = 0
for i in range(len(board)):
  di = board[i][0]
  if di == 1 or di == 2:
    if w < board[i][1]:
      w = board[i][1]
      w_idx = i
  elif di == 3 or di == 4:
    if h < board[i][1]:
      h = board[i][1]
      h_idx = i
mini_w = abs(board[(w_idx-1) % 6][1] - board[(w_idx+1) % 6][1])
mini_h = abs(board[(h_idx-1) % 6][1] - board[(h_idx+1) % 6][1])
print(((w*h)-(mini_w*mini_h)) * k)

