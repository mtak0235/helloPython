import sys
input = sys.stdin.readline
cnt = int(input())
s = list()
for _ in range(cnt):
	i = int(input())
	if i == 0:
		s.pop()
		continue
	s.append(i)
print(sum(s))
