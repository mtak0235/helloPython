import sys
input = sys.stdin.readline
side = int(input())
m = [list(map(int, input().split())) for _ in range(side)]
nw, nb = 0, 0
def divide(x, y, N):
	global nw, nb
	nt = 0
	for i in range(x, x + N):
		for j in range(y, y + N):
			if m[i][j]:
				nt += 1
	if nt == N * N:
		nb += 1
	elif nt == 0:
		nw += 1
	else:
		divide(x, y, N//2)
		divide(x, y + N//2, N//2)
		divide(x + N//2, y, N//2)
		divide(x + N//2, y + N//2, N//2)
	return

divide(0, 0, side)
print(nw)
print(nb)