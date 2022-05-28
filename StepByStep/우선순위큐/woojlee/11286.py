# 절대값 힙

import sys, heapq

inp = sys.stdin.readline
N = int(inp())
A = []
for _ in range(N):
    x = int(inp())    
    if x != 0:
        heapq.heappush(A, (-x, x)) if x < 0 else heapq.heappush(A, (x, x))
    else:
        print(heapq.heappop(A)[1]) if len(A) else print(0)
