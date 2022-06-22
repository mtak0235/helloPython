import sys

# 총 케이스 개수
total = int(sys.stdin.readline())
for i in range(total) :
	# 각 케이스 입력(첫 번째 입력값: 해당 케이스의 학생 수)
	case = list(map(int, sys.stdin.readline().split()))
	avg = (sum(case) - case[0]) / case[0]
	# 평균을 넘는 학생 수
	cnt = 0
	for j in range(1, len(case)) :
		if case[j] > avg :
			cnt += 1
	print(f'{cnt/case[0] * 100:.3f}%')
