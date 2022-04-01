import sys

input = sys.stdin.readline

T = int(input())

nums = []
for _ in range(T):
	nums.append(int(input()))

for i in range(T):
	mi = i
	for j in range(i + 1, T):
		if nums[j] < nums[mi]:
			mi = j
	nums[i], nums[mi] = nums[mi], nums[i]

ans = []
for i in range(T):
	ans.append(str(nums[i]))

print('\n'.join(ans))