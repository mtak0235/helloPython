#
#
#


import sys

##############
print = sys.stdout.write
#############

stack = [0] * 100001
N = int(input())

size = 0
idx = -1

cmds = [sys.stdin.readline().strip() for i in range(N)]

for line in cmds:
	_cmd = line.split()
	cmd = _cmd[0]
	if cmd == "push":
		n = _cmd[1]
		idx += 1
		stack[idx] = n
		size += 1
	elif cmd == "pop":
		if size == 0:
			print("%s\n" % "-1")
		else:
			size -= 1
			n = stack[idx]
			idx -= 1
			print("%s\n" % n)
	elif cmd == "size":
		print("%s\n" % str(size))
	elif cmd == "empty":
		if size == 0:
			print("%s\n" % "1")
		else:
			print("%s\n" % "0")
	elif cmd == "top":
		if size == 0:
			print("%s\n" % "-1")
		else:
			n = stack[idx]
			print("%s\n" % n)

