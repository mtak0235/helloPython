l = open(0).read().strip().split("\n")[:-1]
for i, j, k in map(str.split, l):
	i, j, k = int(i), int(j), int(k)
	m = max(i, j, k)
	if 2 * m**2 == i**2+j**2+k**2:
		print("right")
	else:
		print("wrong")