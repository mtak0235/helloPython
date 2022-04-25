def is_prime(x:int) -> bool:
	if x == 2:
		return True
	for i in range(2, int(x**(1/2)) + 1):
		if x % i == 0:
			return False
	return True

p_list = []
for k in range(2, 246912 + 1):
	if is_prime(k):
		p_list.append(k)

while True:
	n = int(input())
	if n == 0:
		break
	cnt = 0;
	if n == 2:
		print(1)
	else:
		for i in p_list:
			if n < i < 2*n+1:
				cnt+=1
		print(cnt)