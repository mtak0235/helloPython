#
#
#

N = int(input())
q = [i for i in range(1, 1250000)]
top, bot = 0, N - 1

while top != bot:
	top += 1
	if top == bot:
		break
	c = q[top]
	top += 1

	bot += 1
	q[bot] = c
	
print(q[top])
