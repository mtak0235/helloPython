import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

sum = 0
t = int(input())
n = [int(input()) for _ in range(t)]
most = [0 for _ in range(t)]
for i in range(t):
	sum += n[i]
n.sort()
for i in range(t - 1):
	if n[i] == n[i + 1]:
		most[i + 1] = most[i] + 1
temp = max(most)
check = 0
for i in range(t):
	if temp == most[i]:
		check += 1
		if check <= 2:
			ans_3 = n[i]

ans_1 = round(sum / t)
ans_2 = n[t // 2]
ans_4 = n[t - 1] - n[0]

print ("%d\n%d\n%d\n%d" % (ans_1, ans_2, ans_3, ans_4))