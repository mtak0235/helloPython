def hanoi(n:int, x:int, y:int, z:int):
	global cnt, ans
	if n == 1:
		ans.append([x,z])
		cnt+=1
		return
	hanoi(n-1, x, z, y)
	ans.append([x,z])
	cnt+=1
	hanoi(n-1, y, x, z)

n = int(input())
cnt = 0
ans = []
hanoi(n, 1, 2, 3)
print(cnt)
for i in ans:
	print(*i, sep=' ')