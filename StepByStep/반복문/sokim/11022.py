import sys

cnt = int(input())
i = 1
while i <= cnt:
	A, B = map(int, sys.stdin.readline().rstrip().split())
	print("Case #" + str(i) + ": " + str(A) + " + " + str(B) + " = " + str(A + B))
	i += 1
