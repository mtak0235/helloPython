#[11729] step10, 하노이 탑 이동 속도 kipark
import sys

def hanoi(n, here, mid, there):
	if(n == 1):
		print(here, there)
	else:
		hanoi(n-1, here, there, mid) 
		print(here, there)
		hanoi(n-1, mid, here, there)

n = int(input())

print(pow(2, n) - 1)
hanoi(n, 1, 2, 3)