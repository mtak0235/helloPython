import sys

input = sys.stdin.readline

ans = []

N = int(input())
for _ in range(N):
	lst = list(map(int, input().split()))
	sum = 0
	for i in range(1, len(lst)):
		sum += lst[i]
	avg = sum / lst[0]
	cnt = 0
	for i in range(1, len(lst)):
		if lst[i] > avg:
			cnt += 1
	ans.append('%.3f%%' % (cnt / lst[0] * 100))

print('\n'.join(ans))