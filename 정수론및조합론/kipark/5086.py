#[5086] 정수론및조합론, 배수와 약수 kipark
import sys

while True:
	a, b = map(int, input().split())
	if a == 0 and b == 0:
		break
	elif b % a == 0:
		print("factor")
	elif a % b == 0:
		print("multiple")
	else:
		print("neither")

