import sys

T = int(input())
for t in range(T):
	a, word = input().split()
	for str in word:
		for i in range(int(a)):
			print(str, end='')
	print()