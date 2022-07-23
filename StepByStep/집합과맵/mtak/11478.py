import sys

input = sys.stdin.readline
str = input().strip()
s = set()
for i in range(len(str)):
    tmp = ""
    for j in range(i, len(str)):
        tmp += str[j]
        s.add(tmp)
print(len(s))

