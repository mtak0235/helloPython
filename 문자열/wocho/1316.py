import sys

input = sys.stdin.readline

N = int(input())

cnt = 0
for _ in range(N):
	s = input().rstrip()
	length = len(s)
	lst = [False] * 26
	flag = True

	i = 0
	while i < length:
		c = s[i]
		if lst[ord(c) - 97] == False:
			lst[ord(c) - 97] = True
			i += 1
			while i < length and s[i] == c:
				i += 1
		else:
			flag = False
			break
	if flag:
		cnt += 1

print(cnt)