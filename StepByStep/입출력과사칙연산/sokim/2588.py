A = int(input())
B = int(input())
array = [0] * 3
i = 0
while i < 3:
	array[i] = A * (B % 10)
	print(array[i])
	B = int(B / 10)
	i += 1
result = 0
i = 2
while i >= 0:
	result *= 10
	result += array[i]
	i -= 1
print(result)
