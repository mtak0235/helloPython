# 알파벳 찾기
import sys
import string

word = list(map(str, sys.stdin.readline().strip()))
lst = list(string.ascii_lowercase)
ret = []

for i in lst:
    if i in word:
        ret.append(word.index(i))
    elif i not in word:
        ret.append(-1)

print(*ret, sep=' ')
