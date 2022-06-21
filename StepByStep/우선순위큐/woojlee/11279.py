# 최대 힙


import heapq
import sys

inp = sys.stdin.readline

N = int(inp())

heap = []
s = ''
for _ in range(N):
    x = int(inp())
    if x:
        heapq.heappush(heap, -x)
    else:
        print(-heapq.heappop(heap)) if len(heap) else print(0)
