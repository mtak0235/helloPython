import sys
layer = int(sys.stdin.readline())
for i in  range(layer):
	layer -= 1
	print("*" * (i + 1))