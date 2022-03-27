import sys # what is the import L?

array = list()
for i in range(10):
	array.append(int(sys.stdin.readline().strip()) % 42)

print(len(set(array)))