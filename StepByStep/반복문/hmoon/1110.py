import sys

# 입력
num = int(sys.stdin.readline())
solve = num
cnt = 0

while (1):
	if num < 9:
		x = 0
	else:
		x = num // 10
	y = num % 10
	num = x + y
	num = (y * 10) + (num % 10)
	cnt += 1
	if num == solve:
		break
print(cnt)
