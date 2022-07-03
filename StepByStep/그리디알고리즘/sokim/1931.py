# 회의의 수
N = int(input())

# 회의 정보: [(시작시간, 종료시간), (시작시간, 종료시간), ... ]
info = list()
for i in range(N) :
	time = tuple(map(int, input().split()))
	info.append(time)

# 시작 시간이 빠른 순으로 정렬
info.sort(key = lambda x : x[0])
# 종료 시간이 빠른 순으로 정렬
info.sort(key = lambda x : x[1])

# 직전 회의 종료 시간
last = 0
# 회의 개수
count = 0
for s, e in info :
	if s >= last :
		last = e
		count += 1
print(count)
