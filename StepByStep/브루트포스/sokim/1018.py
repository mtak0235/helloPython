def	start_from_white(board) :
	cnt = 0
	# 짝수 행(0, 2, ...) 검사
	for i in range(0, 8, 2) :
		# 짝수 열(0, 2, ...) 검사
		for j in range(0, 8, 2) :
			if board[i][j] != 'W' :
				cnt += 1
		# 홀수 열(1, 3, ...) 검사
		for j in range(1, 8, 2) :
			if board[i][j] != 'B' :
				cnt += 1
	# 홀수 행(1, 3, ...) 검사
	for i in range(1, 8, 2) :
		# 짝수 열(0, 2, ...) 검사
		for j in range(0, 8, 2) :
			if board[i][j] != 'B' :
				cnt += 1
		# 홀수 열(1, 3, ...) 검사
		for j in range(1, 8, 2) :
			if board[i][j] != 'W' :
				cnt += 1
	return cnt

def	start_from_black(board) :
	cnt = 0
	# 짝수 행(0, 2, ...) 검사
	for i in range(0, 8, 2) :
		# 짝수 열(0, 2, ...) 검사
		for j in range(0, 8, 2) :
			if board[i][j] != 'B' :
				cnt += 1
		# 홀수 열(1, 3, ...) 검사
		for j in range(1, 8, 2) :
			if board[i][j] != 'W' :
				cnt += 1
	# 홀수 행(1, 3, ...) 검사
	for i in range(1, 8, 2) :
		# 짝수 열(0, 2, ...) 검사
		for j in range(0, 8, 2) :
			if board[i][j] != 'W' :
				cnt += 1
		# 홀수 열(1, 3, ...) 검사
		for j in range(1, 8, 2) :
			if board[i][j] != 'B' :
				cnt += 1
	return cnt

# 체스판의 행의 개수, 열의 개수
N, M = map(int, input().split())

# 체스판
board = list()
for _ in range(N) :
	board.append(list(input()))

# 다시 칠해야하는 최솟값
result = N * M

# 8x8 크기로 자른 체스판
for i in range(0, N - 7) :
	for j in range(0, M - 7) :
		tmp = list()
		for k in range(8) :
			tmp.append(board[i+k][j:j+8])
		# (0, 0)이 흰색으로 시작
		cnt1 = start_from_white(tmp)
		# (0, 0)이 검은색으로 시작
		cnt2 = start_from_black(tmp)
		# 지금까지 구한 경우의 수 중에서 최솟값으로 업데이트
		result = min(result, cnt1, cnt2)

print(result)
