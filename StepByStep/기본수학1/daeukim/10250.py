# ACM 호텔
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  h, w, n = map(int, input().split())
  q = (n-1) // h
  r = (n-1) % h
  print((r+1) * 100 + q + 1)
