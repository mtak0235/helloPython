import sys

cnt = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
min = numbers[0]
max = numbers[0]

for i in numbers :
	if i < min :
		min = i
	elif i > max :
		max = i

print(min, max)
