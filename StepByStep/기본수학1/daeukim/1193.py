# 분수찾기
x = int(input())
cnt = 0
i = 1
while cnt < x:
  cnt += i
  i += 1
i -= 1
cnt -= x
if (i % 2 == 0):
  a = i - cnt
  b = cnt + 1
else:
  a = cnt + 1
  b = i - cnt
print('{}/{}'.format(a, b))
