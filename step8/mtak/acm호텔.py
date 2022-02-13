import sys
test_cnt = int(sys.stdin.readline())
test_list = [list(map(int, sys.stdin.readline().split())) for i in range(test_cnt)]
for hotel in test_list:
	n = 0
	for w in range(1, hotel[1] + 1):
		for h in range(1, hotel[0] + 1):
			n+= 1
			if n == hotel[2]:
				print("%d%02d"%(h, w))
