n, m = map(int, input().split())
chess_map = [list(input()) for _ in range(n)]
result = []

for i in range(n - 7):
    for j in range(m - 7):
        w_start = 0
        b_start = 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:
                    if chess_map[k][l] != 'W':
                        w_start += 1
                    if chess_map[k][l] != 'B':
                        b_start += 1
                else:
                    if chess_map[k][l] != 'B':
                        w_start += 1
                    if chess_map[k][l] != 'W':
                        b_start += 1
        result.append(w_start)
        result.append(b_start)

print(min(result))