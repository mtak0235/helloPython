# 링
n = int(input())
rs = list(map(int, input().split()))

for r in range(1, n):
	n1 = rs[0]
	n2 = rs[r]
	while (n1 % n2 != 0):
		m = n1 % n2
		n1 = n2
		n2 = m
	n1 = rs[0] // n2
	n2 = rs[r] // n2
	print(f"{n1}/{n2}")
	