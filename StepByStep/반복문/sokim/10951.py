import sys

while 1:
	try:
		A, B = map(int, sys.stdin.readline().rstrip().split())
		print(A + B)
	except:
		break
