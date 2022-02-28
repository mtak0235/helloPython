n, m = map(int, input().split())

arr = [0]*9

def func(k):
	if k == m:
		print(*arr[:m], sep=' ')
		return
	for i in range(arr[k-1], n+1):
		arr[k] = i
		func(k+1)

for j in range(1, n+1):
	arr[0] = j
	func(1)