# 최단 경로
# 다익스트라

import heapq
import sys

input = sys.stdin.readline
V, E = map(int, input().split())
K = int(input())

INF = 3000001
A = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    A[u].append((v, w))

q = []
dist = [INF] * (V + 1)
dist[K] = 0
heapq.heappush(q, (0, K))
while q:
    pre_cost, node = heapq.heappop(q)
    for dest, weight in A[node]:
        cur_cost = pre_cost + weight
        if cur_cost < dist[dest]:
            dist[dest] = cur_cost
            heapq.heappush(q, (cur_cost, dest))

for i in range(1, V + 1):
    print("INF") if dist[i] == INF else print(dist[i])