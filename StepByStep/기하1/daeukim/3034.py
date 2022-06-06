# 앵그리 창영
n, w, h = map(int, input().split())
length = w ** 2 + h ** 2
length = int(length ** 0.5)
for _ in range(n):
	if int(input()) > length:
		print("NE")
	else:
		print("DA")