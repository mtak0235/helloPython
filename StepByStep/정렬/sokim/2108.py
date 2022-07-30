import sys

# 산술평균
def	print_average(nums, N):
	sum = 0
	for num, cnt in nums.items():
		sum += num * cnt
	print(round(sum / N))

# 중앙값
def	print_median(nums, N):
	idx = N // 2
	for num, cnt in nums.items():
		idx -= cnt
		if idx < 0:
			print(num)
			break

# 최빈값
def	print_most_freqeunt(nums):
	array = list()
	maxcnt = max(nums.values())
	for num, cnt in nums.items():
		if cnt == maxcnt:
			array.append(num)
	array.sort()
	if len(array) == 1:
		print(array[0])
	else:
		print(array[1])

# 범위
def	print_range(nums):
	array = [k for k, v in nums.items() if v > 0]
	maxnum = max(array)
	minnum = min(array)
	print(maxnum - minnum)

N = int(sys.stdin.readline().rstrip())
nums = {x : 0 for x in range(-4000, 4001)}
for _ in range(N):
	idx = int(sys.stdin.readline().rstrip())
	nums[idx] += 1

print_average(nums, N)
print_median(nums, N)
print_most_freqeunt(nums)
print_range(nums)
