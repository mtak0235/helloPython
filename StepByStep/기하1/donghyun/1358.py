i, *l = open(0).read().strip().split("\n")
w, h, x, y, p = map(int, i.split())
r = h//2
x1, y1, x2, y2 = x, y + r, x + w, y + r
c = 0
for i, j in map(str.split, l):
	i, j = int(i), int(j)
	c1 = x <= i <= x + w and y <= j <= y + h
	c2 = (x1-i)**2+(y1-j)**2<=r**2
	c3 = (x2-i)**2+(y2-j)**2<=r**2
	if c1 or c2 or c3:
		c += 1
print(c)