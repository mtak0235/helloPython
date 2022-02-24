N = int(input())

def recur(height, origin, dest):
	if height == 1:
		move.append(str(origin) + " " + str(dest))
		return
	rest = 6 - origin - dest
	recur(height - 1, origin, rest)
	move.append(str(origin) + " " + str(dest))
	recur(height - 1, rest, dest)

move = []
recur(N, 1, 3)

print(2 ** N - 1)
print('\n'.join(move))