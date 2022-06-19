#
#
#

N = int(input())

for _ret, n in enumerate(range(1, N), start=1):
	for c in (str_n := str(n)):
		_ret += int(c)
	if _ret == N:
		print(n)
		break
else:
	print(0)
