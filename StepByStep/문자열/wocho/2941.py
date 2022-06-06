import sys

input = sys.stdin.readline

s = input().rstrip()

N = len(s)
i, ans = 0, 0
while i < N:
	if s[i] == 'c':
		if i + 1 < N and (s[i + 1] == '=' or s[i + 1] == '-'):
			i += 1
	elif s[i] == 'd':
		if i + 2 < N and s[i + 1] == 'z' and s[i + 2] == '=':
			i += 2
		elif i + 1 < N and s[i + 1] == '-':
			i += 1
	elif s[i] == 'l':
		if i + 1 < N and s[i + 1] == 'j':
			i += 1
	elif s[i] == 'n':
		if i + 1 < N and s[i + 1] == 'j':
			i += 1
	elif s[i] == 's':
		if i + 1 < N and s[i + 1] == '=':
			i += 1
	elif s[i] == 'z':
		if i + 1 < N and s[i + 1] == '=':
			i += 1
	i, ans = i + 1, ans + 1

print(ans)