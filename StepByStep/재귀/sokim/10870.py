def	fibo(num) :
	if num == 0 :
		return 0
	elif num == 1 :
		return 1
	return fibo(num - 2) + fibo(num - 1)

n = int(input())

print(fibo(n))
