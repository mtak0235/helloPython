import sys

input = sys.stdin.readline
n = int(input())
l = []
for _ in range(n):
	l.append(list(map(int, input().split())))
l.sort(key=lambda x: x[0])
l = [i[1] for i in l]
lis = [1] * n
for i in range(n):
	for j in range(i):
		if l[j] < l[i]:
			lis[i] = max(lis[j]+1, lis[i])
print(n-max(lis))