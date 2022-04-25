import sys

input = sys.stdin.readline

ans = []
nums = sorted(list(map(int, input().split())))
while nums[0] != 0 or nums[1] != 0 or nums[2] != 0:
	if nums[0] * nums[0] + nums[1] * nums[1] == nums[2] * nums[2]:
		ans.append('right')
	else:
		ans.append('wrong')
	nums = sorted(list(map(int, input().split())))

print('\n'.join(ans))