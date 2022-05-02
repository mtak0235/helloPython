import sys
from collections import defaultdict
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

k, n = map(int, input().split())
cable = [int(input()) for _ in range(k)] 

start = 1
end = max(cable)

while start <= end:
	cnt = 0
	mid = (start + end) // 2
	for cable_len in cable:
		cnt += cable_len // mid
	if cnt >= n:
		start = mid + 1
	else :
		end = mid - 1
		
print(end)