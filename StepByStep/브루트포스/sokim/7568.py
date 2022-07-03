# 총 사람 수
total = int(input())
# 각각의 사람마다의 몸무게/키
data = list()
for _ in range(total) :
	data.append(list(map(int, input().split())))

 # 덩치 등수 리스트
result = list()
for w1, h1 in data : # 지금 랭크를 매기려는 사람(1번)
	rank = 1
	for w2, h2 in data : # 비교 대상(2번)
		# 만약 1번이 2번보다 몸무게와 키가 작으면 순위 +1
		if w1 < w2 and h1 < h2 :
			rank += 1
	result.append(rank)

for i in result :
	print(i, end=' ')
