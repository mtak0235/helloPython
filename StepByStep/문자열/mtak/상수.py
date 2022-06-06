import sys
def rev(target):
	ret = ""
	for c in target:
		ret = c + ret
	return ret
a, b = map(rev, sys.stdin.readline().split())
_to_print = a if int(a) > int(b) else b
print(_to_print)