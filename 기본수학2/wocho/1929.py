M, N = map(int, input().split())

check = [True] * 1000001
check[0] = False
check[1] = False

for i in range(2, 1000001):
	if check[i] == True:
		for j in range(2 * i, 1000001, i):
			check[j] = False

lst = []
for i in range(M, N + 1):
	if check[i] == True:
		lst.append(str(i))

print('\n'.join(lst))