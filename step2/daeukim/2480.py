# 주사위 세개
a, b, c = map(int, input().split())

if (a == b == c): # 같은 눈이 3개
  sum = 10000 + a * 1000
elif (a == b or a == c): # 같은 눈이 2개
  sum = 1000 + a * 100
elif (b == c):
  sum = 1000 + b * 100
else: # 모두 다른 눈
  sum = max(a, b, c) * 100
print(sum)
