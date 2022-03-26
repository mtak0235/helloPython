#[1181] step12, 단어 정렬 kipark
import sys

n = int(input())
word_list = []

for i in range(n):
	word_list.append(input())

temp_list = list(set(word_list))
temp_list.sort()
temp_list.sort(key=len)

for word in temp_list:
	print(word)