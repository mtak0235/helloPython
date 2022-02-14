import sys

N = int(input())
for length in range(N):
	arr = list(map(int, sys.stdin.readline().split()))
	student_avg_score = sum(arr[1:]) / arr[0]
	student_count = 0
	for student_score in arr[1:]:
		if(student_score > student_avg_score):
			student_count += 1
	avg_score = (student_count / arr[0]) * 100
	print(f"{avg_score:.3f}", "%", sep='')