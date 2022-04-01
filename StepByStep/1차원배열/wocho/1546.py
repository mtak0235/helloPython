N = int(input())
lst = list(map(int, input().split()))

M = max(lst)
sum = 0
for i in range(N):
	sum += lst[i] / M * 100

print(sum / N)