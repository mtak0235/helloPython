import math

l = open(0).read().strip().split("\n")[1]
l = [i for i in map(int, l.split())]
f = l[0]
for i in l[1:]:
	g = math.gcd(f, i)
	print(f"{f//g}/{i//g}")