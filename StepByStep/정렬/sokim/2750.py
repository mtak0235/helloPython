# 버블정렬
N = int(input())
nums = list()

for _ in range(N):
	nums.append(int(input()))

for i in range(N - 1):
	for j in range(N - 1 - i):
		if nums[j] > nums[j + 1]:
			nums[j], nums[j + 1] = nums[j + 1], nums[j]

for num in nums:
	print(num)
