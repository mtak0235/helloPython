# 동전 종류의 수, 금액 총합
N, K = map(int, input().split())

# 동전 종류 리스트
coins = list()
for i in range(N) :
	coins.append(int(input()))
# 단위 가치가 큰 순서대로 정렬
coins.reverse()

# 필요한 동전의 수 
count = 0
for coin in coins :
	count += K // coin
	K %= coin
	if K == 0 :
		break
print(count)
