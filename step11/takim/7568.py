n = int(input())
humans = [None] * n
for i in range(n):
	humans[i] = tuple(map(int, input().split()))
chart = [None] * n

def compare(h1, h2):
	if ((h1[0] > h2[0]) and(h1[1] > h2[1])):
		return 1
	elif ((h1[0] < h2[0]) and(h1[1] < h2[1])):
		return -1
	else:
		return 0
for i in range(n):
	rank = 1
	for j in range(n):
		if compare(humans[i], humans[j]) < 0:
			rank += 1
		chart[i] = rank
for i in range(n):
	print(chart[i], end=" ")
