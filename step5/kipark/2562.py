import sys

nlist = []
for i in range(9):
	a = int(sys.stdin.readline())
	nlist.append(a)

print(max(nlist))
print(nlist.index(max(nlist)) + 1)