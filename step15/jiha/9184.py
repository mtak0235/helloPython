arr = [[[1 for col in range(21)] for row in range(21)] for depth in range(21)]

for i in range(1, 21):
	for j in range(1, 21):
		for k in range(1, 21):
			if i < j < k:
				arr[i][j][k] = arr[i][j][k-1] + arr[i][j-1][k-1] - arr[i][j-1][k]
			else:
				arr[i][j][k] = arr[i-1][j][k] + arr[i-1][j-1][k]+arr[i-1][j][k-1] - arr[i-1][j-1][k-1]

while True:
	a, b, c = map(int, input().split())
	if a ==-1 and b == -1 and c ==-1:
		break
	if a <=0 or b<=0 or c<=0:
		print('w({0}, {1}, {2}) = {3}'.format(a, b, c, 1))
	elif a > 20 or b > 20 or c > 20:
		print('w({0}, {1}, {2}) = {3}'.format(a, b, c, arr[20][20][20]))
	else:
		print('w({0}, {1}, {2}) = {3}'.format(a, b, c, arr[a][b][c]))