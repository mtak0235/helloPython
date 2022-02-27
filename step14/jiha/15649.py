n, m = map(int, input().split())
arr = [0]*9
used = [False]*9
def func(k:int):
	if k==m:
		print(*arr[:m], sep=' ')
		return
	for i in range(1, n+1):
		if not used[i]:
			arr[k] = i
			used[i] = True
			func(k+1)
			used[i] = False
func(0)