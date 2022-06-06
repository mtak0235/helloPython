# 문자열 집합
n, m = map(int, input().split())
s_list = []
for _ in range(n):
	s_list.append(input())
board = []
for _ in range(m):
	board.append(input())
cnt = 0
for s in board:
	if s in s_list:
		cnt += 1
print(cnt)