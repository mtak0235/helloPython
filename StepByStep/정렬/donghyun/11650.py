l = map(lambda x: list(map(int, x.split())), list(open(0))[1:])
for i in sorted(l, key=lambda x: [x[0], x[1]]):
	print(*i)