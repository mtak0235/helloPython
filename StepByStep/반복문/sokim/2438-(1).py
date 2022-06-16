N = int(input())

for i in range(1, N + 1):
	j = 1
	while j <= i:
		print("*", end='')
		j += 1
	print("")
