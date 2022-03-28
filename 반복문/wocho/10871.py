N, pivot = map(int, input().split())

nums = list(map(int, input().split()))

ans = []
for x in nums:
	if x < pivot:
		ans.append(str(x))

print(' '.join(ans))