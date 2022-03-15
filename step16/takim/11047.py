import sys

n, k = map(int, sys.stdin.readline().split())
coinNum = 0
coins = []

for i in range(n):
	coins.append(int(sys.stdin.readline()))

for i in range(n-1, -1, -1):
	coin = coins[i]
	quotient, k = divmod(k, coin)
	coinNum += quotient
	if k == 0:
		break;
print(coinNum)