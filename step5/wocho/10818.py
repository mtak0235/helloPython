N = int(input())
lst = list(map(int, input().split()))

M = lst[0]
m = lst[0]
for i in range(1, N):
	if lst[i] < m:
		m = lst[i]
	elif lst[i] > M:
		M = lst[i]

print("{0} {1}".format(m, M))