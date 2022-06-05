import sys
from collections import deque
input = sys.stdin.readline
n_cmd = int(input())
target = deque()


def push(s):
	target.append(s)


def pop():
    if len(target) == 0:
        print(-1)
    else:
        print(target.popleft())

def size():
		print(len(target))


def empty():
    if len(target):
        print(0)
    else:
        print(1)


def front():
    if (len(target) == 0):
        print(-1)
    else:
        print(target[0])


def back():
	if (len(target) == 0):
		print(-1)
	else:
		print(target[-1])

cmd = {
	'push' : push,
	'pop' : pop,
	'size' : size,
	'empty' : empty,
	'front' : front,
	'back' : back
}
for i in range(n_cmd):
	get = input().strip().split()
	if len(get) == 2:
		cmd[get[0]](int(get[1]))
	elif len(get) == 1:
		cmd[get[0]]()