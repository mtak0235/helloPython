import sys

input = sys.stdin.readline

ans = []

N = int(input())
for i in range(N):
	lst = input().rstrip().split("X")
	score = 0
	for j in range(len(lst)):
		score += (len(lst[j]) + 1) / 2 * len(lst[j])
	ans.append(str(int(score)))

print('\n'.join(ans))