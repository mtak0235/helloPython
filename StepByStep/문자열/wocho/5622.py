dial = [3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10]

number = input()

answer = 0

A = ord('A')
for x in number:
	answer += dial[ord(x) - A]

print(answer)