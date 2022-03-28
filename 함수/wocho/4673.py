lst = [False] * 10001

def get_next_num(n: int) -> int:
	ret = n
	while n != 0:
		ret += n % 10
		n //= 10
	
	return ret

for i in range(1, 10001):
	next = get_next_num(i)
	while next <= 10000 and lst[next] == False:
		lst[next] = True
		next = get_next_num(next)

ans = []
for i in range(1, 10001):
	if lst[i] == False:
		ans.append(str(i))

print('\n'.join(ans))