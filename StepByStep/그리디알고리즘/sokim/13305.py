# 가장 저렴한 가격의 도시에서 마지막 목적지까지 필요한 기름 전부 주유
# 해당 도시에 도착하기 전에는 그 다음으로 저렴한 도시에서 최대 주유, 반복
# 예: 도시별 가격/거리가 3 - (1) - 4 - (1) - 1 - (1) - 2 - (1) - 3 이라면, 첫 번째 도시에서 주유(3 * 2), 세 번째 도시에서 주유(1 * 2)

def	get_minimum_sum(end, sum) :
	if end == 0 :
		return sum
	# 최소 비용이었던 도시 이전에 방문하는 도시들 사이에서의 최소 비용 탐색
	cheapest = min(prices[:end])
	pos = prices.index(cheapest)
	distance = 0
	for i in range(pos, end) :
		distance += distances[i]
	sum += cheapest * distance
	sum = get_minimum_sum(pos, sum)
	return sum

# 총 도시 수, 도시간 거리, 도시별 주유 가격
cnt = int(input())
distances = list(map(int, input().split()))
# 마지막 도시에선 실제로 이동하지 않지만 계산상 편리를 위해 0 추가
distances.append(0)
prices = list(map(int, input().split()))

# 가장 저렴하게 주유할 경우의 총 비용
sum = 0
# 재귀 함수에 넘겨줄 인자를 리스트의 마지막 인덱스 + 1 로 초기화
pos = len(prices)
sum = get_minimum_sum(pos, sum)
print(sum)
