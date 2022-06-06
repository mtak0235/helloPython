import sys

input = sys.stdin.readline

check = [False, False] + [True] * 9999

for i in range(2, 101):
	if check[i] == True:
		for j in range(2 * i, 10001, i):
			check[j] = False

T = int(input())

lst = []
for _ in range(T):
	n = int(input())
	lt = rt = n // 2
	while check[lt] == False or check[rt] == False:
		lt -= 1
		rt += 1
	print(lt, rt)
