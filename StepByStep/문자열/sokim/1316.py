import sys
cases = int(input())
total = cases

# 입력 받은 단어들의 리스트
words = list()
for i in range(cases) :
	words.append(sys.stdin.readline().strip())

# 단어 리스트 순회
for word in words :
	# 각 문자의 등장 횟수를 세는 딕셔너리 
	cnt = dict()
	# 각 단어 순회
	for i in range(len(word)) :
		cnt[word[i]] = cnt.get(word[i], 0) + 1
		if cnt[word[i]] > 1 and word[i-1] != word[i] :
			total -= 1
			break
print(total)
