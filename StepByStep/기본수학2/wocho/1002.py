import sys, math

input = sys.stdin.readline

T = int(input())

ans = []
for _ in range(T):
	x1, y1, r1, x2, y2, r2 = map(int, input().split())
	dx = x1 - x2
	dy = y1 - y2
	dist = math.sqrt(dx * dx + dy * dy)
	if r1 >= r2:
		rmax = r1
		rmin = r2
	else:
		rmax = r2
		rmin = r1
	if dist == 0:
		if rmax == rmin:
			ans.append(str(-1))
		else:
			ans.append(str(0))
	elif dist < rmax:
		if dist + rmin < rmax:
			ans.append(str(0))
		elif dist + rmin > rmax:
			ans.append(str(2))
		else:
			ans.append(str(1))
	elif dist == rmax:
		ans.append(str(2))
	else:
		if dist > rmax + rmin:
			ans.append(str(0))
		elif dist < rmax + rmin:
			ans.append(str(2))
		else:
			ans.append(str(1))

print('\n'.join(ans))