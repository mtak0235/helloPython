import sys
import heapq
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

n = int(input())
heap = []
for i in range(n):
	temp = int(input())
	if temp != 0:
		heapq.heappush(heap, (abs(temp), temp))
	else :
		if not heap:
			print(0)
		else:
			print(heapq.heappop(heap)[1])