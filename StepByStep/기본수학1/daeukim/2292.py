# 벌집
n = int(input())
cnt = 1
result = 0
i = 0
while cnt < n:
  i += 1
  cnt += i * 6
print(i + 1)