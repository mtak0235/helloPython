N = int(input())

def recur(height, origin, dest):
	if height == 1:
		move.append(str(origin) + " " + str(dest))
		return
	if 1 != origin and 1 != dest:
		rest = 1
	elif 2 != origin and 2 != dest:
		rest = 2
	else:
		rest = 3
	recur(height - 1, origin, rest)
	move.append(str(origin) + " " + str(dest))
	recur(height - 1, rest, dest)

move = []
recur(N, 1, 3)

print(len(move))
print('\n'.join(move))