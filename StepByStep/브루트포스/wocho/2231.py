N = int(input())

ans = 0
for i in range(1, N):
	temp = i
	num = i
	while temp > 0:
		num += temp % 10
		temp //= 10
	if num == N:
		ans = i
		break

print(ans)