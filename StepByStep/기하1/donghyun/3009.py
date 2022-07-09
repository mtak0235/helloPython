a, b, c = map(str.split, open(0).read().strip().split("\n"))
for i, j, k in zip(a,b,c):
	print(0^int(i)^int(j)^int(k), end=' ')