# 검문
from math import gcd

n = int(input())
num = []
for _ in range(n):
	num.append(int(input()))
num.sort()
dif = [num[i+1] - num[i] for i in range(n-1)]

result = []
tmp = dif[0]
for i in range(1, n-1):
	tmp = gcd(tmp, dif[i])
for m in range(2, int(pow(tmp, 0.5))+1):
	if tmp % m == 0:
		result.append(m)
		result.append(tmp//m)
result.append(tmp)
result = list(set(result))
result.sort()
for i in result:
	print(i, end=' ')