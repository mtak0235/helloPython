# 10250

import sys

t: int = int(sys.stdin.readline())

for i in range(t):
	h, w, n = map(int, sys.stdin.readline().split())
	cnt: int = 0
	res_w: int = 0
	tobreak = True
	for width in range(w):
		res_w += 1
		res_h: int = 0
		for height in range(h):
			res_h += 100
			cnt += 1
			if cnt == n:
				print(res_h + res_w)
				tobreak = False
				break
		if tobreak == False:
			break
