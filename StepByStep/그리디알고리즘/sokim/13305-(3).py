# -------------------------------------------------------------------------------------------------------------------- #
# 가장 저렴한 가격의 도시에서 마지막 목적지까지 필요한 기름 전부 주유
# 해당 도시에 도착하기 전에는 그 다음으로 저렴한 도시에서 최대 주유, 반복
# 예: 도시별 가격/거리가 3 - (1) - 4 - (1) - 1 - (1) - 2 - (1) - 3 이라면, 첫 번째 도시에서 주유(3 * 2), 세 번째 도시에서 주유(1 * 2)
# -------------------------------------------------------------------------------------------------------------------- #


# 총 도시 수, 도시간 거리, 도시별 주유 가격
cnt = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))
# 마지막 도시의 주유 가격은 필요 없음
prices.pop()

# 가장 저렴하게 주유할 경우의 총 비용
sum = 0
# 지금까지 탐색한 도시 중에 최소 비용
min = prices[0]
for price, distance in zip(prices, distances) :
	if price < min :
		min = price
	sum += min * distance
print(sum)


# ------------------------------------------------------------------------------------------ #
# 기타 풀이
#
# 1. 리스트 컴프리헨션 - prices.pop() 없이 조건문으로 자름
# prices = [(i, price) for i, price in enumerate(prices) if i < len(prices) - 1]
# min = prices[0][1]
# for i, price in prices :
# 	if price < min :
# 		min = price
# 	print("min: ", min)
# 	sum += min * distances[i]
# print(sum)
# 
# 2. enumerate() - prices 의 인덱스와 값을 하나의 쌍으로 묶어서 순회
# min = prices[0]
# for i, price in enumerate(prices) :
# 	if price < min :
# 		min = price
# 	sum += min * distances[i]
# print(sum)
# ------------------------------------------------------------------------------------------ #
