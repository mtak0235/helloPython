#올라가기, 내려가기, 나무높이
A, B, V = map(int, input().split())

day = (V-B)/(A-B)
if day == int(day):
	day = int(day)
else:
	day = int(day) + 1
print(int(day))
