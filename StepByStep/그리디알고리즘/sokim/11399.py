total = int(input()) # 총 사람 수
time = list(map(int, input().split())) # 각 사람마다 출금에 걸리는 시간

sum = 0 # 모든 사람이 대기+출금하는 데에 걸리는 최소 시간
time.sort() # 출금에 걸리는 시간을 오름차순으로 정렬

for i in range(len(time)) :
	for j in range(i + 1) :
		sum += time[j]
print(sum)
