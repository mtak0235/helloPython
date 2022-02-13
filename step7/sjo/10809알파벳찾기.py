# 1 ---------------------------------------------

# word = input()
# alphabets = 'abcdefghijklmnopqrstuvwxyz'

# for i in alphabets:
#     if i in word:
#         print(word.index(i), end = " ")
#     else:
#         print(-1, end = " ")


# 2 ---------------------------------------------

word = input()
alphabets = list(range(97, 123))    # 아스키코드 숫자 범위

for i in alphabets:
    print(word.find(chr(i)), end = " ")