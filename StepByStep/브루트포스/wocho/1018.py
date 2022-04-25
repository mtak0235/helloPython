import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(input().strip())

result = float("inf")
check = ('B', 'W')
for i in range(N - 7):
    for j in range(M - 7):
        # flag => Black: False / White: True
        flag = False
        for _ in range(2):
            cnt = 0
            for p in range(i, i + 8):
                for q in range(j, j + 8):
                    if flag:
                        # 현재 칸이 white 이어야 하는 경우
                        if board[p][q] == check[0]:
                            cnt += 1
                    else:
                        # 현재 칸이 black 이어야 하는 경우
                        if board[p][q] == check[1]:
                            cnt += 1
                    flag = not flag
                flag = not flag
            flag = not flag
            result = min(result, cnt)

print(result)