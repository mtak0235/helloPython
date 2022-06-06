import sys

input = input()
arr = list(range(97, 123))

for i in arr:
	if (input.find(chr(i)) != -1):
		print(input.find(chr(i)), end=" ")
	else:
		print("-1", end=" ")