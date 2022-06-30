def	get_min_generator(num) :
	for i in range(num) :
		string = str(i)
		# i 의 분해합
		generated = i
		for j in string :
			generated += int(j)
		if generated == num :
			return i
	return 0
	
# 자연수 N
N = int(input())

# 가장 작은 생성자 구하기
generator = get_min_generator(N)
print(generator)
