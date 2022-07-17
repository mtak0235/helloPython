import math

N = int(input()) # 입력값 개수
array = list(map(int, input().split())) # 입력값

cnt = 0 # 정답
for i in array:
	if i == 1:
		continue
	elif i == 2 or i == 3:
		cnt += 1
		continue
	flag = True # 소수 판별 플래그
	for j in range(2, int(math.sqrt(i)) + 1):
		if i % j == 0:
			flag = False
	if flag == True:
		cnt += 1
print(cnt)
