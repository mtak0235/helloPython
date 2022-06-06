N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
virus = [[0] * N for i in range(N)]
visit = [0 for i in range(N)]
for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    virus[x - 1][x - 1] = 1
    virus[y - 1][y - 1] = 1
def dfs(find):
    visit[find] = 1
    for i in range(N):
        if virus[find][i] == 1 and visit[i] == 0:
            dfs(i)
dfs(0)
cnt = 0
for i in range(1, N):
    if visit[i] == 1:
        cnt += 1
print(cnt)