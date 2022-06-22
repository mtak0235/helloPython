import sys

sys.setrecursionlimit(10**9)

def dfs(G, dist, n, e):
    for i in G[n]:
        a, b = i
        if dist[a] == -1:
            dist[a] = e + b
            dfs(G, dist, a, e + b)


N = int(input())
G = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b, c = map(int, input().split())
    G[a].append([b, c])
    G[b].append([a, c])

dist = [-1] * (N + 1)
dist[1] = 0

dfs(G, dist, 1, 0)

start = dist.index(max(dist))
dist = [-1] * (N + 1)
dist[start] = 0
dfs(G, dist, start, 0)

print(max(dist))