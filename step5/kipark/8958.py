import sys

n = int(input())

for i in range(n):
	arr = sys.stdin.readline()
	result = 0
	result_count = 0
	for j in arr:
		if(j == 'O'):
			result_count += 1
		else:
			result_count = 0
		result += result_count
	print(result)
