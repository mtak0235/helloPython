def make_star(n):
	if n == 3:
		star[1] = ['*', ' ', '*']
		star[0][:3] = star[2][:3] = ['*']*3
		return
	div_n = n//3
	make_star(div_n)
	for i in range(3):
		for j in range(3):
			if i == 1 and j == 1:
				continue
			for k in range(div_n):
				#첫번째 블록 단위를 제대로 입력하고 그를 베낀다는 마인드
				star[div_n * i + k][div_n*j:div_n*(j+1)] = star[k][:div_n]

n = int(input())
star = [[' ' for _ in range(n)] for _ in range(n)]
make_star(n)
for i in star:
	print(*i, sep='')