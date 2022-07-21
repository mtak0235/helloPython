def get_days_to_top(A, B, V):
	result = 0
	height = 0
	while True:
		result += 1
		height += A
		if height >= V :
			return result
		height -= B

#올라가기, 내려가기, 나무높이
A, B, V = map(int, input().split())

result = get_days_to_top(A, B, V)
print(result)
