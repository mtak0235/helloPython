# 4673

def d(n: int) -> int:
	return n + sum(map(int, list(str(n))))

numList = {}
for i in range(1, 10001):
	if i not in numList:
		print(i)
	numList[d(i)] = 1
