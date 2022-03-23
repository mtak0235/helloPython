n = int(input())

def isTermNum(num):
	count = 0
	for  i in range(20, -1, -1):
		div = 10 ** i
		q, r = divmod(num, div)
		num = r
		if q == 6:
			count +=1
		else:
			count = 0
		if count >=3:
			return True
	return False
i = 666
th = 0
result = 0
while(True):
	
	if (isTermNum(i)):
		th +=1
	if (th == n):
		result = i
		break;
	i +=1
print(i)