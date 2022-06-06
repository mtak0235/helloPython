# 한수
def solve(a):
  a3 = a % 10
  a = a // 10
  a2 = a % 10
  a1 = a // 10
  if ((a1 - a2) == (a2 - a3)):
    return (1)
  else:
    return (0);

n = int(input())
cnt = 0
if (n < 100):
  cnt = n
if (n == 1000):
  n = n - 1
if (n >= 100):
  while (n >= 100):
    if solve(n):
      cnt += 1
    n = n - 1
  cnt = cnt + 99
print(cnt)