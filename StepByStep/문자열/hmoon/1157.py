# 단어 공부
import sys
import string

word = sys.stdin.readline().strip()
word = list(map(str, (word.upper())))
word_temp = set(word)
word_temp = list(word_temp)
cnt = []

for i in word_temp:
    cnt.append(word.count(i))
if (cnt.count(max(cnt)) > 1):
    print('?')
else:
    print(word_temp[cnt.index(max(cnt))])
