def get_days_to_top(A, B, V):
	day = 0
	height = 0
	while True:
		day += 1
		if day >= (V-B)/(A-B):
			return day

#올라가기, 내려가기, 나무높이
A, B, V = map(int, input().split())

result = get_days_to_top(A, B, V)
print(result)

#day(A-B)+B >= V
#day >= (V-B)/(A-B)
