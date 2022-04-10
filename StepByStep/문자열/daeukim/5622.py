# 다이얼
dial = ['ABC', 'DEF,', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
words = input()
cnt = 0
for word in words:
  for i in range(8):
    if word in dial[i]:
      cnt += (i + 3)
print(cnt)