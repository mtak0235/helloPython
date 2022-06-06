# 소수
m = int(input())
n = int(input())

def ft_isprime(num):
  i = 2
  if num < 2:
    return (0)
  if num == 2:
    return (1)
  while i <= int(num**0.5)+1:
    if num % i == 0:
      return (0)
    i += 1
  return (1)
    
p_list = []
for i in range(m, n+1):
  if ft_isprime(i):
    p_list.append(i)
if len(p_list) == 0:
  print(-1)
else:
  print(sum(p_list))
  print(min(p_list))