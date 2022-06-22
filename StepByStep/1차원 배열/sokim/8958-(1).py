import sys

cnt = int(sys.stdin.readline())
case = []
for i in range(cnt) :
	case = list(sys.stdin.readline().rstrip())
	score = 0
	bonus = 0
	for j in range(len(case)) :
		if case[j] == 'X' :
			bonus = 0
			continue
		elif j != 0 and case[j - 1] == 'O' :
			bonus += 1
		score += 1 + bonus
	print(score)
