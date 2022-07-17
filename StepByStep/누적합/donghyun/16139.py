import sys
from string import ascii_lowercase

input = sys.stdin.readline
s = input().strip()
d = {}
for a in ascii_lowercase:
	tmp = []
	c = 0
	for i in s:
		c += i == a 
		tmp.append(c)
	d[a] = tmp
for i in range(int(input())):
	a, f, t = input().split()
	f, t = int(f), int(t)
	ans = d[a][t]-d[a][f-1] if f else d[a][t]
	sys.stdout.write(str(ans)+"\n")