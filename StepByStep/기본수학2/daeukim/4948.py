# 베르트랑 공준
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

num = [i for i in range(123456*2+1)]
prime_list = []

for i in num:
  if ft_isprime(i):
    prime_list.append(i)

while True:
  n = int(input())
  if n == 0:
    break
  cnt = 0
  for i in prime_list:
    if n<i<=n*2:
      cnt += 1
  print(cnt)
  