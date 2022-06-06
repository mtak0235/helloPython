import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

minus = input().split('-')
number = []
for i in minus:
	cnt = 0
	plus = i.split('+')
	for j in plus:
		cnt += int(j)
	number.append(cnt)
n = number[0]
for i in range(1, len(number)):
	n -= number[i]
print(n)