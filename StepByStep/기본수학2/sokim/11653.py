import math

N = int(input())

if N == 1:
	pass
else:
	# N 의 소인수 리스트
	primefactors = list()
	for i in range(2, N + 1):
		while N % i == 0:
			primefactors.append(i)
			N //= i
	for i in primefactors:
		print(i)
