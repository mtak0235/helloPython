n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

size_row = n - 8
size_col = m - 8
ans = 65
bw = ['B', 'W']
cnt = []
def chess(x, y) -> int:
	for k in range(2):
		dec_a = bw[k]
		dec_b = bw[k-1]
		cnt_local = 0
		for i in range(x, x + 8):
			for j in range(y, y + 8):
				if (i + j - x - y)%2 == 0 and arr[i][j] != dec_a:
					cnt_local+=1
				elif (i + j - x - y)%2 != 0 and arr[i][j] != dec_b:
					cnt_local+=1
		cnt.append(cnt_local)

for i in range(size_row + 1):
	for j in range(size_col + 1):
		chess(i, j)
print(min(cnt))