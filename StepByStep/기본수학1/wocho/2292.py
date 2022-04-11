N = int(input())

move = 1
while N > 1:
	N -= 6 * move
	move += 1

print(move)