N, M = map(int, input().split())
nums = list(map(int, input().split()))

jack = 0
for i in range(N - 2):
	for j in range(i + 1, N - 1):
		for k in range(j + 1, N):
			temp = nums[i] + nums[j] + nums[k]
			if (temp > M):
				continue
			if jack < temp:
				jack = temp

print(jack)
