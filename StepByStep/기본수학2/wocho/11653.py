N = int(input())

lst = []
div = 2
while N != 1:
	while N % div == 0:
		N /= div
		lst.append(str(div))
	div += 1

if lst:
	print('\n'.join(lst))
else:
	pass
