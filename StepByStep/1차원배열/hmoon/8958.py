import sys


for i in range(int(sys.stdin.readline())):
	score = 0
	cnt = 0
	result = list(str(sys.stdin.readline()))
	for j in range(0, len(result)):
		if result[j] == 'O':
			cnt += 1
		elif result[j] == 'X' or j == len(result) - 1:
			score += (cnt * (cnt + 1) / 2)
			cnt = 0
	print(int(score))

