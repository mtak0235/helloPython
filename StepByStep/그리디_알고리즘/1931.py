# 회의실 배정
# 그리디 알고리즘

import sys

input = sys.stdin.readline
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
A.sort(key=lambda x: (x[1], x[0]))

answer = 0
end_time = -1
for x in A:
    if x[0] >= end_time:
        answer += 1
        end_time = x[1]
print(answer)