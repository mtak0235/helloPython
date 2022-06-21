import sys

numbers = []
for i in range(0, 9) :
	numbers.append(int(sys.stdin.readline().rstrip()))
print(max(numbers))
print(numbers.index(max(numbers)) + 1)
