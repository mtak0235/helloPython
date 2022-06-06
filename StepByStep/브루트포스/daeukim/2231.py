# 분해합
def recur_sum(n):
	if n < 10:
		return (n)
	if n >= 10:
		return (n % 10 + recur_sum(n // 10))

n = int(input())
for i in range(n):
	if i + recur_sum(i) == n:
		print(i)
		break
else:
	print(0)