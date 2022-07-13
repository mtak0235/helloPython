# 테스트케이스 개수
T = int(input())

for _ in range(T):
	floor = int(input()) # 층
	num = int(input()) # 호
	# 호마다 살고 있는 사람 수
	cnt = [x for x in range(1, num + 1)]
	# 층을 올라갈 때마다 업데이트
	for _ in range(floor):
		for i in range(1, num):
			cnt[i] += cnt[i - 1]
	print(cnt[-1])


# 2층: 1 4 10 16 ...
# 1층: 1 3 6 10 ...
# 0층: 1 2 3 4 ... 14
