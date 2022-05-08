# 직각삼각형
while True:
  num = list(map(int, input().split()))
  if sum(num) == 0:
    break
  num.sort()
  if num[0]**2 + num[1]**2 == num[2]**2:
    print("right")
  else:
    print("wrong")
