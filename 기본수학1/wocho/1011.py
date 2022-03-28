import sys
import math

input = sys.stdin.readline

T = int(input())

lst = []
for _ in range(T):
	x, y = map(int, input().split())
	dist = y - x
	temp = math.ceil(math.sqrt(dist))
	if dist <= math.pow(temp, 2) - temp:
		lst.append(str((temp - 1) * 2))
	else:
		lst.append(str(temp * 2 - 1))

print('\n'.join(lst))