# import collections 해서 collections.Counter() 처럼 써도 됨
from collections import Counter

# 입력 받은 문자열을 모두 대문자화 + 리스트화
string = list(input().upper())

# 리스트를 딕셔너리화(단어-단어개수 튜플)
c = Counter(string)

# 가장 많이 등장한 단어 리스트(2개 이상이면 물음표 출력)
c_max = list()
for letter, count in c.items() :
	if count == max(c.values()) :
		c_max.append(letter)
if len(c_max) > 1 :
	print('?')
else :
	print(c_max[0])
