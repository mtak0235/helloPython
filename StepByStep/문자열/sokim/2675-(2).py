# 전체 케이스 개수
cnt = int(input())

# R = 반복 횟수, S = 문자열
for i in range(cnt) :
	R, S = input().split()

	# 빈 문자열을 생성하여 각 문자 * R 만큼씩 병합
	result = ''
	for letter in S :
		result += letter * int(R)
	print(result)
