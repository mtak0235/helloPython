import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

def check_dot():
	a = 0
	b = 0
	c = [0]
	d = 1
	cnt = 0
	n = list(input().rstrip())
	while True:
		if a < 0 or b < 0 or d == 0:
			print("no")
			break
		if n[cnt] == '.':
			if cnt == 0:
				return 0
			if a == 0 and b == 0:
				print("yes")
			else :
				print("no")
			break
		elif n[cnt] == '(':
			a += 1
			c.append(1)
		elif n[cnt] == '[':
			b += 1
			c.append(-1)
		elif n[cnt] == ')':
			if c[a + b] == 1:
				a -= 1
				c.pop()
			else :
				d = 0
		elif n[cnt] == ']':
			if c[a + b] == -1:
				b -= 1
				c.pop()
			else :
				d = 0
		cnt += 1
	return 1

temp = 1
while (temp):
	temp = check_dot()