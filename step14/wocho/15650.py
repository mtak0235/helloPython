N, M = map(int, input().split())

def recur(start, limit, lst, cnt):
	if cnt == 0:
		print(*lst)
		return
	for i in range(start, limit + 1):
		if i not in lst:
			lst.append(i)
			recur(i + 1, limit, lst, cnt - 1)
			lst.pop()

lst = []
recur(1, N, lst, M)