# 101, 201, 301, ... H01 (H개)
# 102, 202, 302, ... H02 (H개)
# 1W, 2W, 3W, ... HW (H개)
# 최대 H * W 만큼의 방 할당 가능

# 3, 5, 10 -> 104호
def get_best_room_number(H, W, N):
	width = N // H + 1
	height = N % H
	if height == 0:
		width -= 1
		height = H
	if width < 10:
		result = str(height) + '0' + str(width)
	else:
		result = str(height) + str(width)
	return int(result)

T = int(input()) # 테스트 케이스 개수
for _ in range(T):
	# 층수, 방수, 몇번째 손님
	H, W, N = map(int, input().split())
	result = get_best_room_number(H, W, N)
	print(result)
