n = int(input())
result = n

for _ in range(n):
    word = input()
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            pass
        elif word[i] in word[i + 1:]:
            result -= 1
            break

print(result)
