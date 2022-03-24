num = int(input())

def calcSum(num):
	sum = num
	for i in range(6, -1, -1):
		q,r = divmod(num, 10 ** i)
		sum += q
		num -= q * (10 ** i) 
	return sum

flag = 0
for i in range(1, num + 1):
	if (calcSum(i) == num):
		flag = 1
		break;
if flag == 0:
	print(0)
else:
	print(i)

