import sys
input = sys.stdin.readline
houses = int(input())
prices = [list(map(int, input().split())) for _ in range(houses)]
ref = [prices[0][0],prices[0][1], prices[0][2]]
for i in range(1, houses):
	tmp = [0, 0, 0]
	tmp[0] = min(ref[1], ref[2]) + prices[i][0]
	tmp[1] = min(ref[0], ref[2]) + prices[i][1]
	tmp[2] = min(ref[0], ref[1]) + prices[i][2]
	ref = tmp

print(min(ref))