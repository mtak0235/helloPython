# 부녀회장이 될테야
t = int(input())
for _ in range(t):
  k = int(input()) # k층
  n = int(input()) # n호
  n_list = [i + 1 for i in range(n)]
  for _ in range(k): # k층만큼 반복
    for j in range(1, n):
      n_list[j] += n_list[j-1] 
  print(n_list[n-1])

