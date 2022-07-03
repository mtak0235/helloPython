numbers = []
remainders = []
cnt = 10

for i in range(10) :
	numbers.append(int(input()))
	remainders.append(numbers[i] % 42)
for i in range(10) :
	for j in range(i) :
		if remainders[i] == remainders[j] :
			cnt -= 1
			break
print(cnt)
