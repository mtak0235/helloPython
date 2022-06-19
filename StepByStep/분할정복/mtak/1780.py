import sys
input = sys.stdin.readline
side = int(input())
ma = [list(map(int, input().split())) for _ in range(side)]
m, z, o = 0, 0, 0

def divide(x, y, N):
	global m, z, o
	isBundle = True
	nt = ma[x][y]
	for i in range(x, x + N):
		for j in range(y, y + N):
			if ma[i][j] != nt:
				isBundle = False
				break
		if isBundle == False:
			break
	if isBundle:
		if nt == -1:
			m+= 1
		elif nt == 0:
			z += 1
		elif nt == 1:
			o += 1
	else:
		size = N//3
		divide(x, y, size)
		divide(x + size, y, size)
		divide(x, y + size, size)
		divide(x + size, y + size, size)
		divide(x, y + size * 2, size)
		divide(x + size * 2, y, size)
		divide(x + size * 2, y + size * 2, size)
		divide(x + size, y + size* 2, size)
		divide(x + size * 2, y + size, size)
	return

divide(0, 0, side)
print(m)
print(z)
print(o)