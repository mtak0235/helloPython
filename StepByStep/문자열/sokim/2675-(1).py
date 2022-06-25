# 전체 케이스 개수
cnt = int(input())

# R = 반복 횟수, S = 문자열
for i in range(cnt) :
	R, S = input().split()
	# 각 문자 * R 만큼 리스트에 추가
	result = list()
	for letter in S :
		for repeat in range(int(R)) :
			result.append(letter)
	# 리스트를 문자열로 변환
	string = ''.join(result)
	print(string)
