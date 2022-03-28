import sys

input = sys.stdin.readline

N = int(input())

nums = []
for _ in range(N):
	nums.append(int(input()))
nums.sort()

ans = []
for i in range(N):
	ans.append(str(nums[i]))

print('\n'.join(ans))