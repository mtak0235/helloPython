from collections import deque

n = int(input())
if n != 1:
	ans = []
	q = deque([])
	q.append(n)
	while q:
		v = q.popleft()
		r = int(v**(1/2))
		for i in range(r, 0, -1):
			if i == 1:
				ans.append(v)
				break
			if v % i == 0:
				q.append(v // i)
				q.append(i)
				break
	ans.sort()
	print(*ans, sep='\n')