import sys

N = int(sys.stdin.readline().rstrip())
nums = [0 for _ in range(10001)]
for i in range(N):
	idx = int(sys.stdin.readline().rstrip())
	nums[idx] += 1

for idx, cnt in enumerate(nums):
	for _ in range(cnt):
		print(idx)
