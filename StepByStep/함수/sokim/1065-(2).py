num = int(input())

# 한수의 개수
cnt = 0
for i in range(1, num + 1) :
	# 100 미만의 수는 전부 한수
	if i < 100 :
		cnt += 1
	else :
		num_list = list(map(int, str(i)))
		if num_list[0] - num_list[1] == num_list[1] - num_list[2] :
			cnt += 1	
print(cnt)
