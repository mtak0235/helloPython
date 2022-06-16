import sys

while (1):
	try:
		A, B = map(int, sys.stdin.readline().split())
		print(A + B)
	except:
		break
