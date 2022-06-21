import sys

numbers = []
for i in range(0, 3) :
	numbers.append(int(sys.stdin.readline().rstrip()))
total = str(numbers[0] * numbers[1] * numbers[2])

cnt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
i = 0
for i in range(0, len(total)) :
	for j in range(0, 10) :
		if total[i] == str(j) :
			cnt[j] += 1

for i in range(0, 10) :
	print(cnt[i])
