remainders = []

for i in range(10) :
	number = int(input())
	remainders.append(number % 42)
remainders = set(remainders)
print(len(remainders))
