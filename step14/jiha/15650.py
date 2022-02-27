n, m = map(int, input().split())

arr = [0]*9
check = [False]*9

def func(k):
	if k == m:
		print(*arr[:m], sep=' ')
		return
	for i in range(arr[k-1] + 1, n + 1):
		if not check[i]:
			arr[k] = i
			check[i] = True
			func(k+1)
			check[i] = False
for j in range(1, n - m + 2):
	arr[0] = j
	func(1)