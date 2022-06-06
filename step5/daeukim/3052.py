# 나머지
rm = []
for i in range(10):
  rm.append(int(input()) % 42)
print(len(set(rm)))
