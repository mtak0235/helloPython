# 골드바흐의 추측
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

t = int(input())
for _ in range(t):
  n = int(input())
  for i in range(n//2, 1, -1):
    if ft_isprime(i):
      if ft_isprime(n-i):
        print(i, n-i)
        break
  