import sys
layer = int(sys.stdin.readline())
for i in  range(layer):
	star = "*" * (i + 1)
	print(f'{star:>{layer}}')