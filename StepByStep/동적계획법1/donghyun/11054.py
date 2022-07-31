import sys

input = sys.stdin.readline
n = int(input())
l = list(map(int, input().split()))
lis, lds = [1] * n, [1] * n
for i in range(n):
	for j in range(i):
		if l[j] < l[i]:
			lis[i] = max(lis[j] + 1, lis[i])
		if l[-j-1] < l[-i-1]:
			lds[-i-1] = max(lds[-j-1] + 1, lds[-i-1])
print(max(map(lambda x: x[0]+x[1]-1, zip(lis, lds))))