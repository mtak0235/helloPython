self_nums = set(range(1, 10001))
generated_nums = set()
for i in range(1, 10001) :
	for j in str(i) :
		i += int(j)
	generated_nums.add(i)
self_nums = self_nums - generated_nums

for i in sorted(self_nums) :
	print(i)
