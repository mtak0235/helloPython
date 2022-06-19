import sys

n = int(sys.stdin.readline())

for i in range(1, 10):
	print('%d * %d = %d'%(n, i, i * n))
