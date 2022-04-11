a, b, c = map(int, input().split())

profit = c - b
print(a // profit + 1 if profit > 0  else -1)