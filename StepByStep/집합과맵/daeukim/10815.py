# 숫자 카드
import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
m = int(input())
board = list(map(int, input().split()))

card.sort()

def binary_search(arr, target, start, end):
  while start <= end:
    mid = (start+end)//2
    if arr[mid] == target:
      return mid
    elif arr[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return None

for i in range(m):
    if binary_search(card, board[i], 0, n - 1) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')