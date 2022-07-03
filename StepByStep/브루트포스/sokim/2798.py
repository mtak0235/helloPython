# 카드의 개수, 목표 숫자
N, M = map(int, input().split())

# 각 카드에 써있는 수
nums = list(map(int, input().split()))

# 현재 선택한 카드들에 써있는 숫자들의 합
sum = 0
# M 에 가장 가까운 최대 sum
max = 0
for i in range(N - 2) :
	for j in range(i + 1, N - 1) :
		for k in range(j + 1, N) :
			sum = nums[i] + nums[j] + nums[k]
			if sum > M :
				continue
			elif sum > max :
				max = sum
print(max)
