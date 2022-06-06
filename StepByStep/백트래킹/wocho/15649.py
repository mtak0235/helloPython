N, M = map(int, input().split())

def recur(max, lst, to_pick):
	if to_pick == 0:
		print(*lst)
		return
	for i in range(1, max + 1):
		if i not in lst:
			lst.append(i)
			recur(max, lst, to_pick - 1)
			lst.pop()

lst = []
recur(N, lst, M)