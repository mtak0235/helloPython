import sys
layer = int(sys.stdin.readline())
for i in  range(layer):
	layer -= 1
	star = "*" * (i + 1)
	print(f'{star:>{layer}}')