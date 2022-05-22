import sys
input = sys.stdin.readline
cnt = int(input())
a = [int(input()) for _ in range(cnt)]
if cnt > 2:
	utmost = [a[0], a[0] + a[1], max(a[0] + a[2], a[1] + a[2], a[0] + a[1])] + [0] * (cnt - 3)
	if cnt == 3:
		print(utmost[2])
		exit()
	for i in range(3, cnt):
		utmost[i] = max(max(utmost[i - 2],a[i - 1] + utmost[i - 3]) + a[i], utmost[i - 1])
	print(utmost[cnt - 1])
else:
    print(sum(a))
