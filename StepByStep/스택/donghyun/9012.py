import sys

input = sys.stdin.readline
for _ in range(int(input())):
	l = 0
	for i in input().strip():
		l += 1 if i == '(' else -1
		if l < 0:
			print("NO")
			break
	else:
		print("NO") if l else print("YES")