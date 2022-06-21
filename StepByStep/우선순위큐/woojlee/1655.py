# 가운데를 말해봐요
# 우선 순위 큐
# 두개의 힙, 중간 값 찾기

import sys, heapq

input = sys.stdin.readline
leftH = []  # 중간 값 이하의 수
rightH = [] # 중간 값 초과의 수

s = ''
N = int(input())

for i in range(N):
    x = int(input())
    heapq.heappush(leftH, -x) if len(leftH) == len(rightH) else heapq.heappush(rightH, x)

    # 중간 값이 중간 값 초과의 수보다 크다면 교환
    if rightH and -leftH[0] > rightH[0]:
        m = heapq.heappop(rightH)
        heapq.heappush(rightH, -heapq.heappop(leftH))
        heapq.heappush(leftH, -m)
    
    s += str(-leftH[0]) + '\n'

print(s)