from re import T


m = int(input())
n = int(input())
### 변수 2개를 만드는 대신 리스트를 만들면 편합니다
p_num_min = 0
p_num_sum = 0

for i in range(m, n+1):
	p_num = True
	if i == 1:
		continue
	for j in range(2, int(i**(1/2))+1):
		if i%j == 0:
			p_num = False
			break
	if p_num == True:
		p_num_sum+=i
		if p_num_min == 0:
			p_num_min = i

if p_num_min == 0:
	print(-1)
else:
	print(p_num_sum)
	print(p_num_min)