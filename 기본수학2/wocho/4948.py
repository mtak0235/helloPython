import sys

input = sys.stdin.readline

limit = 123456 * 2
check = [True] * (limit + 1)
check[0] = False
check[1] = False

for i in range(2, limit + 1):
	if check[i] == True:
		for j in range(2 * i, limit + 1, i):
			check[j] = False

ans = []
n = int(input())
while n != 0:
	count = 0
	for i in range(n + 1, 2 * n + 1):
		if check[i] == True:
			count += 1
	ans.append(str(count))
	n = int(input())

print('\n'.join(ans))
