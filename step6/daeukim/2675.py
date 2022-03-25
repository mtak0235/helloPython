# 문자열 반복
t = int(input())
for _ in range(t):
  r, str1 = input().split()
  str2 = ""
  for s in str1:
    str2 += s * int(r)
print(str2)