#[1181]step12,단어 정렬
#길이가 짧은 것부터. 같으면 사전 순

n = int(input())
words_list = []

for _ in range(n):
    word = str(input())
    word_count = len(word)
    words_list.append((word, word_count))

#중복 삭제
words_list = list(set(words_list))

#단어 숫자 정렬 > 단어 알파벳 정렬
words_list.sort(key = lambda word: (word[1], word[0]))

for word in words_list:
    print(word[0])