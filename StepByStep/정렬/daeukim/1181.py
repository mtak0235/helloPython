# 단어 정렬
n = int(input())
words = []
for _ in range(n):
	words.append(input())
words = list(set(words))
words.sort()
words.sort(key = lambda x : len(x))
for i in words:
	print(i)
