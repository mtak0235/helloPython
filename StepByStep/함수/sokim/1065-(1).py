import sys
num = int(input())

# 1~99 까지는 전부 한수이므로 받은 숫자 그대로 출력
if num <= 99 :
	print(num)
	sys.exit()

# 100 이상의 숫자가 입력된 경우 등차수열 여부 확인
cnt = num
for i in range(100, num + 1) :
	string = str(i)
	diff_first = int(string[1]) - int(string[0])
	for j in range(1, len(string) - 1) :
		diff_now = int(string[j + 1]) - int(string[j])
		if diff_now != diff_first :
			cnt -= 1
			break
print(cnt)
