N = int(input())

n = 1
num = 666
while n < N:
	count = 0
	num += 1
	temp = num
	while temp > 0:
		if temp % 10 == 6:
			count += 1
			if count == 3:
				n += 1
				break
		else:
			count = 0
		temp //= 10

print(num)