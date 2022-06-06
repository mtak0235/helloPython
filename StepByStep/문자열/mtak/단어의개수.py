import sys
_input = sys.stdin.readline().strip().split(" ")
if _input[0] == "":
	print("0")
else:
	print(len(_input))