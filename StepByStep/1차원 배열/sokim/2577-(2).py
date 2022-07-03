import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
total = list(str(A * B * C))

for i in range(10) :
	print(total.count(str(i)))
