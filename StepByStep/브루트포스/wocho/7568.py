import sys

input = sys.stdin.readline

N = int(input())

hw = dict()
for i in range(N):
	h, w = map(int, input().split())
	hw[i] = (h, w)

ans = []
for i in range(N):
	rank = 1
	for j in range(N):
		if hw[j][0] > hw[i][0] and hw[j][1] > hw[i][1]:
			rank += 1
	ans.append(str(rank))

print(' '.join(ans))