cnt = int(input())

for i in range(cnt) :
	case = list(input())
	sum = 0
	score = 1
	for j in case :
		if j == 'O' :
			sum += score
			score += 1
		else :
			score = 1
	print(sum)
