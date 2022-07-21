import sys
import heapq
input = sys.stdin.readline
n = int(input())
a = [int(input()) for _ in range(n)]
heap = []
heapq.heapify(heap)
for i in a:
    if i == 0 and len(heap)==0:
        print(0)
    elif i == 0:
        print(abs(heapq.heappop(heap)))
    else:
        heapq.heappush(heap, i)


