n,m = map(int, input().split())

cards = tuple(map(int, input().split()))

maximum = 0

for i in range(0, n - 2):
	firstCard = cards[i]
	for j in range(i + 1, n - 1):
		secondCard = cards[j]
		for k in range(j + 1, n):
			thirdCard = cards[k]
			summation = firstCard + secondCard + thirdCard
			if (summation) <= m and summation > maximum:
				maximum = summation
print(maximum)
	