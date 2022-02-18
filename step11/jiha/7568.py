n = int(input())
arr = []
ans = []
for _ in range(n):
	x, y = map(int, input().split())
	arr.append((x, y))

for i in range(n):
	cnt = 1
	for j in range(n):
		if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
			cnt+=1
	ans.append(cnt)
print(*ans, sep=' ')