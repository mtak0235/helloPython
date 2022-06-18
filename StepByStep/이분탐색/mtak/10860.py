# import sys
# input = sys.stdin.readline
# n = int(input())
# N = list(map(int, input().split()))
# T = list()
# def binarySearch(i, li):
#     start = 0
#     end = len(li) - 1
#     mid = (start + end) // 2
#     while end - start  >= 0:
#         if li[mid][0] == i:
#             return mid
#         elif li[mid][0] < i:
#             start = mid + 1
#         else:
#             end = mid - 1
#         mid = (start + end) // 2
#     return -1

# for idx, i in enumerate(N):
#     position = binarySearch(i, T) 
#     if position == -1:
#         T.append([i, 1])
#         T.sort()
#     else:
#         T[position][1] += 1
# m = int(input())
# M = list(map(int, input().split()))

# for i in M:
#     position = binarySearch(i, T)
#     if position == -1:
#         print(0)
#     else:
#         print(T[position][1])

from bisect import bisect_left, bisect_right
from sys import stdin

n = stdin.readline().rstrip()
card = list(map(int,stdin.readline().split()))
m = stdin.readline().rstrip()
test = list(map(int,stdin.readline().split()))
card.sort()

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

for i in range(len(test)):
    print(count_by_range(card, test[i], test[i]), end=' ')